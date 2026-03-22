import os
from dotenv import load_dotenv

from src.agent import IncidentAgent
from src.formatter import save_markdown_report

def main():
    # 1. Load environment variables
    load_dotenv()
    
    # 2. Read local Ollama configuration as standard
    api_key = os.getenv("LLM_API_KEY", "ollama")
    base_url = os.getenv("LLM_BASE_URL", "http://localhost:11434/v1/")
    model_name = os.getenv("MODEL_NAME", "llama3.2")
        
    print("--- Mini Incident Analysis Agent (Local Ollama Version) ---")
    print(f"Provider: Ollama @ {base_url}")
    print(f"Model configured: {model_name}\n")
    
    agent = IncidentAgent(api_key=api_key, base_url=base_url, model_name=model_name)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    incident_files = [
        "incident_01_timeout.txt", 
        "incident_02_auth.txt", 
        "incident_03_data_delay.txt"
    ]
    
    for filename in incident_files:
        incident_path = os.path.join(base_dir, "data", "sample_incidents", filename)
        try:
            with open(incident_path, "r", encoding="utf-8") as f:
                incident_text = f.read()
        except FileNotFoundError:
            print(f"Skipping {filename}: File not found.")
            continue
            
        print(f"Analyzing {filename}...")
        report = agent.analyze_incident(incident_text)
        
        out_name = os.path.splitext(filename)[0] + "_report.md"
        output_path = os.path.join(base_dir, "outputs", out_name)
        save_markdown_report(report, output_path)
        
        print(f"  -> Summary: {report.incident_summary}")
        print(f"  -> Used Tools: {', '.join(report.used_tools) if report.used_tools else 'none'}")
        print(f"  -> Saved to: outputs/{out_name}\n")

    print("-------------------------------------------------------")
    print("Project Execution Complete.")

if __name__ == "__main__":
    main()
