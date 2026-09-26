# Violation Decay Case Study

Generated: 2026-09-26T08:38:29.402456+00:00

## Claim
verification-vocabulary-gate cooled from 16 to 0 weekly hits; terminal-state-evidence-gate is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 326
- Distinct contracts in log: 59
- Distinct failure modes: 18
- Eligible contracts: 32
- Cooled contracts: 20
- Hotter contracts: 8

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `verification-vocabulary-gate` | 16 | 16 | 0 | -16 | -100.0% |
| `personal-token-send-guard` | 15 | 15 | 0 | -15 | -100.0% |
| `raw-gmail-send-guard` | 12 | 12 | 0 | -12 | -100.0% |
| `privacy-exposure-taxonomy` | 20 | 13 | 2 | -11 | -84.6% |
| `personal-help-provenance-carveout` | 9 | 9 | 0 | -9 | -100.0% |
| `dox-guard` | 13 | 9 | 1 | -8 | -88.9% |
| `factual-claim-verification` | 28 | 14 | 7 | -7 | -50.0% |
| `stale-state-assertion-guard` | 28 | 12 | 5 | -7 | -58.3% |
| `state-assertion-grounding` | 28 | 11 | 5 | -6 | -54.5% |
| `fleet-state-claim-grounding-gate` | 6 | 6 | 0 | -6 | -100.0% |
| `thin-context-brief-gate` | 8 | 6 | 2 | -4 | -66.7% |
| `vendor-availability-external-fetch-required` | 7 | 5 | 1 | -4 | -80.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `terminal-state-evidence-gate` | 12 | 1 | 5 | +4 | +400.0% |
| `cleanup-claim-mechanism-gate` | 8 | 1 | 4 | +3 | +300.0% |
| `completion-artifact` | 8 | 2 | 3 | +1 | +50.0% |
| `unbuilt-guarantee-guard` | 7 | 1 | 2 | +1 | +100.0% |
| `live-state-claim-guard` | 4 | 1 | 2 | +1 | +100.0% |
| `runtime-activation-claim-gate` | 4 | 1 | 2 | +1 | +100.0% |
| `commit-hash-verification` | 3 | 1 | 2 | +1 | +100.0% |
| `manual-handoff-guard` | 3 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
