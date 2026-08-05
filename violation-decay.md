# Violation Decay Case Study

Generated: 2026-08-05T08:29:05.788234+00:00

## Claim
partial-evidence-flag cooled from 105 to 0 weekly hits; state-assertion-grounding is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1332
- Distinct contracts in log: 65
- Distinct failure modes: 20
- Eligible contracts: 46
- Cooled contracts: 38
- Hotter contracts: 4

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `partial-evidence-flag` | 176 | 105 | 0 | -105 | -100.0% |
| `persistent-correction` | 115 | 75 | 0 | -75 | -100.0% |
| `scope-coverage-guard` | 43 | 43 | 0 | -43 | -100.0% |
| `completion-artifact` | 50 | 40 | 3 | -37 | -92.5% |
| `verification-vocabulary-gate` | 83 | 53 | 17 | -36 | -67.9% |
| `stale-state-assertion-guard` | 80 | 36 | 8 | -28 | -77.8% |
| `factual-claim-verification` | 122 | 43 | 21 | -22 | -51.2% |
| `platform-action-precheck` | 112 | 23 | 2 | -21 | -91.3% |
| `commit-hash-verification` | 34 | 23 | 3 | -20 | -87.0% |
| `definitive-state-assertion-gate` | 20 | 20 | 0 | -20 | -100.0% |
| `self-verification` | 60 | 18 | 0 | -18 | -100.0% |
| `sensitive-write-router` | 12 | 11 | 0 | -11 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `state-assertion-grounding` | 176 | 25 | 36 | +11 | +44.0% |
| `terminal-state-evidence-gate` | 35 | 15 | 20 | +5 | +33.3% |
| `pressure-framing-guard` | 20 | 4 | 8 | +4 | +100.0% |
| `crypto-price-claim-guard` | 3 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
