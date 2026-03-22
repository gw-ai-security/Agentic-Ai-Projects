import json
from typing import Dict, Any
from openai import OpenAI

from src.schemas import IncidentReport
from src.prompts import SYSTEM_PROMPT, FINAL_REPORT_PROMPT
from src.mcp_server import get_runbook, get_asset_context

class IncidentAgent:
    def __init__(self, api_key: str, model_name: str):
        self.client = OpenAI(api_key=api_key) if api_key else None
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
        
        if not self.client:
            # Fallback for local testing without API key
            return IncidentReport(
                incident_summary="API Key missing, dummy response generated.",
                incident_category="Unknown",
                severity="Unknown",
                affected_component=asset_id,
                confidence="low",
                reasoning="No LLM call made. Please configure OPENAI_API_KEY.",
                recommended_actions=["Configure OPENAI_API_KEY"],
                used_tools=used_tools
            )
            
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
        
        try:
            data = json.loads(clean_json)
        except json.JSONDecodeError:
            data = {
                "incident_summary": "Failed to parse LLM response.",
                "incident_category": "Error",
                "severity": "Unknown",
                "affected_component": asset_id,
                "confidence": "low",
                "reasoning": "JSON parsing error.",
                "recommended_actions": []
            }
            
        # Ensure used_tools is deterministically overridden by actual tools used
        data["used_tools"] = used_tools
        
        return IncidentReport(**data)
