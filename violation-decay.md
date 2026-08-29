# Violation Decay Case Study

Generated: 2026-08-29T08:45:45.697556+00:00

## Claim
spawn-lifecycle-claim-guard cooled from 75 to 0 weekly hits; stale-state-assertion-guard is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1022
- Distinct contracts in log: 60
- Distinct failure modes: 18
- Eligible contracts: 48
- Cooled contracts: 45
- Hotter contracts: 2

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `spawn-lifecycle-claim-guard` | 81 | 75 | 0 | -75 | -100.0% |
| `state-assertion-grounding-gate` | 33 | 33 | 0 | -33 | -100.0% |
| `state-assertion-grounding` | 85 | 38 | 11 | -27 | -71.1% |
| `mutable-state-grounding-guard` | 27 | 27 | 0 | -27 | -100.0% |
| `crypto-price-claim-guard` | 20 | 19 | 0 | -19 | -100.0% |
| `terminal-state-evidence-gate` | 28 | 20 | 2 | -18 | -90.0% |
| `verification-vocabulary-gate` | 94 | 18 | 8 | -10 | -55.6% |
| `question-referent-grounding-gate` | 8 | 8 | 0 | -8 | -100.0% |
| `factual-claim-verification` | 97 | 21 | 15 | -6 | -28.6% |
| `pressure-framing-guard` | 15 | 9 | 4 | -5 | -55.6% |
| `numeric-parameter-assertion-guard` | 11 | 5 | 0 | -5 | -100.0% |
| `bitwarden-claim-verification-guard` | 8 | 5 | 0 | -5 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `stale-state-assertion-guard` | 80 | 8 | 18 | +10 | +125.0% |
| `unbuilt-guarantee-guard` | 8 | 2 | 4 | +2 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
