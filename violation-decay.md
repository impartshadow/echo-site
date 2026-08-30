# Violation Decay Case Study

Generated: 2026-08-30T08:14:58.332791+00:00

## Claim
typed-claim-entailment-gate cooled from 246 to 0 weekly hits; stale-state-assertion-guard is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1018
- Distinct contracts in log: 58
- Distinct failure modes: 18
- Eligible contracts: 49
- Cooled contracts: 46
- Hotter contracts: 2

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `typed-claim-entailment-gate` | 246 | 246 | 0 | -246 | -100.0% |
| `spawn-lifecycle-claim-guard` | 81 | 75 | 0 | -75 | -100.0% |
| `state-assertion-grounding-gate` | 33 | 33 | 0 | -33 | -100.0% |
| `state-assertion-grounding` | 87 | 38 | 11 | -27 | -71.1% |
| `mutable-state-grounding-guard` | 27 | 27 | 0 | -27 | -100.0% |
| `factual-claim-verification` | 95 | 37 | 12 | -25 | -67.6% |
| `terminal-state-evidence-gate` | 29 | 20 | 1 | -19 | -95.0% |
| `crypto-price-claim-guard` | 20 | 19 | 0 | -19 | -100.0% |
| `verification-vocabulary-gate` | 99 | 18 | 10 | -8 | -44.4% |
| `question-referent-grounding-gate` | 8 | 8 | 0 | -8 | -100.0% |
| `pressure-framing-guard` | 15 | 9 | 4 | -5 | -55.6% |
| `numeric-parameter-assertion-guard` | 11 | 5 | 0 | -5 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `stale-state-assertion-guard` | 80 | 9 | 16 | +7 | +77.8% |
| `fleet-state-claim-grounding-gate` | 37 | 13 | 15 | +2 | +15.4% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
