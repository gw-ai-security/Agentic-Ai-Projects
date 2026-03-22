# Mini Incident Analysis Agent

## Overview
This project is a deliberately small prototype.
The objective is to analyze a technical incident description, potentially retrieve controlled contextual information in a later phase, and produce a structured incident report.

## Current Repository Status
Phase 1 scaffold, documentation, and Phase 2 local data context are in place. There is no incident processing implementation yet, and no MCP-like tool layer implemented yet.

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

To set up the project locally, run the following commands:

```bash
# 1. Create a virtual environment
python -m venv .venv

# 2. Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
# source .venv/bin/activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Copy .env.example to .env (use `copy` on Windows cmd)
cp .env.example .env
```

5. Open the `.env` file and add your `OPENAI_API_KEY`.
6. Implementation follows in later phases.

## Scope Limits
- no UI
- no database
- no multi-agent architecture
- no production integration
- no autonomous remediation

This repository currently contains the Phase 1 scaffold and Phase 2 local data context. Implementation logic and end-to-end execution are part of later phases.
