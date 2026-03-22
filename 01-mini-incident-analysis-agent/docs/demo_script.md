# Demo Script

## Purpose
A later demo should show a small AI-supported incident analysis workflow.

## Planned Demo Story
- one technical incident text
- identification of likely issue type
- optional contextual lookup
- structured report output

## What to Emphasize
- deliberately small prototype
- controlled tool usage
- explainable workflow
- human review remains necessary

This demo is final and executable end-to-end. The `src/main.py` script automatically runs through all three sample incidents (`timeout`, `auth_failure`, `data_delay`). The agent securely retrieves local context, executes the generation, and outputs three Markdown reports. Ensure your `.env` is configured for live LLM tests; otherwise, it will securely fall back to a local offline mode.
