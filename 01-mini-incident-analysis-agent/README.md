# Mini Incident Analysis Agent

## Overview
This project is a deliberately small prototype.
The objective is to analyze a technical incident description, potentially retrieve controlled contextual information in a later phase, and produce a structured incident report.

## Current Repository Status
**Project Closed (Local Ollama Version)**. The deliberate small prototype is complete. It features local data context, a local read-only tool layer (MCP-Lite), and a deterministic agent orchestrator powered by local execution via Ollama. It executes end-to-end entirely locally on three sample incidents, outputting Markdown reports.

## Why this project
- AI use case analysis
- systems engineering context
- controlled tool usage in a small prototype
- agentic AI in minimal form
- security-aware design
- explainable documentation

## Planned Workflow
Input Incident -> Analysis -> Optional Context Lookup -> Structured Markdown Report

## Repository Structure
- `data/`: Will contain mock data and sample incidents in later phases.
- `docs/`: Contains project planning and architecture documentation.
- `src/`: Will contain the Python implementation logic. Currently only placeholders.
- `outputs/`: Will store the generated markdown reports.

## Setup

To set up the project locally with Ollama, run the following commands:

```bash
# 1. Start the local Ollama container
docker compose up -d ollama

# 2. Pull the required model
docker exec -it ollama ollama pull llama3.2

# 3. Create a virtual environment
python -m venv .venv

# 4. Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
# source .venv/bin/activate

# 5. Install requirements
pip install -r requirements.txt

# 6. Copy .env.example to .env
# Windows: copy .env.example .env
# Unix: cp .env.example .env
```

7. Execute the agent: `python -m src.main`

## Scope Limits
- no UI
- no database
- no multi-agent architecture
- no production integration
- no autonomous remediation

This repository contains the finalized prototype. The planned extended phases (Phase 7) were deliberately omitted to keep the project strictly focused, readable, and interview-ready. No production-ready or true autonomous MCP features are provided.
