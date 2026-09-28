# Violation Decay Case Study

Generated: 2026-09-28T07:55:46.212606+00:00

## Claim
personal-token-send-guard cooled from 15 to 0 weekly hits.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 307
- Distinct contracts in log: 61
- Distinct failure modes: 19
- Eligible contracts: 36
- Cooled contracts: 31
- Hotter contracts: 0

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `personal-token-send-guard` | 15 | 15 | 0 | -15 | -100.0% |
| `verification-vocabulary-gate` | 15 | 15 | 0 | -15 | -100.0% |
| `raw-gmail-send-guard` | 12 | 12 | 0 | -12 | -100.0% |
| `privacy-exposure-taxonomy` | 16 | 11 | 1 | -10 | -90.9% |
| `dox-guard` | 13 | 9 | 0 | -9 | -100.0% |
| `personal-help-provenance-carveout` | 9 | 9 | 0 | -9 | -100.0% |
| `state-assertion-grounding` | 27 | 11 | 3 | -8 | -72.7% |
| `stale-state-assertion-guard` | 24 | 10 | 2 | -8 | -80.0% |
| `factual-claim-verification` | 25 | 10 | 3 | -7 | -70.0% |
| `thin-context-brief-gate` | 8 | 6 | 1 | -5 | -83.3% |
| `cleanup-claim-mechanism-gate` | 7 | 6 | 1 | -5 | -83.3% |
| `vendor-availability-external-fetch-required` | 7 | 5 | 1 | -4 | -80.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| n/a | 0 | 0 | 0 | 0 | n/a |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
