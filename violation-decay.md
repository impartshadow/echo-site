# Violation Decay Case Study

Generated: 2026-07-17T08:14:55.590992+00:00

## Claim
patterned-stop cooled from 19 to 0 weekly hits; partial-evidence-flag is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1381
- Distinct contracts in log: 53
- Distinct failure modes: 22
- Eligible contracts: 43
- Cooled contracts: 30
- Hotter contracts: 11

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `patterned-stop` | 26 | 19 | 0 | -19 | -100.0% |
| `loop-name-validation-guard` | 42 | 21 | 6 | -15 | -71.4% |
| `behavioral-haiku-guard` | 50 | 14 | 3 | -11 | -78.6% |
| `commit-hash-verification` | 46 | 11 | 0 | -11 | -100.0% |
| `live-state-claim-guard` | 25 | 13 | 2 | -11 | -84.6% |
| `dox-guard` | 38 | 7 | 0 | -7 | -100.0% |
| `cl-stop_editing_github_inbound_check` | 8 | 7 | 0 | -7 | -100.0% |
| `cl-stop_editing_gmail_summary_py` | 8 | 7 | 0 | -7 | -100.0% |
| `concurrence-grounding` | 23 | 12 | 6 | -6 | -50.0% |
| `balar-clarification` | 18 | 6 | 0 | -6 | -100.0% |
| `cl-channel_shadow_hq_system_bot` | 6 | 6 | 0 | -6 | -100.0% |
| `cl-if_title_seems_relevant_can` | 6 | 6 | 0 | -6 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `partial-evidence-flag` | 226 | 21 | 55 | +34 | +161.9% |
| `completion-artifact` | 84 | 13 | 26 | +13 | +100.0% |
| `platform-action-precheck` | 95 | 13 | 25 | +12 | +92.3% |
| `state-assertion-grounding` | 104 | 11 | 22 | +11 | +100.0% |
| `factual-claim-verification` | 85 | 11 | 17 | +6 | +54.5% |
| `self-verification` | 75 | 14 | 19 | +5 | +35.7% |
| `stale-state-assertion-guard` | 61 | 5 | 9 | +4 | +80.0% |
| `dangerous-path-guard` | 17 | 6 | 10 | +4 | +66.7% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
