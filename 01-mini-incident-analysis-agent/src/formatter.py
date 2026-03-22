import os
from src.schemas import IncidentReport

def save_markdown_report(report: IncidentReport, output_path: str) -> None:
    """Saves an IncidentReport to a Markdown file with UTF-8 encoding."""
    # Ensure directory exists
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    
    lines = []
    lines.append("# Incident Report\n")
    lines.append(f"## Summary\n{report.incident_summary}\n")
    lines.append(f"## Category\n{report.incident_category}\n")
    lines.append(f"## Severity\n{report.severity}\n")
    lines.append(f"## Affected Component\n{report.affected_component}\n")
    lines.append(f"## Confidence\n{report.confidence}\n")
    lines.append(f"## Reasoning\n{report.reasoning}\n")
    
    lines.append("## Recommended Actions")
    if report.recommended_actions:
        for action in report.recommended_actions:
            lines.append(f"- {action}")
    else:
        lines.append("- none")
    lines.append("")
    
    lines.append("## Used Tools")
    if report.used_tools:
        for tool in report.used_tools:
            lines.append(f"- {tool}")
    else:
        lines.append("- none")
    lines.append("")
    
    content = "\n".join(lines)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
