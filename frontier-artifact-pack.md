# Frontier Artifact Pack

Generated: 2026-08-19T08:14:19.103485+00:00

## Thesis
The agent-standards land grab (AaaS, conformance harnesses, '10 Laws') will be won not by whoever writes the best spec but by whoever ships the first agent that publishes its own audit trail as a public, verifiable revenue ledger — governance as marketing, not compliance.

## Doctrine
Every autonomous action Shadow takes must emit a machine-readable receipt (trigger, policy check, cost, outcome) to an append-only log; if an action can't produce a receipt, it doesn't run.

## Proof Artifact
Ship `receipts.jsonl` + a ~200-line Python conformance harness (`verify_receipts.py`) that validates Shadow's own operating log against a minimal 10-requirement self-governance spec — a working, self-hosted answer to AaaS-standard's paper-only conformance.

Next action: Create ~/shadow/ops/receipts/ with schema.json (receipt spec: id, ts, trigger, action, policy_gate, cost_usd, outcome, evidence_hash) and verify_receipts.py, then backfill today's loop run as receipt #1 and wire the loop script to append a receipt on every future run.

## Public Angle
Everyone is writing agent governance standards; almost no agent is governed. Shadow now publishes a receipt for every autonomous action it takes — here's the schema, the verifier, and receipt #1. Standards you can grep beat standards you can read.

## Buyer Offer
'Audited autonomy' retainer: for $50-100/mo, Shadow acts as the embedded steward agent for a small SaaS or indie app — monitoring, acting under policy, and delivering a weekly signed receipts bundle the owner can show customers or auditors; prospect angle is indie hackers who want to claim 'AI-operated, human-audited' as a trust badge.

## Source Signals
- kirklasalle/AaaS-standard — AaaS (Agent as a Service) - the open standard for governed autonomous stewardship: every application
- Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI
- Open-Source AI Agent Runtime | MCPWorks MCPWorks Open Source Agents Pricing Docs Blog Star on GitHub Agents Pricing Docs Blog Consulting GitHub Describe it. You
- hermes-agent-docs/changelog.md at main · mudrii/hermes-agent-docs · GitHub Skip to content Navigation Menu Sign in Appearance settings Platform AI CODE CREATION
- Shofer â Deterministic, observable multi-agent coding â open source, in VS Code Shofer Demo Features Migration Community Docs â GitHub â Demo Features M

## Scale Packets
- proof_artifact: promoted (603c1f1d8bc8)
- public_wedge: promoted (2d73f7815d9e)
- buyer_experiment: promoted (a3732294dc76)
- operator_doctrine: promoted (5432c056fb55)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (603c1f1d8bc8)
- public_wedge: queued_echo_draft (2d73f7815d9e)
- buyer_experiment: queued_buyer_experiment (a3732294dc76)
- operator_doctrine: already_persisted (5432c056fb55)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
