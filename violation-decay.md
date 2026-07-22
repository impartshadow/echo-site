# Violation Decay Case Study

Generated: 2026-07-22T08:18:41.995435+00:00

## Claim
dox-guard cooled from 28 to 0 weekly hits; platform-action-precheck is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1644
- Distinct contracts in log: 56
- Distinct failure modes: 22
- Eligible contracts: 45
- Cooled contracts: 32
- Hotter contracts: 12

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `dox-guard` | 31 | 28 | 0 | -28 | -100.0% |
| `completion-artifact` | 79 | 26 | 3 | -23 | -88.5% |
| `live-state-claim-guard` | 23 | 13 | 2 | -11 | -84.6% |
| `patterned-stop` | 13 | 11 | 0 | -11 | -100.0% |
| `persistent-correction` | 190 | 38 | 29 | -9 | -23.7% |
| `behavioral-haiku-guard` | 46 | 15 | 7 | -8 | -53.3% |
| `balar-clarification` | 15 | 8 | 0 | -8 | -100.0% |
| `cl-stop_editing_github_inbound_check` | 8 | 7 | 0 | -7 | -100.0% |
| `cl-stop_editing_gmail_summary_py` | 8 | 7 | 0 | -7 | -100.0% |
| `state-io-consolidation-guard` | 14 | 6 | 0 | -6 | -100.0% |
| `api-first-routing-guard` | 6 | 6 | 0 | -6 | -100.0% |
| `cl-channel_shadow_hq_system_bot` | 5 | 5 | 0 | -5 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `platform-action-precheck` | 128 | 16 | 63 | +47 | +293.8% |
| `partial-evidence-flag` | 259 | 31 | 63 | +32 | +103.2% |
| `state-assertion-grounding` | 156 | 39 | 68 | +29 | +74.4% |
| `factual-claim-verification` | 112 | 13 | 37 | +24 | +184.6% |
| `self-verification` | 96 | 13 | 34 | +21 | +161.5% |
| `stale-state-assertion-guard` | 82 | 8 | 28 | +20 | +250.0% |
| `dangerous-path-guard` | 11 | 1 | 10 | +9 | +900.0% |
| `concurrence-grounding` | 37 | 12 | 16 | +4 | +33.3% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
