# Violation Decay Case Study

Generated: 2026-08-13T08:23:31.475046+00:00

## Claim
partial-evidence-flag cooled from 50 to 0 weekly hits; stale-state-assertion-guard is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1270
- Distinct contracts in log: 68
- Distinct failure modes: 21
- Eligible contracts: 44
- Cooled contracts: 37
- Hotter contracts: 3

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `partial-evidence-flag` | 73 | 50 | 0 | -50 | -100.0% |
| `platform-action-precheck` | 89 | 49 | 0 | -49 | -100.0% |
| `scope-coverage-guard` | 43 | 43 | 0 | -43 | -100.0% |
| `self-verification` | 45 | 29 | 0 | -29 | -100.0% |
| `persistent-correction` | 41 | 28 | 0 | -28 | -100.0% |
| `definitive-state-assertion-gate` | 20 | 20 | 0 | -20 | -100.0% |
| `state-assertion-grounding` | 175 | 38 | 20 | -18 | -47.4% |
| `loop-name-validation-guard` | 13 | 13 | 0 | -13 | -100.0% |
| `terminal-state-evidence-gate` | 39 | 15 | 4 | -11 | -73.3% |
| `verification-vocabulary-gate` | 127 | 53 | 43 | -10 | -18.9% |
| `sensitive-write-router` | 11 | 10 | 0 | -10 | -100.0% |
| `dangerous-path-guard` | 10 | 10 | 0 | -10 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `stale-state-assertion-guard` | 81 | 26 | 37 | +11 | +42.3% |
| `factual-claim-verification` | 126 | 37 | 47 | +10 | +27.0% |
| `unbuilt-guarantee-guard` | 10 | 1 | 3 | +2 | +200.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
