import os
from dotenv import load_dotenv

def main():
    # 1. Load environment variables
    load_dotenv()
    
    # 2. Read MODEL_NAME with a sensible default
    model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")
    
    # 3. Read the sample incident file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    incident_path = os.path.join(base_dir, "data", "sample_incidents", "incident_01_timeout.txt")
    
    with open(incident_path, "r", encoding="utf-8") as f:
        incident_text = f.read()
        
    # 4. Short status output indicating readiness
    print("--- Mini Incident Analysis Agent (Phase 3 Scaffold) ---")
    print(f"Model configured: {model_name}")
    print(f"Loaded incident from {os.path.basename(incident_path)} ({len(incident_text)} chars)")
    print("-------------------------------------------------------")
    
    # 5. Clear TODO pointers to Phase 5
    print("TODO (Phase 5): Initialize Agent (src.agent) here.")
    print("TODO (Phase 5): Execute Agent with incident text.")
    print("TODO (Phase 5): Save Markdown Report via src.formatter.")

if __name__ == "__main__":
    main()
