import os
from dotenv import load_dotenv

from src.agent import IncidentAgent
from src.formatter import save_markdown_report

def main():
    # 1. Load environment variables
    load_dotenv()
    
    # 2. Read configuration
    api_key = os.getenv("OPENAI_API_KEY", "")
    model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")
    
    if not api_key or api_key == "your_api_key_here":
        print("Warning: OPENAI_API_KEY is missing or not set in .env. Running without LLM.")
        api_key = ""
        
    # 3. Read the sample incident file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    incident_path = os.path.join(base_dir, "data", "sample_incidents", "incident_01_timeout.txt")
    
    with open(incident_path, "r", encoding="utf-8") as f:
        incident_text = f.read()
        
    # 4. Short status output indicating readiness
    print("--- Mini Incident Analysis Agent (Phase 5) ---")
    print(f"Model configured: {model_name}")
    print(f"Loaded incident from {os.path.basename(incident_path)} ({len(incident_text)} chars)")
    print("-------------------------------------------------------")
    
    # 5. Initialize Agent and Analyze
    agent = IncidentAgent(api_key=api_key, model_name=model_name)
    
    print("Analyzing incident...")
    report = agent.analyze_incident(incident_text)
    
    output_path = os.path.join(base_dir, "outputs", "incident_report.md")
    save_markdown_report(report, output_path)
    
    print("Analysis complete!")
    print(f"Summary: {report.incident_summary}")
    print(f"Used Tools: {', '.join(report.used_tools) if report.used_tools else 'none'}")
    print(f"Report saved to: {output_path}")

if __name__ == "__main__":
    main()
