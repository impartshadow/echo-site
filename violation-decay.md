# Violation Decay Case Study

Generated: 2026-08-25T08:08:25.133622+00:00

## Claim
spawn-lifecycle-claim-guard cooled from 75 to 0 weekly hits; stale-state-assertion-guard is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1045
- Distinct contracts in log: 60
- Distinct failure modes: 18
- Eligible contracts: 48
- Cooled contracts: 43
- Hotter contracts: 3

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `spawn-lifecycle-claim-guard` | 81 | 75 | 0 | -75 | -100.0% |
| `state-assertion-grounding` | 98 | 48 | 8 | -40 | -83.3% |
| `state-assertion-grounding-gate` | 33 | 33 | 0 | -33 | -100.0% |
| `mutable-state-grounding-guard` | 27 | 27 | 0 | -27 | -100.0% |
| `crypto-price-claim-guard` | 20 | 19 | 0 | -19 | -100.0% |
| `terminal-state-evidence-gate` | 28 | 20 | 3 | -17 | -85.0% |
| `verification-vocabulary-gate` | 104 | 23 | 8 | -15 | -65.2% |
| `commit-hash-verification` | 15 | 11 | 1 | -10 | -90.9% |
| `question-referent-grounding-gate` | 8 | 8 | 0 | -8 | -100.0% |
| `pressure-framing-guard` | 12 | 5 | 0 | -5 | -100.0% |
| `numeric-parameter-assertion-guard` | 11 | 5 | 0 | -5 | -100.0% |
| `bitwarden-claim-verification-guard` | 8 | 5 | 0 | -5 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `stale-state-assertion-guard` | 75 | 6 | 14 | +8 | +133.3% |
| `factual-claim-verification` | 97 | 12 | 13 | +1 | +8.3% |
| `unbuilt-guarantee-guard` | 8 | 2 | 3 | +1 | +50.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
