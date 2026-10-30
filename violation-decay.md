# Violation Decay Case Study

Generated: 2026-10-30T08:24:43.456345+00:00

## Claim
chat-remark-validation-guard cooled from 4 to 0 weekly hits; factual-claim-verification is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 164
- Distinct contracts in log: 61
- Distinct failure modes: 24
- Eligible contracts: 37
- Cooled contracts: 28
- Hotter contracts: 5

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `chat-remark-validation-guard` | 5 | 4 | 0 | -4 | -100.0% |
| `state-assertion-grounding` | 5 | 4 | 0 | -4 | -100.0% |
| `pressure-framing-guard` | 4 | 3 | 0 | -3 | -100.0% |
| `cleanup-claim-mechanism-gate` | 3 | 2 | 0 | -2 | -100.0% |
| `dox-guard` | 2 | 2 | 0 | -2 | -100.0% |
| `stale-state-assertion-guard` | 11 | 2 | 1 | -1 | -50.0% |
| `verify-before-report` | 6 | 1 | 0 | -1 | -100.0% |
| `completion-artifact` | 5 | 3 | 2 | -1 | -33.3% |
| `capitulation-flip-gate` | 4 | 2 | 1 | -1 | -50.0% |
| `terminal-state-evidence-gate` | 3 | 1 | 0 | -1 | -100.0% |
| `cl-channel_shadow_hq_system_bot` | 2 | 1 | 0 | -1 | -100.0% |
| `cl-don_t_just_blindly_take` | 2 | 1 | 0 | -1 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `factual-claim-verification` | 11 | 1 | 5 | +4 | +400.0% |
| `live-state-claim-guard` | 8 | 2 | 5 | +3 | +150.0% |
| `term-lookup-before-ask-gate` | 5 | 1 | 3 | +2 | +200.0% |
| `runtime-activation-claim-gate` | 5 | 2 | 3 | +1 | +50.0% |
| `third-party-outbound-authorization-gate` | 4 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
