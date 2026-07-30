# Violation Decay Case Study

Generated: 2026-07-30T08:14:49.088729+00:00

## Claim
partial-evidence-flag cooled from 51 to 0 weekly hits; state-assertion-grounding is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1453
- Distinct contracts in log: 58
- Distinct failure modes: 20
- Eligible contracts: 43
- Cooled contracts: 40
- Hotter contracts: 1

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `partial-evidence-flag` | 220 | 51 | 0 | -51 | -100.0% |
| `persistent-correction` | 150 | 46 | 0 | -46 | -100.0% |
| `platform-action-precheck` | 130 | 31 | 2 | -29 | -93.5% |
| `self-verification` | 83 | 28 | 0 | -28 | -100.0% |
| `behavioral-haiku-guard` | 31 | 17 | 0 | -17 | -100.0% |
| `commit-hash-verification` | 45 | 24 | 11 | -13 | -54.2% |
| `sensitive-write-router` | 12 | 11 | 1 | -10 | -90.9% |
| `factual-claim-verification` | 114 | 17 | 8 | -9 | -52.9% |
| `loop-name-validation-guard` | 24 | 9 | 0 | -9 | -100.0% |
| `dox-guard` | 11 | 10 | 1 | -9 | -90.0% |
| `high-stakes-pre-critique` | 17 | 8 | 0 | -8 | -100.0% |
| `completion-artifact` | 58 | 11 | 4 | -7 | -63.6% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `state-assertion-grounding` | 159 | 20 | 30 | +10 | +50.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
