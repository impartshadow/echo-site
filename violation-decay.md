# Violation Decay Case Study

Generated: 2026-09-30T08:37:22.934716+00:00

## Claim
personal-token-send-guard cooled from 15 to 0 weekly hits.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 291
- Distinct contracts in log: 63
- Distinct failure modes: 20
- Eligible contracts: 34
- Cooled contracts: 34
- Hotter contracts: 0

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `personal-token-send-guard` | 15 | 15 | 0 | -15 | -100.0% |
| `raw-gmail-send-guard` | 12 | 12 | 0 | -12 | -100.0% |
| `privacy-exposure-taxonomy` | 16 | 11 | 0 | -11 | -100.0% |
| `factual-claim-verification` | 24 | 10 | 1 | -9 | -90.0% |
| `dox-guard` | 13 | 9 | 0 | -9 | -100.0% |
| `personal-help-provenance-carveout` | 9 | 9 | 0 | -9 | -100.0% |
| `verification-vocabulary-gate` | 8 | 8 | 0 | -8 | -100.0% |
| `state-assertion-grounding` | 24 | 11 | 4 | -7 | -63.6% |
| `stale-state-assertion-guard` | 20 | 8 | 1 | -7 | -87.5% |
| `terminal-state-evidence-gate` | 11 | 6 | 0 | -6 | -100.0% |
| `cleanup-claim-mechanism-gate` | 7 | 6 | 0 | -6 | -100.0% |
| `thin-context-brief-gate` | 8 | 6 | 1 | -5 | -83.3% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| n/a | 0 | 0 | 0 | 0 | n/a |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
