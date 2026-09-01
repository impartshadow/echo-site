# Violation Decay Case Study

Generated: 2026-09-01T08:22:29.813777+00:00

## Claim
typed-claim-entailment-gate cooled from 246 to 0 weekly hits; privacy-exposure-taxonomy is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1026
- Distinct contracts in log: 61
- Distinct failure modes: 18
- Eligible contracts: 53
- Cooled contracts: 52
- Hotter contracts: 1

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `typed-claim-entailment-gate` | 246 | 246 | 0 | -246 | -100.0% |
| `spawn-lifecycle-claim-guard` | 81 | 75 | 0 | -75 | -100.0% |
| `state-assertion-grounding-gate` | 33 | 33 | 0 | -33 | -100.0% |
| `factual-claim-verification` | 100 | 37 | 10 | -27 | -73.0% |
| `state-assertion-grounding` | 80 | 34 | 7 | -27 | -79.4% |
| `mutable-state-grounding-guard` | 27 | 27 | 0 | -27 | -100.0% |
| `verification-vocabulary-gate` | 93 | 30 | 10 | -20 | -66.7% |
| `terminal-state-evidence-gate` | 28 | 20 | 1 | -19 | -95.0% |
| `crypto-price-claim-guard` | 20 | 19 | 0 | -19 | -100.0% |
| `stale-state-assertion-guard` | 83 | 20 | 12 | -8 | -40.0% |
| `question-referent-grounding-gate` | 8 | 8 | 0 | -8 | -100.0% |
| `fleet-state-claim-grounding-gate` | 37 | 13 | 6 | -7 | -53.8% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `privacy-exposure-taxonomy` | 11 | 4 | 5 | +1 | +25.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
