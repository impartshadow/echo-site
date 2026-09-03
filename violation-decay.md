# Violation Decay Case Study

Generated: 2026-09-03T08:17:47.025092+00:00

## Claim
typed-claim-entailment-gate cooled from 246 to 0 weekly hits; privacy-exposure-taxonomy is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 962
- Distinct contracts in log: 57
- Distinct failure modes: 17
- Eligible contracts: 50
- Cooled contracts: 48
- Hotter contracts: 2

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `typed-claim-entailment-gate` | 246 | 246 | 0 | -246 | -100.0% |
| `spawn-lifecycle-claim-guard` | 81 | 75 | 0 | -75 | -100.0% |
| `state-assertion-grounding-gate` | 33 | 33 | 0 | -33 | -100.0% |
| `factual-claim-verification` | 90 | 41 | 12 | -29 | -70.7% |
| `verification-vocabulary-gate` | 90 | 44 | 16 | -28 | -63.6% |
| `mutable-state-grounding-guard` | 27 | 27 | 0 | -27 | -100.0% |
| `stale-state-assertion-guard` | 80 | 37 | 11 | -26 | -70.3% |
| `crypto-price-claim-guard` | 20 | 19 | 0 | -19 | -100.0% |
| `state-assertion-grounding` | 57 | 20 | 10 | -10 | -50.0% |
| `question-referent-grounding-gate` | 8 | 8 | 0 | -8 | -100.0% |
| `fleet-state-claim-grounding-gate` | 38 | 13 | 6 | -7 | -53.8% |
| `concurrence-grounding` | 11 | 7 | 0 | -7 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `privacy-exposure-taxonomy` | 19 | 4 | 13 | +9 | +225.0% |
| `pressure-framing-guard` | 7 | 1 | 4 | +3 | +300.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
