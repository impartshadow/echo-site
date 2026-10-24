# Violation Decay Case Study

Generated: 2026-10-24T08:37:53.303051+00:00

## Claim
state-assertion-grounding cooled from 7 to 0 weekly hits; live-state-claim-guard is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 276
- Distinct contracts in log: 72
- Distinct failure modes: 24
- Eligible contracts: 56
- Cooled contracts: 47
- Hotter contracts: 2

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `state-assertion-grounding` | 12 | 7 | 0 | -7 | -100.0% |
| `cleanup-claim-mechanism-gate` | 9 | 6 | 0 | -6 | -100.0% |
| `dox-guard` | 8 | 6 | 0 | -6 | -100.0% |
| `pressure-framing-guard` | 9 | 5 | 0 | -5 | -100.0% |
| `terminal-state-evidence-gate` | 8 | 5 | 1 | -4 | -80.0% |
| `ownership-ask-execution-gate` | 4 | 4 | 0 | -4 | -100.0% |
| `platform-message-id-claim-guard` | 4 | 4 | 0 | -4 | -100.0% |
| `repeat-complaint-stale-commit` | 4 | 4 | 0 | -4 | -100.0% |
| `chat-remark-validation-guard` | 5 | 4 | 1 | -3 | -75.0% |
| `privacy-exposure-taxonomy` | 5 | 4 | 1 | -3 | -75.0% |
| `recurring-failure-burn-in-guard` | 3 | 3 | 0 | -3 | -100.0% |
| `continuation-ambiguity-guard` | 8 | 5 | 3 | -2 | -40.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `live-state-claim-guard` | 10 | 3 | 5 | +2 | +66.7% |
| `self-diagnosis-execution-gate` | 3 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
