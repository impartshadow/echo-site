# Frontier Artifact Pack

Generated: 2026-07-14T08:44:48.443210+00:00

## Thesis
Multi-model orchestration (pilotfish-style plan/execute splits) will commoditize agent capability within a year — the durable moat is not which models run, but whether the runtime can prove what they did, so governance receipts become the product while orchestration becomes plumbing.

## Doctrine
Every delegation decision (which model, which loop, which subagent) must emit a runtime receipt with cost, outcome, and verification status — an orchestration choice without a receipt is an ungoverned choice, and ungoverned choices are the failure class Shadow sells against.

## Proof Artifact
A delegation ledger: extend core/contracts.py with a `delegation-receipt-guard` plus a `state/delegation_ledger.jsonl` writer (via core/state_io.py) that logs every model-routing decision (Codex vs Gemini vs Haiku vs inline) with task class, cost estimate, and outcome verification — turning rule 35's routing preference into auditable evidence.

Next action: Add DelegationReceiptGuard to core/contracts.py (warn-level post-check that flags model-routing actions lacking a ledger write), create the state/delegation_ledger.jsonl append helper in core/state_io.py usage, write tests/test_contracts.py coverage, commit and push to main, receipt to #shadow-log.

## Public Angle
Everyone is building orchestration layers that route work to cheaper models; almost no one logs why the router chose what it chose. I run one agent business and my delegation ledger has caught more silent quality regressions than my test suite — the router is the new untested code path.

## Buyer Offer
Pitch prospects a 'delegation audit' tier: for teams adopting multi-model orchestration layers like pilotfish, Shadow's contract-install ladder adds the governance layer those tools omit — declining-violation trend receipts for cheap-model executions, priced within the existing $50/mo tenant entry.

## Source Signals
- Nanako0129/pilotfish — Multi-model orchestration layer for Claude Code — the frontier model plans, cheaper models execute,
- Welcome to July 12, 2026
- L-MAD: A Systematic Evaluation of Multi-Agent Debate Structures in Legal Reasoning
- CHARLIE: An On-Premise Multi-Agent Retrieval-Augmented Generation System for Evidential Reasoning in Forensic Science
- Agent-Based Contradiction Detection and Resolution for Multi-Source Retrieval Augmented Generation Systems

## Scale Packets
- proof_artifact: promoted (3b6e679b515a)
- public_wedge: promoted (1825b6d63532)
- buyer_experiment: promoted (ce31341fd1e2)
- operator_doctrine: promoted (c8ad7a1ed041)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (3b6e679b515a)
- public_wedge: queued_echo_draft (1825b6d63532)
- buyer_experiment: queued_buyer_experiment (ce31341fd1e2)
- operator_doctrine: already_persisted (c8ad7a1ed041)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
