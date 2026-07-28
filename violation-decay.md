# Violation Decay Case Study

Generated: 2026-07-28T08:14:35.597959+00:00

## Claim
partial-evidence-flag cooled from 57 to 0 weekly hits; factual-claim-verification is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1575
- Distinct contracts in log: 61
- Distinct failure modes: 22
- Eligible contracts: 47
- Cooled contracts: 43
- Hotter contracts: 3

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `partial-evidence-flag` | 235 | 57 | 0 | -57 | -100.0% |
| `persistent-correction` | 163 | 46 | 0 | -46 | -100.0% |
| `completion-artifact` | 74 | 26 | 3 | -23 | -88.5% |
| `self-verification` | 87 | 22 | 0 | -22 | -100.0% |
| `behavioral-haiku-guard` | 36 | 22 | 0 | -22 | -100.0% |
| `dox-guard` | 19 | 18 | 0 | -18 | -100.0% |
| `commit-hash-verification` | 42 | 20 | 7 | -13 | -65.0% |
| `sensitive-write-router` | 12 | 11 | 1 | -10 | -90.9% |
| `balar-clarification` | 9 | 9 | 0 | -9 | -100.0% |
| `platform-action-precheck` | 137 | 30 | 22 | -8 | -26.7% |
| `stale-state-assertion-guard` | 87 | 15 | 9 | -6 | -40.0% |
| `loop-name-validation-guard` | 26 | 6 | 0 | -6 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `factual-claim-verification` | 114 | 14 | 18 | +4 | +28.6% |
| `state-assertion-grounding` | 186 | 45 | 48 | +3 | +6.7% |
| `unbuilt-guarantee-guard` | 6 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
