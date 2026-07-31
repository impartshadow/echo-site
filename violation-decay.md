# Violation Decay Case Study

Generated: 2026-07-31T08:13:33.055984+00:00

## Claim
partial-evidence-flag cooled from 61 to 0 weekly hits; state-assertion-grounding is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1446
- Distinct contracts in log: 64
- Distinct failure modes: 22
- Eligible contracts: 42
- Cooled contracts: 37
- Hotter contracts: 2

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `partial-evidence-flag` | 217 | 61 | 0 | -61 | -100.0% |
| `persistent-correction` | 143 | 55 | 0 | -55 | -100.0% |
| `platform-action-precheck` | 128 | 31 | 0 | -31 | -100.0% |
| `self-verification` | 80 | 25 | 0 | -25 | -100.0% |
| `factual-claim-verification` | 111 | 21 | 7 | -14 | -66.7% |
| `behavioral-haiku-guard` | 27 | 14 | 0 | -14 | -100.0% |
| `commit-hash-verification` | 45 | 24 | 11 | -13 | -54.2% |
| `high-stakes-pre-critique` | 16 | 10 | 0 | -10 | -100.0% |
| `sensitive-write-router` | 12 | 11 | 1 | -10 | -90.9% |
| `stale-state-assertion-guard` | 81 | 16 | 7 | -9 | -56.2% |
| `dox-guard` | 11 | 10 | 1 | -9 | -90.0% |
| `loop-name-validation-guard` | 23 | 8 | 0 | -8 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `state-assertion-grounding` | 166 | 20 | 32 | +12 | +60.0% |
| `unbuilt-guarantee-guard` | 7 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
