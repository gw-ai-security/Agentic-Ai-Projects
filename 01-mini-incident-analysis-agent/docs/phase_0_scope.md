# Phase 0 Scope

## Project Name
Mini Incident Analysis Agent

## Project Purpose
A small Python prototype analyzes a technical incident description, optionally retrieves controlled contextual information through local tools, and produces a structured incident report. It serves as a focused demonstration of context retrieval and markdown generation without unnecessary complexity.

## Core Use Case
- AI-supported incident triage for technical incident descriptions

## In Scope (Must Have)
- Incident-Text einlesen
- Incident grob klassifizieren
- Asset erkennen
- Runbook-Kontext abrufen
- Asset-Kontext abrufen
- Markdown-Report erzeugen

## Optional Later
- JSON-Output zusätzlich
- einfaches Logging
- einfacher Confidence Score

## Out of Scope / Not Now
- Web UI
- Datenbank
- mehrere Agenten
- Langzeit-Memory
- Auth-System
- Deployment/Infra
- autonome Remediation
- Produktivintegration
- echtes Ticket-System

## Fixed Architecture Constraints
- Python only
- one agent
- two tools maximum
- local JSON context only
- Markdown report as output
- deliberately small prototype

## Chosen Tools
- get_runbook(issue_type)
- get_asset_context(asset_id)

## Output Decision
- final output format: Markdown incident report

## Communication Guardrails
- do not claim production readiness
- do not overstate MCP
- do not overstate agentic AI
- distinguish implemented vs planned vs out of scope

## 30-Second Explanation
This project is a deliberately small, single-agent Python prototype that demonstrates AI-supported incident triage. Given a technical incident description, it uses up to two local tools to fetch relevant runbook and asset context, then generates a structured Markdown report to assist human operators.
