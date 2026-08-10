# Violation Decay Case Study

Generated: 2026-08-10T08:28:31.936572+00:00

## Claim
scope-coverage-guard cooled from 43 to 0 weekly hits; stale-state-assertion-guard is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1222
- Distinct contracts in log: 66
- Distinct failure modes: 21
- Eligible contracts: 42
- Cooled contracts: 33
- Hotter contracts: 4

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `scope-coverage-guard` | 43 | 43 | 0 | -43 | -100.0% |
| `partial-evidence-flag` | 76 | 31 | 0 | -31 | -100.0% |
| `platform-action-precheck` | 91 | 27 | 0 | -27 | -100.0% |
| `persistent-correction` | 42 | 21 | 0 | -21 | -100.0% |
| `definitive-state-assertion-gate` | 20 | 20 | 0 | -20 | -100.0% |
| `self-verification` | 49 | 19 | 0 | -19 | -100.0% |
| `verification-vocabulary-gate` | 118 | 53 | 35 | -18 | -34.0% |
| `loop-name-validation-guard` | 13 | 13 | 0 | -13 | -100.0% |
| `state-assertion-grounding` | 170 | 24 | 12 | -12 | -50.0% |
| `terminal-state-evidence-gate` | 39 | 15 | 5 | -10 | -66.7% |
| `sensitive-write-router` | 11 | 10 | 0 | -10 | -100.0% |
| `dangerous-path-guard` | 10 | 10 | 0 | -10 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `stale-state-assertion-guard` | 74 | 26 | 30 | +4 | +15.4% |
| `completion-artifact` | 15 | 3 | 6 | +3 | +100.0% |
| `factual-claim-verification` | 112 | 37 | 38 | +1 | +2.7% |
| `unbuilt-guarantee-guard` | 9 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
