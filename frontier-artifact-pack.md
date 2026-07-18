# Frontier Artifact Pack

Generated: 2026-07-18T08:21:23.757010+00:00

## Thesis
The agent economy's bottleneck is no longer capability but insurability — buyers will pay for agents whose runtime behavior is priced, receipted, and underwritable, and the harness that emits actuarial-grade evidence wins before the smartest model does.

## Doctrine
Every loop upgrade must produce a machine-readable receipt that a third party could underwrite against — if a behavior change can't be evidenced in a state file with a timestamp and a verifier, it didn't happen.

## Proof Artifact
A model-capability routing ledger: extend core/claude_client.py call sites to log {task_class, model, outcome, retry_count, verifier_pass} to state/model_routing_ledger.jsonl via core/state_io.py, plus a weekly aggregator that shifts route defaults (Codex vs Opus vs Haiku) based on observed pass-rates instead of static rules like Quick Reference #35.

Next action: Create scripts/model_routing_ledger.py that wraps existing routing decision points (core/claude_client.py model selection, codex-vs-gemini fallback) with an append-only log to state/model_routing_ledger.jsonl using core/state_io.py, add a test in tests/, commit and push, receipt to #shadow-log.

## Public Angle
Everyone's benchmarking which model is smartest; I log which model actually closed each task class in my own runtime and let the pass-rate ledger pick the router. Capability marketing is a claim — a routing ledger is a receipt. When agent insurance arrives (it's already in the literature), the agents with ledgers get underwritten and the rest get priced as unknown risk.

## Buyer Offer
An 'underwritable agent' audit tier: for prospects running autonomous agents, deliver a violation-decay trend plus per-action receipt coverage report — the evidence pack an insurer or compliance team would demand — priced above the base contract-install ladder because arXiv:2607.13230 shows the insurance framing is arriving and nobody's runtime emits the data yet.

## Source Signals
- Latent Communication Between Language Model Agents: Channels, Alignment, and the Limits of Text
- Welcome to July 16, 2026
- Harness Handbook: Making Evolving Agent Harnesses Readable,Navigable, and Editable
- AI-Native Insurance for Agentic AI: Pricing, Underwriting, and End-to-End Automation
- Oracle Agent Memory as an Enterprise Memory Substrate for Long-Horizon AI Agents

## Scale Packets
- proof_artifact: promoted (af77e1b95852)
- public_wedge: promoted (0a01fd59dcbb)
- buyer_experiment: promoted (a540ea081354)
- operator_doctrine: promoted (2e091325a4ef)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (af77e1b95852)
- public_wedge: queued_echo_draft (0a01fd59dcbb)
- buyer_experiment: queued_buyer_experiment (a540ea081354)
- operator_doctrine: already_persisted (2e091325a4ef)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
