# Violation Decay Case Study

Generated: 2026-08-04T08:13:58.379324+00:00

## Claim
partial-evidence-flag cooled from 114 to 0 weekly hits; state-assertion-grounding is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1375
- Distinct contracts in log: 64
- Distinct failure modes: 20
- Eligible contracts: 45
- Cooled contracts: 39
- Hotter contracts: 4

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `partial-evidence-flag` | 187 | 114 | 0 | -114 | -100.0% |
| `persistent-correction` | 121 | 80 | 0 | -80 | -100.0% |
| `scope-coverage-guard` | 43 | 43 | 0 | -43 | -100.0% |
| `completion-artifact` | 50 | 41 | 2 | -39 | -95.1% |
| `verification-vocabulary-gate` | 83 | 53 | 18 | -35 | -66.0% |
| `factual-claim-verification` | 122 | 47 | 17 | -30 | -63.8% |
| `stale-state-assertion-guard` | 80 | 36 | 8 | -28 | -77.8% |
| `platform-action-precheck` | 116 | 27 | 2 | -25 | -92.6% |
| `self-verification` | 68 | 23 | 0 | -23 | -100.0% |
| `definitive-state-assertion-gate` | 20 | 20 | 0 | -20 | -100.0% |
| `commit-hash-verification` | 37 | 26 | 8 | -18 | -69.2% |
| `sensitive-write-router` | 12 | 11 | 0 | -11 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `state-assertion-grounding` | 180 | 25 | 36 | +11 | +44.0% |
| `terminal-state-evidence-gate` | 34 | 15 | 19 | +4 | +26.7% |
| `pressure-framing-guard` | 22 | 4 | 8 | +4 | +100.0% |
| `raw-gmail-send-guard` | 3 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
