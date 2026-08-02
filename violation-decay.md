# Violation Decay Case Study

Generated: 2026-08-02T08:14:58.605997+00:00

## Claim
partial-evidence-flag cooled from 96 to 0 weekly hits; state-assertion-grounding is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1449
- Distinct contracts in log: 66
- Distinct failure modes: 22
- Eligible contracts: 46
- Cooled contracts: 41
- Hotter contracts: 3

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `partial-evidence-flag` | 211 | 96 | 0 | -96 | -100.0% |
| `persistent-correction` | 139 | 84 | 0 | -84 | -100.0% |
| `scope-coverage-guard` | 43 | 43 | 0 | -43 | -100.0% |
| `platform-action-precheck` | 128 | 36 | 2 | -34 | -94.4% |
| `stale-state-assertion-guard` | 81 | 40 | 6 | -34 | -85.0% |
| `verification-vocabulary-gate` | 76 | 53 | 23 | -30 | -56.6% |
| `factual-claim-verification` | 115 | 40 | 12 | -28 | -70.0% |
| `self-verification` | 73 | 23 | 0 | -23 | -100.0% |
| `commit-hash-verification` | 43 | 32 | 10 | -22 | -68.8% |
| `definitive-state-assertion-gate` | 20 | 20 | 0 | -20 | -100.0% |
| `completion-artifact` | 54 | 21 | 4 | -17 | -81.0% |
| `behavioral-haiku-guard` | 21 | 12 | 0 | -12 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `state-assertion-grounding` | 186 | 24 | 48 | +24 | +100.0% |
| `terminal-state-evidence-gate` | 34 | 15 | 19 | +4 | +26.7% |
| `unbuilt-guarantee-guard` | 7 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
