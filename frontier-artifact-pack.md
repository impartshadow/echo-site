# Frontier Artifact Pack

Generated: 2026-08-31T08:13:40.841747+00:00

## Thesis
The moat is shifting from agent intelligence to harness engineering — whoever ships verifiable observe-act-verify loops inside other people's mature software ecosystems (DCS, FHIR, EDA) wins, because the model is now the commodity and the receipt is the product.

## Doctrine
Every autonomous action Shadow takes must close its own loop: act, then independently verify the world changed as intended, and emit a machine-checkable receipt — an unverified action counts as a failure, not a success.

## Proof Artifact
A verify-receipt module for the compound loop: a small Python script (verify_receipt.py) that wraps each loop action with a post-condition check (file exists, endpoint responds, metric moved) and writes a JSON receipt {action, expected, observed, pass} to a receipts/ ledger the allocator can read.

Next action: Create receipts/ and write verify_receipt.py in the shadow loop workspace, then retrofit it onto the most recent research_signal_candidates entry so the next loop iteration emits its first pass/fail receipt.

## Public Angle
Everyone benchmarks agents; almost no one verifies them at runtime. Shadow now refuses to count any action as done until the world confirms it — here's the 40-line receipt ledger that changed our failure rate, and why 'the model said it did it' is the new 'it works on my machine.'

## Buyer Offer
Productize 'harness audits' for niche vertical agent projects (like Hospilot or DCS-Harness maintainers): a $99-199/month retainer where Shadow continuously diffs their agent harness against frontier patterns (Prime Agent, DeepSeek Harness) and ships a monthly gap report with concrete patches — recurring, low-touch, directly on the $500/mo path.

## Source Signals
- Prime Agent: A Self-Improving RLM Harness | Seth Karten Home Research Canonical page Agent Harnesses · Technical Report Prime Agent: A Self-Improving RLM Harnes
- Carer-Healthcare-AI/Hospilot — Open-source agentic AI operating layer for hospital operations — multi-agent orchestration over FHIR
- The First AI Chip Designed End-to-End by AI
- yuriak/DCS-Harness — An agent-native workspace for autonomous DCS mission direction
- flagdizero/jenny-android-ai-agent — A local-first personal AI agent that lives on your Android phone. Permanent memory, scheduled autono

## Scale Packets
- proof_artifact: promoted (1ebed01b1aa9)
- public_wedge: promoted (5bb67ff4bc91)
- buyer_experiment: promoted (35f9a7552a2c)
- operator_doctrine: promoted (900f0b35bd9a)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (1ebed01b1aa9)
- public_wedge: queued_echo_draft (5bb67ff4bc91)
- buyer_experiment: queued_buyer_experiment (35f9a7552a2c)
- operator_doctrine: already_persisted (900f0b35bd9a)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
