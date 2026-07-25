# Violation Decay Case Study

Generated: 2026-07-25T08:05:33.749372+00:00

## Claim
dox-guard cooled from 28 to 0 weekly hits; platform-action-precheck is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1637
- Distinct contracts in log: 57
- Distinct failure modes: 21
- Eligible contracts: 45
- Cooled contracts: 34
- Hotter contracts: 9

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `dox-guard` | 31 | 28 | 0 | -28 | -100.0% |
| `completion-artifact` | 74 | 24 | 2 | -22 | -91.7% |
| `persistent-correction` | 178 | 39 | 18 | -21 | -53.8% |
| `behavioral-haiku-guard` | 43 | 22 | 5 | -17 | -77.3% |
| `sensitive-write-router` | 11 | 11 | 0 | -11 | -100.0% |
| `state-io-consolidation-guard` | 13 | 9 | 0 | -9 | -100.0% |
| `balar-clarification` | 11 | 9 | 0 | -9 | -100.0% |
| `cl-stop_editing_github_inbound_check` | 8 | 7 | 0 | -7 | -100.0% |
| `cl-stop_editing_gmail_summary_py` | 8 | 7 | 0 | -7 | -100.0% |
| `patterned-stop` | 7 | 7 | 0 | -7 | -100.0% |
| `api-first-routing-guard` | 6 | 6 | 0 | -6 | -100.0% |
| `personal-token-send-guard` | 5 | 5 | 0 | -5 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `platform-action-precheck` | 146 | 20 | 58 | +38 | +190.0% |
| `state-assertion-grounding` | 176 | 43 | 77 | +34 | +79.1% |
| `factual-claim-verification` | 118 | 15 | 44 | +29 | +193.3% |
| `stale-state-assertion-guard` | 86 | 15 | 25 | +10 | +66.7% |
| `concurrence-grounding` | 39 | 12 | 16 | +4 | +33.3% |
| `self-verification` | 91 | 22 | 25 | +3 | +13.6% |
| `pressure-framing-guard` | 16 | 3 | 6 | +3 | +100.0% |
| `manual-handoff-guard` | 6 | 2 | 4 | +2 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
