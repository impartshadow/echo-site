# Violation Decay Case Study

Generated: 2026-10-05T08:02:21.605055+00:00

## Claim
personal-token-send-guard cooled from 15 to 0 weekly hits; pressure-framing-guard is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 252
- Distinct contracts in log: 61
- Distinct failure modes: 22
- Eligible contracts: 49
- Cooled contracts: 47
- Hotter contracts: 1

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `personal-token-send-guard` | 15 | 15 | 0 | -15 | -100.0% |
| `raw-gmail-send-guard` | 12 | 12 | 0 | -12 | -100.0% |
| `dox-guard` | 14 | 9 | 1 | -8 | -88.9% |
| `factual-claim-verification` | 15 | 7 | 1 | -6 | -85.7% |
| `thin-context-brief-gate` | 8 | 6 | 0 | -6 | -100.0% |
| `stale-state-assertion-guard` | 15 | 6 | 1 | -5 | -83.3% |
| `terminal-state-evidence-gate` | 12 | 6 | 1 | -5 | -83.3% |
| `cleanup-claim-mechanism-gate` | 8 | 6 | 1 | -5 | -83.3% |
| `continuation-ambiguity-guard` | 5 | 5 | 0 | -5 | -100.0% |
| `state-assertion-grounding` | 17 | 6 | 2 | -4 | -66.7% |
| `vendor-availability-external-fetch-required` | 8 | 5 | 1 | -4 | -80.0% |
| `ownership-ask-execution-gate` | 4 | 4 | 0 | -4 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `pressure-framing-guard` | 9 | 1 | 3 | +2 | +200.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
