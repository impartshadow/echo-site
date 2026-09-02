# Violation Decay Case Study

Generated: 2026-09-02T08:28:39.176702+00:00

## Claim
typed-claim-entailment-gate cooled from 246 to 0 weekly hits; privacy-exposure-taxonomy is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 978
- Distinct contracts in log: 60
- Distinct failure modes: 17
- Eligible contracts: 53
- Cooled contracts: 52
- Hotter contracts: 1

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `typed-claim-entailment-gate` | 246 | 246 | 0 | -246 | -100.0% |
| `spawn-lifecycle-claim-guard` | 81 | 75 | 0 | -75 | -100.0% |
| `state-assertion-grounding-gate` | 33 | 33 | 0 | -33 | -100.0% |
| `factual-claim-verification` | 99 | 42 | 14 | -28 | -66.7% |
| `mutable-state-grounding-guard` | 27 | 27 | 0 | -27 | -100.0% |
| `verification-vocabulary-gate` | 93 | 34 | 12 | -22 | -64.7% |
| `stale-state-assertion-guard` | 81 | 31 | 12 | -19 | -61.3% |
| `crypto-price-claim-guard` | 20 | 19 | 0 | -19 | -100.0% |
| `fleet-state-claim-grounding-gate` | 37 | 13 | 5 | -8 | -61.5% |
| `question-referent-grounding-gate` | 8 | 8 | 0 | -8 | -100.0% |
| `numeric-parameter-assertion-guard` | 10 | 8 | 1 | -7 | -87.5% |
| `state-assertion-grounding` | 61 | 17 | 11 | -6 | -35.3% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `privacy-exposure-taxonomy` | 11 | 4 | 5 | +1 | +25.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
