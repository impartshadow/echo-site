# Violation Decay Case Study

Generated: 2026-07-23T08:32:02.514616+00:00

## Claim
dox-guard cooled from 28 to 0 weekly hits; platform-action-precheck is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1679
- Distinct contracts in log: 59
- Distinct failure modes: 22
- Eligible contracts: 46
- Cooled contracts: 35
- Hotter contracts: 11

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `dox-guard` | 31 | 28 | 0 | -28 | -100.0% |
| `completion-artifact` | 79 | 26 | 3 | -23 | -88.5% |
| `persistent-correction` | 189 | 39 | 25 | -14 | -35.9% |
| `live-state-claim-guard` | 21 | 11 | 1 | -10 | -90.9% |
| `state-io-consolidation-guard` | 13 | 9 | 0 | -9 | -100.0% |
| `behavioral-haiku-guard` | 46 | 15 | 7 | -8 | -53.3% |
| `patterned-stop` | 9 | 8 | 0 | -8 | -100.0% |
| `balar-clarification` | 14 | 7 | 0 | -7 | -100.0% |
| `cl-stop_editing_github_inbound_check` | 8 | 7 | 0 | -7 | -100.0% |
| `cl-stop_editing_gmail_summary_py` | 8 | 7 | 0 | -7 | -100.0% |
| `api-first-routing-guard` | 6 | 6 | 0 | -6 | -100.0% |
| `cl-channel_shadow_hq_system_bot` | 5 | 5 | 0 | -5 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `platform-action-precheck` | 145 | 17 | 70 | +53 | +311.8% |
| `state-assertion-grounding` | 167 | 39 | 77 | +38 | +97.4% |
| `factual-claim-verification` | 118 | 15 | 45 | +30 | +200.0% |
| `self-verification` | 93 | 13 | 32 | +19 | +146.2% |
| `partial-evidence-flag` | 258 | 40 | 58 | +18 | +45.0% |
| `stale-state-assertion-guard` | 82 | 15 | 26 | +11 | +73.3% |
| `concurrence-grounding` | 38 | 12 | 16 | +4 | +33.3% |
| `pressure-framing-guard` | 17 | 3 | 7 | +4 | +133.3% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
