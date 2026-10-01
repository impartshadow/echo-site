# Violation Decay Case Study

Generated: 2026-10-01T09:24:08.535171+00:00

## Claim
personal-token-send-guard cooled from 15 to 0 weekly hits; capitulation-flip-gate is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 290
- Distinct contracts in log: 63
- Distinct failure modes: 20
- Eligible contracts: 36
- Cooled contracts: 34
- Hotter contracts: 1

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `personal-token-send-guard` | 15 | 15 | 0 | -15 | -100.0% |
| `raw-gmail-send-guard` | 12 | 12 | 0 | -12 | -100.0% |
| `privacy-exposure-taxonomy` | 15 | 11 | 0 | -11 | -100.0% |
| `personal-help-provenance-carveout` | 9 | 9 | 0 | -9 | -100.0% |
| `dox-guard` | 14 | 9 | 1 | -8 | -88.9% |
| `state-assertion-grounding` | 24 | 11 | 4 | -7 | -63.6% |
| `factual-claim-verification` | 22 | 8 | 1 | -7 | -87.5% |
| `verification-vocabulary-gate` | 7 | 7 | 0 | -7 | -100.0% |
| `stale-state-assertion-guard` | 21 | 8 | 2 | -6 | -75.0% |
| `terminal-state-evidence-gate` | 11 | 6 | 0 | -6 | -100.0% |
| `cleanup-claim-mechanism-gate` | 7 | 6 | 0 | -6 | -100.0% |
| `thin-context-brief-gate` | 8 | 6 | 1 | -5 | -83.3% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `capitulation-flip-gate` | 4 | 1 | 3 | +2 | +200.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
