# Violation Decay Case Study

Generated: 2026-09-23T08:54:43.709480+00:00

## Claim
fleet-state-claim-grounding-gate cooled from 13 to 0 weekly hits; terminal-state-evidence-gate is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 356
- Distinct contracts in log: 60
- Distinct failure modes: 18
- Eligible contracts: 31
- Cooled contracts: 19
- Hotter contracts: 9

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `fleet-state-claim-grounding-gate` | 14 | 13 | 0 | -13 | -100.0% |
| `verification-vocabulary-gate` | 18 | 11 | 0 | -11 | -100.0% |
| `stale-state-assertion-guard` | 34 | 15 | 6 | -9 | -60.0% |
| `personal-help-provenance-carveout` | 9 | 9 | 0 | -9 | -100.0% |
| `factual-claim-verification` | 35 | 12 | 7 | -5 | -41.7% |
| `dox-guard` | 13 | 9 | 4 | -5 | -55.6% |
| `thin-context-brief-gate` | 7 | 6 | 1 | -5 | -83.3% |
| `state-assertion-grounding` | 31 | 11 | 7 | -4 | -36.4% |
| `vendor-availability-external-fetch-required` | 7 | 5 | 1 | -4 | -80.0% |
| `privacy-exposure-taxonomy` | 22 | 7 | 4 | -3 | -42.9% |
| `attribute-correction-verification-guard` | 2 | 2 | 0 | -2 | -100.0% |
| `canonical-source-guard` | 2 | 2 | 0 | -2 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `terminal-state-evidence-gate` | 12 | 1 | 5 | +4 | +400.0% |
| `cleanup-claim-mechanism-gate` | 9 | 2 | 4 | +2 | +100.0% |
| `live-state-claim-guard` | 4 | 1 | 3 | +2 | +200.0% |
| `pressure-framing-guard` | 10 | 4 | 5 | +1 | +25.0% |
| `completion-artifact` | 9 | 3 | 4 | +1 | +33.3% |
| `unbuilt-guarantee-guard` | 8 | 2 | 3 | +1 | +50.0% |
| `commit-hash-verification` | 3 | 1 | 2 | +1 | +100.0% |
| `manual-handoff-guard` | 3 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
