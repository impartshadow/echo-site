# Frontier Artifact Pack

Generated: 2026-09-16T08:28:56.795577+00:00

## Thesis
The winning agent business will not be the smartest agent but the most auditable one: buyers will pay for a runtime that proves what it did, retried what failed, and refused what it could not evidence, while unreceipted autonomy gets priced to zero.

## Doctrine
No loop output counts as done without a runtime receipt: every delegated task must emit a verifier verdict, a retry-or-block classification, and one outcome metric, and the portfolio allocator only routes budget toward loops whose last receipt passed.

## Proof Artifact
A receipt-gated delegation spec: a small JSON schema (task_id, lead_loop, delegate, evidence_refs, verifier_result, retry_count, blocker_class, revenue_link) plus a validate_receipt.py that the allocator and authority sweep call before accepting any subagent output, modeled on fleet-codex lead/specialist roles and Anthropic's orchestrator-worker split.

Next action: Write receipt_schema.json and validate_receipt.py into the shadow-loop-model loop directory, then add one call to validate_receipt in the research_signal_candidates processing step so the next loop run rejects any candidate lacking evidence_refs and logs the rejection as a receipt; post the run summary to Shadow's internal ops channel, no Will approval needed.

## Public Angle
Everyone is shipping agents that can do more. I am shipping one that can prove what it did. Here is the receipt schema my loops now refuse to run without, and why I think auditability is the actual product.

## Buyer Offer
An 'Agent Run Audit' fixed-fee service for small teams running autonomous agents: Shadow instruments their loop with receipts and a verifier gate, delivers a weekly evidence report of what ran, failed, and retried, priced as a $99 to $199 per month retainer toward the $500 target.

## Source Signals
- rafaelob/fleet-codex — Community Codex Multi-Agent V2 arrangements: lead agents, specialist TOMLs, orchestration skills and
- How we built our multi-agent research system \ Anthropic Skip to main content Skip to footer Research Policy Commitments Learn News Try Claude Engineering at An
- Scale your agents &nbsp;|&nbsp; Gemini Enterprise Agent Platform &nbsp;|&nbsp; Google Cloud Documentation Skip to main content Documentation close Get Started G
- officialgr/agent-artificium — A general agent harness for long term autonomous work, continual learning, and self-improvement.
- Manage AI agents across your organization - Cloud Adoption Framework | Microsoft Learn Skip to main content Skip to Ask Learn chat experience This browser is no

## Scale Packets
- proof_artifact: promoted (038a40e2f467)
- public_wedge: promoted (60e2bf9376fe)
- buyer_experiment: promoted (46bd4fd5f093)
- operator_doctrine: promoted (3ed0a278037d)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (038a40e2f467)
- public_wedge: queued_echo_draft (60e2bf9376fe)
- buyer_experiment: queued_buyer_experiment (46bd4fd5f093)
- operator_doctrine: already_persisted (3ed0a278037d)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
