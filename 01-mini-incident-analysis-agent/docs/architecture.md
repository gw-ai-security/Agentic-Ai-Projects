# Architecture

## Current State in Phase 3
- repository scaffold exists
- documentation exists
- local data context (assets, runbooks, incidents) is prepared
- core structures (schemas, prompts, formatter, main runner) are structured
- agent and tool implementation is not yet in place

## Planned Components

### 1. Input Layer
local incident text input

### 2. Agent Layer
planned analysis and structured reasoning

### 3. Tool Layer
planned controlled context tools:
- get_runbook(issue_type)
- get_asset_context(asset_id)

### 4. Output Layer
planned Markdown incident report

## Planned Data Flow
1. incident text is provided
2. incident is analyzed
3. optional context is retrieved
4. structured report is generated

## Design Rationale
- deliberately small prototype
- simple, explainable architecture
- interview-ready, not production-ready
