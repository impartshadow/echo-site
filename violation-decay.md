# Violation Decay Case Study

Generated: 2026-08-28T08:15:58.588466+00:00

## Claim
spawn-lifecycle-claim-guard cooled from 75 to 0 weekly hits; stale-state-assertion-guard is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1013
- Distinct contracts in log: 59
- Distinct failure modes: 18
- Eligible contracts: 49
- Cooled contracts: 46
- Hotter contracts: 2

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `spawn-lifecycle-claim-guard` | 81 | 75 | 0 | -75 | -100.0% |
| `state-assertion-grounding-gate` | 33 | 33 | 0 | -33 | -100.0% |
| `state-assertion-grounding` | 83 | 38 | 9 | -29 | -76.3% |
| `mutable-state-grounding-guard` | 27 | 27 | 0 | -27 | -100.0% |
| `crypto-price-claim-guard` | 20 | 19 | 0 | -19 | -100.0% |
| `terminal-state-evidence-gate` | 28 | 20 | 2 | -18 | -90.0% |
| `verification-vocabulary-gate` | 93 | 18 | 6 | -12 | -66.7% |
| `question-referent-grounding-gate` | 8 | 8 | 0 | -8 | -100.0% |
| `pressure-framing-guard` | 13 | 9 | 2 | -7 | -77.8% |
| `factual-claim-verification` | 96 | 21 | 15 | -6 | -28.6% |
| `numeric-parameter-assertion-guard` | 11 | 5 | 0 | -5 | -100.0% |
| `bitwarden-claim-verification-guard` | 8 | 5 | 0 | -5 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `stale-state-assertion-guard` | 78 | 8 | 18 | +10 | +125.0% |
| `unbuilt-guarantee-guard` | 8 | 2 | 4 | +2 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
