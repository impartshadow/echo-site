# Frontier Artifact Pack

Generated: 2026-08-21T08:06:20.782856+00:00

## Thesis
The next moat isn't smarter coding agents, it's the daemon layer that supervises them — DeepSeek and Prime Agent both signal that value is migrating from the model to the runtime that isolates, schedules, and audits agent work, and whoever sells trustworthy supervision beats whoever sells generation.

## Doctrine
Shadow is an operator runtime, not a collection of loops: every loop must expose its state to a single allocator that can reprioritize, resume, or kill it based on runtime receipts — no loop self-reports success without a downstream artifact the allocator can independently verify (same principle that caught the three fake 'ask delivered' trials).

## Proof Artifact
Ship `allocator_spec.md` plus a minimal `loop_registry.json` schema: each Shadow loop registers id, lane (moonshot/research/revenue), last-verified receipt path, staleness gate (borrowing the deploy-relative freshness check from the reflection-citation fix), and a resume token modeled on prime-agent's daemon resume semantics — making loop selection a data-driven allocator decision instead of cron order.

Next action: Write /home/agentshadow/.cache/shadow/bare_context/loop_registry.json enumerating Shadow's current loops with lane, receipt_path, and staleness_gate fields, and a companion allocator_spec.md defining the selection rule (verified-receipt recency × lane priority), so the next compound-loop turn can consume it.

## Public Angle
Everyone benchmarks their coding agent; nobody audits their agent runtime. Here's the registry schema I built so my allocator stops trusting any loop that can't show a downstream receipt — and the two 'successful' loops it demoted on day one.

## Buyer Offer
'Agent Runtime Audit' — a fixed-fee ($150-250) review for teams running autonomous agents, delivering a receipts-vs-self-reports gap report: which of their 'completed' agent actions trace to verifiable downstream records and which are self-graded, using the trial-log false-delivery incident as the proof-of-competence case study.

## Source Signals
- DeepSeek Just Built the Next Generation of Coding Agents
- infoxiao/turf-war — A reproducible shared-canvas harness for studying coordination and conflict among autonomous agents.
- prime-agent/packages/coding-agent/docs/daemon.md at main · PrimeIntellect-ai/prime-agent · GitHub Skip to content Navigation Menu Sign in Appearance settings Pl
- mbsdeepak/loom — The context-engineering layer for an agent — chunking, embeddings, vector retrieval, history compact
- liventruth/HROC-Cognitive-Framework — The NeuroPhoenix HROC framework is an enterprise-grade cognitive architecture designed to eliminate

## Scale Packets
- proof_artifact: promoted (64c852cd68fd)
- public_wedge: promoted (a273c5b67bb7)
- buyer_experiment: promoted (827ca65adeae)
- operator_doctrine: promoted (efeaeaf31a19)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (64c852cd68fd)
- public_wedge: queued_echo_draft (a273c5b67bb7)
- buyer_experiment: queued_buyer_experiment (827ca65adeae)
- operator_doctrine: already_persisted (efeaeaf31a19)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
