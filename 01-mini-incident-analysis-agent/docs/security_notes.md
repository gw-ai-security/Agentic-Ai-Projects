# Security Notes

## Security Position
- read-only prototype mindset
- no autonomous system changes
- no production access

## Planned Security Measures
- API keys in .env only
- no hardcoded secrets
- no production data
- narrow, controlled tool inputs
- human review of generated outputs

## Risks
- wrong classification
- false confidence
- incomplete context
- unsafe future scope expansion

## Mitigation
- keep the scope small
- separate documentation from implementation claims
- keep tools read-only in later phases
- require human review

The final prototype tool layer is strictly read-only and accesses only local JSON files. It makes no network requests and has no side-effects. The agent module communicates only with a locally containerized Ollama instance on localhost. This eliminates external LLM data leaks. Outputs are purely for decision support, requiring human review. No production systems are integrated.
