# Violation Decay Case Study

Generated: 2026-07-13T08:44:14.536809+00:00

## Claim
patterned-stop cooled from 30 to 0 weekly hits; partial-evidence-flag is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1497
- Distinct contracts in log: 52
- Distinct failure modes: 21
- Eligible contracts: 45
- Cooled contracts: 35
- Hotter contracts: 8

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `patterned-stop` | 44 | 30 | 0 | -30 | -100.0% |
| `dox-guard` | 60 | 27 | 1 | -26 | -96.3% |
| `loop-name-validation-guard` | 36 | 21 | 2 | -19 | -90.5% |
| `dangerous-path-guard` | 15 | 12 | 1 | -11 | -91.7% |
| `concurrence-grounding` | 20 | 12 | 4 | -8 | -66.7% |
| `identity-hash-guard` | 7 | 7 | 0 | -7 | -100.0% |
| `commit-hash-verification` | 61 | 21 | 15 | -6 | -28.6% |
| `behavioral-haiku-guard` | 52 | 13 | 7 | -6 | -46.2% |
| `balar-clarification` | 19 | 6 | 0 | -6 | -100.0% |
| `cl-stop_editing_github_inbound_check` | 8 | 7 | 1 | -6 | -85.7% |
| `cl-stop_editing_gmail_summary_py` | 8 | 7 | 1 | -6 | -85.7% |
| `crypto-price-claim-guard` | 6 | 5 | 0 | -5 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `partial-evidence-flag` | 250 | 51 | 105 | +54 | +105.9% |
| `stale-state-assertion-guard` | 58 | 5 | 35 | +30 | +600.0% |
| `factual-claim-verification` | 85 | 13 | 41 | +28 | +215.4% |
| `state-assertion-grounding` | 96 | 13 | 25 | +12 | +92.3% |
| `completion-artifact` | 110 | 29 | 39 | +10 | +34.5% |
| `platform-action-precheck` | 80 | 13 | 18 | +5 | +38.5% |
| `continuation-ambiguity-guard` | 8 | 2 | 4 | +2 | +100.0% |
| `persistent-correction` | 229 | 67 | 68 | +1 | +1.5% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
