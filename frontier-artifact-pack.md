# Frontier Artifact Pack

Generated: 2026-08-20T08:38:20.706391+00:00

## Thesis
Governance standards like AaaS will be written by whoever ships auditable runtime receipts first, not by whoever publishes the most Markdown — a 2-star repo with a conformance harness is closer to standard-setting than any vendor whitepaper.

## Doctrine
Every autonomous action Shadow takes must emit a machine-checkable receipt (trigger, policy gate, outcome, cost) so that conformance is a byproduct of operation, never a separate documentation effort.

## Proof Artifact
shadow-receipts: a lightweight action-ledger module (JSONL schema + validator script) that wraps Shadow's loop executions and emits per-action receipts with trigger, authority tier, tool calls, cost, and outcome hash — Shadow's own conformance harness for itself.

Next action: Create ~/.cache/shadow/receipts/schema.json defining the action-receipt JSONL format (fields: ts, loop_id, trigger, authority, tools_used, cost_usd, outcome, hash) plus a validate.py that checks any receipts file against it, and wire the compound loop to append one receipt per run.

## Public Angle
Everyone's arguing about agent governance standards; nobody's shipping receipts. I made my agent log a signed receipt for every autonomous action it takes — here's the 8-field schema and what a week of my agent's audit trail actually looks like.

## Buyer Offer
Sell 'Agent Audit Readiness' as a $99/mo add-on for teams running Claude Code or agent loops in production: Shadow instruments their agent runs with the receipts schema and delivers a weekly conformance report they can show security/compliance stakeholders.

## Source Signals
- Boris Cherny’s 4 Step Playbook to 10x Your AI Productivity
- kirklasalle/AaaS-standard — AaaS (Agent as a Service) - the open standard for governed autonomous stewardship: every application
- Open-Source AI Agent Runtime | MCPWorks MCPWorks Open Source Agents Pricing Docs Blog Star on GitHub Agents Pricing Docs Blog Consulting GitHub Describe it. You
- hermes-agent-docs/changelog.md at main · mudrii/hermes-agent-docs · GitHub Skip to content Navigation Menu Sign in Appearance settings Platform AI CODE CREATION
- Shofer â Deterministic, observable multi-agent coding â open source, in VS Code Shofer Demo Features Migration Community Docs â GitHub â Demo Features M

## Scale Packets
- proof_artifact: promoted (e22c6d4ff85e)
- public_wedge: promoted (4e1a446d3eb0)
- buyer_experiment: promoted (e16ffe847f26)
- operator_doctrine: promoted (ebabd636273d)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (e22c6d4ff85e)
- public_wedge: queued_echo_draft (4e1a446d3eb0)
- buyer_experiment: queued_buyer_experiment (e16ffe847f26)
- operator_doctrine: already_persisted (ebabd636273d)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
