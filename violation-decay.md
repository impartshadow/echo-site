# Violation Decay Case Study

Generated: 2026-08-03T08:12:28.042148+00:00

## Claim
partial-evidence-flag cooled from 128 to 0 weekly hits; state-assertion-grounding is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1444
- Distinct contracts in log: 66
- Distinct failure modes: 21
- Eligible contracts: 46
- Cooled contracts: 40
- Hotter contracts: 4

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `partial-evidence-flag` | 204 | 128 | 0 | -128 | -100.0% |
| `persistent-correction` | 131 | 89 | 0 | -89 | -100.0% |
| `completion-artifact` | 53 | 45 | 1 | -44 | -97.8% |
| `scope-coverage-guard` | 43 | 43 | 0 | -43 | -100.0% |
| `platform-action-precheck` | 125 | 34 | 2 | -32 | -94.1% |
| `stale-state-assertion-guard` | 84 | 40 | 8 | -32 | -80.0% |
| `verification-vocabulary-gate` | 83 | 53 | 21 | -32 | -60.4% |
| `factual-claim-verification` | 123 | 49 | 19 | -30 | -61.2% |
| `commit-hash-verification` | 43 | 32 | 10 | -22 | -68.8% |
| `self-verification` | 70 | 21 | 0 | -21 | -100.0% |
| `definitive-state-assertion-gate` | 20 | 20 | 0 | -20 | -100.0% |
| `sensitive-write-router` | 12 | 11 | 0 | -11 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `state-assertion-grounding` | 186 | 30 | 37 | +7 | +23.3% |
| `terminal-state-evidence-gate` | 34 | 15 | 19 | +4 | +26.7% |
| `pressure-framing-guard` | 22 | 4 | 8 | +4 | +100.0% |
| `raw-gmail-send-guard` | 3 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
