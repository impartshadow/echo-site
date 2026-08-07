# Violation Decay Case Study

Generated: 2026-08-07T08:22:23.798566+00:00

## Claim
partial-evidence-flag cooled from 105 to 0 weekly hits; terminal-state-evidence-gate is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1341
- Distinct contracts in log: 66
- Distinct failure modes: 20
- Eligible contracts: 47
- Cooled contracts: 40
- Hotter contracts: 3

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `partial-evidence-flag` | 172 | 105 | 0 | -105 | -100.0% |
| `persistent-correction` | 104 | 68 | 0 | -68 | -100.0% |
| `scope-coverage-guard` | 43 | 43 | 0 | -43 | -100.0% |
| `verification-vocabulary-gate` | 89 | 53 | 15 | -38 | -71.7% |
| `completion-artifact` | 52 | 40 | 5 | -35 | -87.5% |
| `stale-state-assertion-guard` | 84 | 35 | 10 | -25 | -71.4% |
| `definitive-state-assertion-gate` | 20 | 20 | 0 | -20 | -100.0% |
| `factual-claim-verification` | 124 | 41 | 23 | -18 | -43.9% |
| `platform-action-precheck` | 106 | 18 | 2 | -16 | -88.9% |
| `self-verification` | 56 | 14 | 0 | -14 | -100.0% |
| `commit-hash-verification` | 28 | 15 | 2 | -13 | -86.7% |
| `sensitive-write-router` | 12 | 11 | 0 | -11 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `terminal-state-evidence-gate` | 36 | 15 | 20 | +5 | +33.3% |
| `state-assertion-grounding` | 178 | 28 | 31 | +3 | +10.7% |
| `pressure-framing-guard` | 21 | 4 | 6 | +2 | +50.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
