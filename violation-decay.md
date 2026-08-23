# Violation Decay Case Study

Generated: 2026-08-23T08:23:39.979651+00:00

## Claim
spawn-lifecycle-claim-guard cooled from 75 to 0 weekly hits; stale-state-assertion-guard is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1091
- Distinct contracts in log: 62
- Distinct failure modes: 18
- Eligible contracts: 50
- Cooled contracts: 41
- Hotter contracts: 3

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `spawn-lifecycle-claim-guard` | 81 | 75 | 0 | -75 | -100.0% |
| `state-assertion-grounding-gate` | 33 | 33 | 0 | -33 | -100.0% |
| `state-assertion-grounding` | 117 | 41 | 15 | -26 | -63.4% |
| `platform-action-precheck` | 24 | 20 | 2 | -18 | -90.0% |
| `crypto-price-claim-guard` | 20 | 19 | 1 | -18 | -94.7% |
| `commit-hash-verification` | 15 | 11 | 1 | -10 | -90.9% |
| `question-referent-grounding-gate` | 8 | 8 | 0 | -8 | -100.0% |
| `verification-vocabulary-gate` | 113 | 24 | 18 | -6 | -25.0% |
| `concurrence-grounding` | 18 | 5 | 0 | -5 | -100.0% |
| `platform-action-param-schema-guard` | 5 | 5 | 0 | -5 | -100.0% |
| `factual-claim-verification` | 100 | 15 | 11 | -4 | -26.7% |
| `numeric-parameter-assertion-guard` | 11 | 5 | 1 | -4 | -80.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `stale-state-assertion-guard` | 73 | 6 | 10 | +4 | +66.7% |
| `manual-handoff-guard` | 5 | 1 | 4 | +3 | +300.0% |
| `terminal-state-evidence-gate` | 31 | 3 | 4 | +1 | +33.3% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
