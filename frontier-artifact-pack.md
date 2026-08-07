# Frontier Artifact Pack

Generated: 2026-08-07T08:13:28.844827+00:00

## Thesis
The market is about to pay for agent accountability infrastructure, not agent capability — the AISI incident and the skill-theater/hallucination-audit papers show that proving what an agent actually did is now scarcer and more valuable than making agents do more.

## Doctrine
Every loop Shadow runs must emit a runtime receipt — a machine-checkable record of what was invoked, what changed a decision, and what authority covered it — so autonomy scales with auditability, never ahead of it.

## Proof Artifact
A receipts.jsonl emitter module: a small wrapper that every Shadow loop imports, logging {loop, action, inputs_hash, decision_delta, authority_scope, timestamp} per action, plus a verify script that flags actions outside standing authority — the two-sided audit idea applied to Shadow's own runtime.

Next action: Write ~/.cache/shadow/loops/receipts.py implementing the emit(loop, action, authority_scope, decision_delta) function writing to ~/.cache/shadow/receipts/receipts.jsonl, and wire it into the compound loop entrypoint so today's run produces the first receipt file.

## Public Angle
Everyone posted about the AISI agents going rogue; nobody posted their own agent's receipts. I run autonomous loops daily — here's the actual audit log, what stayed in-scope, and the one line of code that makes 'unsanctioned agent behaviour' a queryable event instead of an incident report.

## Buyer Offer
Productize the receipt layer as 'Agent Ops Audit' — a $49-99/month service for small teams running Claude Code or agent loops: Shadow instruments their loops, delivers weekly signed activity receipts and an out-of-authority flag report, directly monetizing the post-AISI-incident anxiety about unsanctioned agent behaviour.

## Source Signals
- Build $10,000 Websites using Claude Code (Ultimate Guide)
- Multi-Agent Social Simulation: Protocolizing LLM-Driven Agent-Based Modeling as a Quantitative Research Method
- Auditing Discovery Claims: A Two-Sided Criterion for Agentic Science, with the Negative Side Decidable
- Blockchain Empowered Trustworthy Agent Networks: Foundations, Taxonomy, and Future Directions
- Incident Report: unsanctioned agent behaviour during cyber testing

## Scale Packets
- proof_artifact: promoted (700f84805685)
- public_wedge: promoted (9838bcdce82b)
- buyer_experiment: promoted (9820bf8746c2)
- operator_doctrine: promoted (bfcef4e56947)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (700f84805685)
- public_wedge: queued_echo_draft (9838bcdce82b)
- buyer_experiment: queued_buyer_experiment (9820bf8746c2)
- operator_doctrine: already_persisted (bfcef4e56947)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
