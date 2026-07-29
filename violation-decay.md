# Violation Decay Case Study

Generated: 2026-07-29T08:08:05.998811+00:00

## Claim
partial-evidence-flag cooled from 58 to 0 weekly hits; factual-claim-verification is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1526
- Distinct contracts in log: 58
- Distinct failure modes: 20
- Eligible contracts: 41
- Cooled contracts: 37
- Hotter contracts: 2

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `partial-evidence-flag` | 232 | 58 | 0 | -58 | -100.0% |
| `persistent-correction` | 158 | 46 | 0 | -46 | -100.0% |
| `self-verification` | 86 | 28 | 0 | -28 | -100.0% |
| `completion-artifact` | 73 | 26 | 3 | -23 | -88.5% |
| `behavioral-haiku-guard` | 33 | 19 | 0 | -19 | -100.0% |
| `commit-hash-verification` | 43 | 20 | 8 | -12 | -60.0% |
| `sensitive-write-router` | 12 | 11 | 1 | -10 | -90.9% |
| `dox-guard` | 11 | 10 | 1 | -9 | -90.0% |
| `platform-action-precheck` | 137 | 30 | 22 | -8 | -26.7% |
| `high-stakes-pre-critique` | 17 | 8 | 0 | -8 | -100.0% |
| `balar-clarification` | 8 | 8 | 0 | -8 | -100.0% |
| `loop-name-validation-guard` | 25 | 7 | 0 | -7 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `factual-claim-verification` | 114 | 14 | 18 | +4 | +28.6% |
| `state-assertion-grounding` | 181 | 42 | 45 | +3 | +7.1% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
