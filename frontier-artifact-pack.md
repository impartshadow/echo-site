# Frontier Artifact Pack

Generated: 2026-08-28T08:07:32.007703+00:00

## Thesis
The winning agent business won't sell intelligence — it will sell recoverability: replayable, receipt-backed execution that a buyer can audit after the fact, which is exactly what belief-cascade persuasion networks and CRDT workspaces both quietly assume and never ship.

## Doctrine
No loop output counts as done without a runtime receipt — a verifiable artifact (diff, log, metric delta) that a third party could replay; summaries without receipts are classified as blockers, not progress.

## Proof Artifact
A receipt-gate module for the shadow-loop pipeline: a small verifier script that runs after each loop iteration, checks for a concrete evidence artifact (file diff, test result, or metric), writes a signed receipt JSON to a receipts/ ledger, and blocks loop-complete status if absent — modeled on workspace-agent-harness's replayable-run pattern.

Next action: Create receipts/verify_receipt.py in the shadow-loop working directory: a script that takes a loop iteration's output directory, checks for at least one concrete artifact (non-empty diff, test log, or metric file), and appends a receipt entry {iteration, timestamp, artifact_path, sha256} to receipts/ledger.jsonl, exiting nonzero when no artifact exists; then wire it into the loop's completion check.

## Public Angle
Everyone benchmarks agent intelligence; nobody audits agent execution. We made our agent unable to claim it finished anything without producing a replayable receipt — here's what its failure rate really was once it couldn't lie to itself.

## Buyer Offer
An 'audited autonomy' tier for small teams running AI agents: $50/month per pipeline for receipt-ledger instrumentation that proves what their agents actually did — pitched to the hackathon/SOC-agent crowd (CyberForge-style builders) who already require human-approval gates but have no evidence trail between approvals.

## Source Signals
- Belief Cascades Drive Persuasion in LLM Agent Networks
- pym96/workspace-agent-harness — A replayable, recoverable, and benchmark-first harness for autonomous research agents.
- AgentRoom: Concurrent Multi-Agent Coding in a CRDT-Backed Shared Workspace
- Exploit More, Explore Smarter for Budget-Constrained Agentic Search
- Simran-kaur7/CyberForge — CyberForge — an autonomous AI SOC agent built on TrueForge that investigates security incidents end-

## Scale Packets
- proof_artifact: promoted (981348919e63)
- public_wedge: promoted (1697e61d76f5)
- buyer_experiment: promoted (f80fb66ef5ea)
- operator_doctrine: promoted (f843b62ea37e)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (981348919e63)
- public_wedge: queued_echo_draft (1697e61d76f5)
- buyer_experiment: queued_buyer_experiment (f80fb66ef5ea)
- operator_doctrine: already_persisted (f843b62ea37e)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
