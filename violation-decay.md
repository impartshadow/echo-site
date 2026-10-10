# Violation Decay Case Study

Generated: 2026-10-10T09:05:34.087578+00:00

## Claim
personal-token-send-guard cooled from 15 to 0 weekly hits; runtime-activation-claim-gate is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 222
- Distinct contracts in log: 62
- Distinct failure modes: 22
- Eligible contracts: 48
- Cooled contracts: 46
- Hotter contracts: 1

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `personal-token-send-guard` | 15 | 15 | 0 | -15 | -100.0% |
| `raw-gmail-send-guard` | 12 | 12 | 0 | -12 | -100.0% |
| `state-assertion-grounding` | 11 | 7 | 0 | -7 | -100.0% |
| `factual-claim-verification` | 14 | 6 | 0 | -6 | -100.0% |
| `dox-guard` | 8 | 6 | 1 | -5 | -83.3% |
| `continuation-ambiguity-guard` | 5 | 5 | 0 | -5 | -100.0% |
| `stale-state-assertion-guard` | 12 | 5 | 1 | -4 | -80.0% |
| `cleanup-claim-mechanism-gate` | 9 | 6 | 2 | -4 | -66.7% |
| `pressure-framing-guard` | 8 | 5 | 1 | -4 | -80.0% |
| `terminal-state-evidence-gate` | 6 | 5 | 1 | -4 | -80.0% |
| `vendor-availability-external-fetch-required` | 6 | 4 | 0 | -4 | -100.0% |
| `ownership-ask-execution-gate` | 4 | 4 | 0 | -4 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `runtime-activation-claim-gate` | 6 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
