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

Phase 4 tool layer is strictly read-only and accesses only local JSON files. It makes no network requests and has no side-effects. Phase 5 agent makes outbound network requests only to the configured LLM API. Outputs remain a decision support tool requiring human review.
