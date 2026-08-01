# Violation Decay Case Study

Generated: 2026-08-01T08:09:59.501176+00:00

## Claim
persistent-correction cooled from 84 to 0 weekly hits; state-assertion-grounding is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1405
- Distinct contracts in log: 63
- Distinct failure modes: 22
- Eligible contracts: 41
- Cooled contracts: 37
- Hotter contracts: 2

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `persistent-correction` | 139 | 84 | 0 | -84 | -100.0% |
| `partial-evidence-flag` | 214 | 60 | 0 | -60 | -100.0% |
| `platform-action-precheck` | 127 | 36 | 0 | -36 | -100.0% |
| `self-verification` | 76 | 22 | 0 | -22 | -100.0% |
| `factual-claim-verification` | 111 | 21 | 7 | -14 | -66.7% |
| `commit-hash-verification` | 45 | 24 | 11 | -13 | -54.2% |
| `behavioral-haiku-guard` | 21 | 12 | 0 | -12 | -100.0% |
| `completion-artifact` | 55 | 14 | 4 | -10 | -71.4% |
| `high-stakes-pre-critique` | 16 | 10 | 0 | -10 | -100.0% |
| `sensitive-write-router` | 12 | 11 | 1 | -10 | -90.9% |
| `stale-state-assertion-guard` | 80 | 16 | 7 | -9 | -56.2% |
| `loop-name-validation-guard` | 20 | 7 | 0 | -7 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `state-assertion-grounding` | 163 | 24 | 32 | +8 | +33.3% |
| `unbuilt-guarantee-guard` | 7 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
