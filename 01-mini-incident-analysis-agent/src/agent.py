import json
from typing import Dict, Any
from openai import OpenAI

from src.schemas import IncidentReport
from src.prompts import SYSTEM_PROMPT, FINAL_REPORT_PROMPT
from src.mcp_server import get_runbook, get_asset_context

class IncidentAgent:
    def __init__(self, api_key: str, base_url: str, model_name: str):
        # Configure client for Ollama locally
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model_name = model_name

    def _detect_issue_type(self, incident_text: str) -> str:
        text = incident_text.lower()
        if "timeout" in text:
            return "timeout"
        if any(word in text for word in ["login", "auth", "token"]):
            return "auth_failure"
        if any(word in text for word in ["delay", "latency", "backlog"]):
            return "data_delay"
        return "unknown"

    def _detect_asset_id(self, incident_text: str) -> str:
        if "R-17" in incident_text:
            return "R-17"
        if "AUTH-02" in incident_text:
            return "AUTH-02"
        if "DP-09" in incident_text:
            return "DP-09"
        return "unknown"
        
    def _clean_json_response(self, text: str) -> str:
        text = text.strip()
        if text.startswith("```json"):
            text = text[7:]
        elif text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        return text.strip()

    def analyze_incident(self, incident_text: str) -> IncidentReport:
        issue_type = self._detect_issue_type(incident_text)
        asset_id = self._detect_asset_id(incident_text)
        
        used_tools = []
        runbook_context = "None"
        asset_context = "None"
        
        if issue_type != "unknown":
            runbook_context = json.dumps(get_runbook(issue_type), indent=2)
            used_tools.append("get_runbook")
            
        if asset_id != "unknown":
            asset_context = json.dumps(get_asset_context(asset_id), indent=2)
            used_tools.append("get_asset_context")
            
        final_prompt = FINAL_REPORT_PROMPT.format(
            incident_text=incident_text,
            runbook_context=runbook_context,
            asset_context=asset_context
        )
        final_prompt += "\nPlease return the result strictly as a valid JSON object."
        
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": final_prompt}
                ],
                response_format={"type": "json_object"},
                temperature=0.1
            )
            raw_json = response.choices[0].message.content
            clean_json = self._clean_json_response(raw_json)
            data = json.loads(clean_json)
            
            string_fields = ["incident_summary", "incident_category", "severity", "affected_component", "confidence", "reasoning"]
            for field in string_fields:
                if field in data:
                    if isinstance(data[field], list):
                        data[field] = " ".join(str(x) for x in data[field])
                    elif not isinstance(data[field], str):
                        data[field] = str(data[field])
                        
            if "recommended_actions" in data and not isinstance(data["recommended_actions"], list):
                if isinstance(data["recommended_actions"], str):
                    data["recommended_actions"] = [data["recommended_actions"]]
                else:
                    data["recommended_actions"] = [str(data["recommended_actions"])]
        except Exception as e:
            data = {
                "incident_summary": f"Failed to call LLM or parse response: {str(e)}",
                "incident_category": "Error",
                "severity": "Unknown",
                "affected_component": asset_id,
                "confidence": "low",
                "reasoning": "Exception during local Ollama inference or logic.",
                "recommended_actions": []
            }
            
        # Ensure used_tools is deterministically overridden by actual tools used
        data["used_tools"] = used_tools
        
        return IncidentReport(**data)
