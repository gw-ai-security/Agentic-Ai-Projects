import os
import json
from typing import Dict, Any

# Define the data directory relative to this file
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")

def _load_json(filename: str) -> list:
    """Helper to load a JSON file from the data directory. Read-only."""
    filepath = os.path.join(DATA_DIR, filename)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def get_runbook(issue_type: str) -> Dict[str, Any]:
    """
    Retrieves the runbook for a given issue type.
    Read-only local context access.
    """
    runbooks = _load_json("runbooks.json")
    for rb in runbooks:
        if rb.get("issue_type") == issue_type:
            return rb
            
    # Fallback for unknown issue_type
    return {
        "issue_type": issue_type,
        "title": "Unknown Runbook",
        "steps": []
    }

def get_asset_context(asset_id: str) -> Dict[str, Any]:
    """
    Retrieves the asset context for a given asset ID.
    Read-only local context access.
    """
    assets = _load_json("assets.json")
    for asset in assets:
        if asset.get("asset_id") == asset_id:
            return asset
            
    # Fallback for unknown asset_id
    return {
        "asset_id": asset_id,
        "type": "Unknown",
        "criticality": "unknown",
        "owner_team": "unknown"
    }
