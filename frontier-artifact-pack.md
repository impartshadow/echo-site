# Frontier Artifact Pack

Generated: 2026-08-29T08:37:33.723566+00:00

## Thesis
The moat is no longer the model or the summary — it's the harness that stays in the loop long enough to verify its own actions, and most agent businesses will die because they ship outputs instead of receipts.

## Doctrine
Every loop action must close observe → act → verify: no artifact counts as shipped until a runtime receipt proves the world changed as intended, and unverified actions get retried or classified as blockers, never silently logged.

## Proof Artifact
A verify-gate module for the Shadow loop runner: after each loop's primary action, run a declared post-condition check (file exists, endpoint responds, metric moved), emit a receipt JSON {action, expected, observed, pass}, and auto-retry once on failure before flagging a blocker.

Next action: Create ~/.cache/shadow/loops/lib/verify_gate.py implementing check-receipt-retry (post_condition callable, receipt written to ~/.cache/shadow/receipts/{loop}_{ts}.json), then wire it into the highest-frequency existing loop runner as its exit step.

## Public Angle
Everyone demos agents acting; nobody demos agents checking whether the action worked. We made verification the exit criterion of every loop — here's what our receipts caught in week one.

## Buyer Offer
Sell 'verified automation' to small ops teams: a $99/mo Shadow-run watchdog that doesn't just execute their recurring task but delivers a signed receipt each run proving the outcome occurred — pitch to prospects already burned by silent cron/Zapier failures.

## Source Signals
- Agents Don't Paginate: First-Chunk Selection for LLM Tool Responses
- Prime Agent: A Self-Improving RLM Harness | Seth Karten Home Research Canonical page Agent Harnesses · Technical Report Prime Agent: A Self-Improving RLM Harnes
- Distributed Training using an Intelligent Network
- yuriak/DCS-Harness — An agent-native workspace for autonomous DCS mission direction
- Carer-Healthcare-AI/Hospilot — Open-source agentic AI operating layer for hospital operations — multi-agent orchestration over FHIR

## Scale Packets
- proof_artifact: promoted (ec88fe6afb96)
- public_wedge: promoted (9ece13962b49)
- buyer_experiment: promoted (4ffe732ec4fe)
- operator_doctrine: promoted (756c300b2bc7)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (ec88fe6afb96)
- public_wedge: queued_echo_draft (9ece13962b49)
- buyer_experiment: queued_buyer_experiment (4ffe732ec4fe)
- operator_doctrine: already_persisted (756c300b2bc7)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
