# Violation Decay Case Study

Generated: 2026-09-24T07:57:46.374439+00:00

## Claim
personal-token-send-guard cooled from 15 to 0 weekly hits; terminal-state-evidence-gate is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 332
- Distinct contracts in log: 59
- Distinct failure modes: 18
- Eligible contracts: 31
- Cooled contracts: 20
- Hotter contracts: 9

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `personal-token-send-guard` | 15 | 15 | 0 | -15 | -100.0% |
| `raw-gmail-send-guard` | 12 | 12 | 0 | -12 | -100.0% |
| `verification-vocabulary-gate` | 17 | 11 | 0 | -11 | -100.0% |
| `stale-state-assertion-guard` | 31 | 15 | 5 | -10 | -66.7% |
| `personal-help-provenance-carveout` | 9 | 9 | 0 | -9 | -100.0% |
| `dox-guard` | 13 | 9 | 2 | -7 | -77.8% |
| `state-assertion-grounding` | 26 | 11 | 5 | -6 | -54.5% |
| `fleet-state-claim-grounding-gate` | 7 | 6 | 0 | -6 | -100.0% |
| `factual-claim-verification` | 29 | 11 | 7 | -4 | -36.4% |
| `privacy-exposure-taxonomy` | 21 | 6 | 2 | -4 | -66.7% |
| `thin-context-brief-gate` | 8 | 6 | 2 | -4 | -66.7% |
| `vendor-availability-external-fetch-required` | 7 | 5 | 1 | -4 | -80.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `terminal-state-evidence-gate` | 12 | 1 | 5 | +4 | +400.0% |
| `cleanup-claim-mechanism-gate` | 8 | 1 | 4 | +3 | +300.0% |
| `unbuilt-guarantee-guard` | 7 | 1 | 3 | +2 | +200.0% |
| `live-state-claim-guard` | 4 | 1 | 3 | +2 | +200.0% |
| `pressure-framing-guard` | 10 | 4 | 5 | +1 | +25.0% |
| `completion-artifact` | 9 | 3 | 4 | +1 | +33.3% |
| `commit-hash-verification` | 3 | 1 | 2 | +1 | +100.0% |
| `manual-handoff-guard` | 3 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
