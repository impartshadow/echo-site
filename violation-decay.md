# Violation Decay Case Study

Generated: 2026-08-31T08:21:56.017704+00:00

## Claim
typed-claim-entailment-gate cooled from 246 to 0 weekly hits; privacy-exposure-taxonomy is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 989
- Distinct contracts in log: 58
- Distinct failure modes: 18
- Eligible contracts: 52
- Cooled contracts: 51
- Hotter contracts: 1

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `typed-claim-entailment-gate` | 246 | 246 | 0 | -246 | -100.0% |
| `spawn-lifecycle-claim-guard` | 81 | 75 | 0 | -75 | -100.0% |
| `state-assertion-grounding-gate` | 33 | 33 | 0 | -33 | -100.0% |
| `mutable-state-grounding-guard` | 27 | 27 | 0 | -27 | -100.0% |
| `state-assertion-grounding` | 79 | 34 | 8 | -26 | -76.5% |
| `factual-claim-verification` | 97 | 37 | 13 | -24 | -64.9% |
| `verification-vocabulary-gate` | 92 | 30 | 11 | -19 | -63.3% |
| `terminal-state-evidence-gate` | 28 | 20 | 1 | -19 | -95.0% |
| `crypto-price-claim-guard` | 20 | 19 | 0 | -19 | -100.0% |
| `question-referent-grounding-gate` | 8 | 8 | 0 | -8 | -100.0% |
| `stale-state-assertion-guard` | 79 | 20 | 15 | -5 | -25.0% |
| `concurrence-grounding` | 12 | 5 | 0 | -5 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `privacy-exposure-taxonomy` | 11 | 4 | 7 | +3 | +75.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
