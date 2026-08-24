# Violation Decay Case Study

Generated: 2026-08-24T08:28:29.395746+00:00

## Claim
spawn-lifecycle-claim-guard cooled from 75 to 0 weekly hits; stale-state-assertion-guard is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1052
- Distinct contracts in log: 60
- Distinct failure modes: 18
- Eligible contracts: 48
- Cooled contracts: 41
- Hotter contracts: 2

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `spawn-lifecycle-claim-guard` | 81 | 75 | 0 | -75 | -100.0% |
| `state-assertion-grounding-gate` | 33 | 33 | 0 | -33 | -100.0% |
| `mutable-state-grounding-guard` | 27 | 27 | 0 | -27 | -100.0% |
| `state-assertion-grounding` | 105 | 32 | 10 | -22 | -68.8% |
| `crypto-price-claim-guard` | 20 | 19 | 0 | -19 | -100.0% |
| `terminal-state-evidence-gate` | 28 | 20 | 4 | -16 | -80.0% |
| `verification-vocabulary-gate` | 105 | 23 | 9 | -14 | -60.9% |
| `commit-hash-verification` | 15 | 11 | 1 | -10 | -90.9% |
| `question-referent-grounding-gate` | 8 | 8 | 0 | -8 | -100.0% |
| `concurrence-grounding` | 17 | 5 | 0 | -5 | -100.0% |
| `pressure-framing-guard` | 12 | 5 | 0 | -5 | -100.0% |
| `numeric-parameter-assertion-guard` | 11 | 5 | 0 | -5 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `stale-state-assertion-guard` | 75 | 7 | 12 | +5 | +71.4% |
| `unbuilt-guarantee-guard` | 8 | 2 | 3 | +1 | +50.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
