from typing import List

from pydantic import BaseModel


class IncidentReport(BaseModel):
    incident_summary: str
    incident_category: str
    severity: str
    affected_component: str
    confidence: str
    reasoning: str
    recommended_actions: List[str]
    used_tools: List[str]