# Violation Decay Case Study

Generated: 2026-10-03T08:33:21.975940+00:00

## Claim
personal-token-send-guard cooled from 15 to 0 weekly hits; pressure-framing-guard is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 270
- Distinct contracts in log: 64
- Distinct failure modes: 22
- Eligible contracts: 49
- Cooled contracts: 47
- Hotter contracts: 2

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `personal-token-send-guard` | 15 | 15 | 0 | -15 | -100.0% |
| `raw-gmail-send-guard` | 12 | 12 | 0 | -12 | -100.0% |
| `privacy-exposure-taxonomy` | 15 | 11 | 0 | -11 | -100.0% |
| `dox-guard` | 14 | 9 | 1 | -8 | -88.9% |
| `state-assertion-grounding` | 19 | 8 | 2 | -6 | -75.0% |
| `factual-claim-verification` | 15 | 7 | 1 | -6 | -85.7% |
| `terminal-state-evidence-gate` | 11 | 6 | 0 | -6 | -100.0% |
| `thin-context-brief-gate` | 8 | 6 | 0 | -6 | -100.0% |
| `cleanup-claim-mechanism-gate` | 7 | 6 | 0 | -6 | -100.0% |
| `stale-state-assertion-guard` | 17 | 6 | 1 | -5 | -83.3% |
| `continuation-ambiguity-guard` | 5 | 5 | 0 | -5 | -100.0% |
| `vendor-availability-external-fetch-required` | 8 | 5 | 1 | -4 | -80.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `pressure-framing-guard` | 9 | 1 | 3 | +2 | +200.0% |
| `capitulation-flip-gate` | 5 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
