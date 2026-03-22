# Agentic-AI-Projects

A curated repository of small, focused, and explainable Agentic AI projects.

This repository is designed to document a practical learning path across AI use case analysis, agentic workflows, controlled tool usage, systems engineering thinking, and security-aware prototyping. The goal is not to present inflated “production-ready” claims, but to show how realistic, well-scoped prototypes can be designed, implemented, documented, tested, and explained.

The projects in this repository are intentionally limited in scope. Each one is meant to demonstrate a concrete problem, a minimal technical solution, clear boundaries, and honest trade-offs.

---

## Why this repository exists

This repository serves three purposes:

1. **Show practical capability**  
   It demonstrates that agentic AI can be translated from abstract concepts into small, working prototypes with a clear input, decision logic, controlled context access, and structured output.

2. **Build structured understanding**  
   The projects are designed to strengthen reasoning about:
   - AI use case analysis
   - systems engineering
   - controlled tool integration
   - explainable agent behavior
   - security-aware implementation
   - technical documentation and communication

3. **Create a reusable learning path**  
   Someone who works through the projects step by step should not only understand the code, but also learn how to:
   - define scope tightly
   - avoid unnecessary complexity
   - structure repositories cleanly
   - separate implemented functionality from planned ideas
   - document assumptions, limitations, and risks honestly

---

## What this repository is meant to demonstrate

Across the projects in this repository, the focus is on demonstrating:

- **AI Use Case Analysis**  
  Identifying where LLMs and agentic workflows add real value and where deterministic logic, human review, or hard constraints remain necessary.

- **Agentic AI in a realistic small-project format**  
  Not as uncontrolled autonomy, but as bounded workflows where the system may analyze input, decide whether context is needed, call controlled tools, and generate a structured result.

- **Systems Engineering thinking**  
  Treating each project as a small system with inputs, components, boundaries, data flow, outputs, and explicit design rationale.

- **Controlled tool usage**  
  Especially in MCP-inspired setups where contextual information is retrieved in a limited, traceable, read-only way.

- **Security-aware prototyping**  
  Using environment variables, avoiding unnecessary privileges, keeping tools read-only where appropriate, and treating AI output as decision support rather than unquestioned truth.

- **Documentation and explainability**  
  Every useful prototype should be understandable by another person without requiring reverse engineering of the codebase.

---

## What someone learns by working through these projects

A reader who studies and rebuilds these projects should gain practical experience in:

### Technical skills
- Python-based AI prototyping
- prompt design for structured outputs
- schema-based output handling
- local tool integration
- deterministic pre-processing combined with LLM reasoning
- Markdown and JSON based reporting
- repository structure and implementation hygiene

### Conceptual skills
- evaluating whether an AI use case is actually useful
- distinguishing agentic behavior from simple text generation
- identifying where autonomy should stop
- balancing deterministic logic and probabilistic reasoning
- designing small architectures that remain explainable

### Engineering habits
- working phase by phase
- avoiding scope creep
- documenting assumptions and boundaries
- keeping prototypes testable and interview-ready
- making realistic claims about what a project does and does not prove

---

## Repository principles

The projects in this repository follow a few consistent principles:

- small scope over artificial complexity
- explainability over cleverness
- controlled tool usage over uncontrolled autonomy
- documentation before expansion
- security-aware defaults
- honest positioning over inflated claims

This repository does **not** aim to showcase large autonomous multi-agent platforms, enterprise-scale infrastructure, or production-grade AI systems. It aims to show disciplined prototyping.

---

## Current and planned projects

### Project 01 — Mini Incident Analysis Agent
**Status:** Completed

A small AI-assisted incident triage prototype. It analyzes a technical incident description, optionally retrieves limited contextual information through local tools, and generates a structured incident report.

**What it demonstrates**
- AI use case analysis
- systems engineering context
- controlled tool usage
- agentic decision logic in a minimal form
- read-only context access
- structured output generation
- security-aware design and documentation

---

### Project 02 — Log Correlation Summary Agent
A compact prototype that ingests a small set of related system log excerpts, groups likely related events, and produces an explainable summary of suspected root-cause patterns.

**Focus**
- event correlation logic
- structured summarization
- signal vs. noise reduction
- traceable reasoning from raw logs to operational summary

---

### Project 03 — Change Risk Review Agent
A small agent that reviews a planned infrastructure or application change description and generates a structured risk briefing, including likely failure points, affected areas, rollback concerns, and human review notes.

**Focus**
- change analysis
- risk framing
- structured pre-deployment review
- security and operational awareness

---

### Project 04 — Runbook Retrieval and Action Guidance Agent
A bounded assistant that maps a problem description to a likely runbook category, retrieves the matching internal guidance from local sources, and produces a concise action recommendation for first-level responders.

**Focus**
- retrieval with constrained tool access
- operational support
- explainable recommendation generation
- safe decision-support workflows

---

### Project 05 — Security Control Mapping Agent
A prototype that takes a short scenario, policy statement, or system description and maps it to relevant security controls or governance requirements in a structured, human-readable format.

**Focus**
- compliance-aware AI support
- structured mapping logic
- documentation quality
- clearly bounded interpretation support

---

### Project 06 — Service Dependency Explainer
A small system that takes a simplified service description or dependency list and generates an understandable explanation of upstream/downstream impact, critical dependencies, and likely operational consequences of failures.

**Focus**
- systems thinking
- dependency reasoning
- technical explanation quality
- operational communication

---

### Project 07 — Alert Deduplication and Prioritization Agent
A narrow prototype that reviews multiple alerts, identifies likely duplicates or near-duplicates, and returns a cleaner, prioritized alert view with justification.

**Focus**
- triage support
- prioritization logic
- bounded agentic reasoning
- operational relevance

---

## Suggested repository structure

```text
Agentic-AI-Projects/
│
├── README.md
│
├── 01-mini-incident-analysis-agent/
├── 02-log-correlation-summary-agent/
├── 03-change-risk-review-agent/
├── 04-runbook-retrieval-action-guidance-agent/
├── 05-security-control-mapping-agent/
├── 06-service-dependency-explainer/
└── 07-alert-deduplication-prioritization-agent/
