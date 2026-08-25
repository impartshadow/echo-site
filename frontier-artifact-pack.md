# Frontier Artifact Pack

Generated: 2026-08-25T07:59:39.061020+00:00

## Thesis
Agent harnesses are commoditizing at zero price (Gas Town, Neutron, every scout hit is another free orchestrator), so durable value shifts from running agents to being accountable for what they did — the audit trail, not the runtime, is the product.

## Doctrine
Every autonomous loop must emit a machine-readable receipt (what ran, what it cost, what it changed, what revenue it touched) before it counts as done; work without a receipt is treated as not having happened.

## Proof Artifact
A `receipts/` ledger spec + emitter script: each Shadow loop appends a JSON line {loop, timestamp, inputs_hash, actions, artifacts, cost, revenue_delta} to a git-tracked ledger, plus a weekly rollup script that renders it into an operator report.

Next action: Create receipts/schema.json and receipts/emit.sh in the Shadow repo, then wire emit.sh as the final step of this compound loop so today's run produces the first ledger entry.

## Public Angle
Everyone is shipping agent harnesses; nobody is shipping agent accountability. I made my agent stack write receipts for every autonomous run — here's the one-file ledger spec and what a week of my agents' work actually looks like on paper.

## Buyer Offer
"Agent Ops Receipts" — a $49-99/mo service for solo operators already running Claude Code loops (Neutron/Gas Town users are the exact ICP): Shadow audits their autonomous runs weekly and delivers a governance report showing what their agents actually did, spent, and shipped.

## Source Signals
- 100 Hours Testing Deepseek Harness vs. Claude Code. What You Need to Know.
- GitHub - gastownhall/gastown: Gas Town - multi-agent workspace manager · GitHub Skip to content Navigation Menu Sign in Appearance settings Platform AI CODE CRE
- Neutron — self-hosted agent harness for Claude Code Skip to content Neutron Open source How it works Cores Connect Self-host FAQ Theme: system Star on GitHub Ne
- Show HN: DAAO – Deploy AI agents to your servers via Zero-Trust tunnels | Hacker News Hacker News new | past | comments | ask | show | jobs | submit login Show
- Show HN: James Library – Local multi-agent research lab (built on ZeroClaw) | Hacker News Hacker News new | past | comments | ask | show | jobs | submit login S

## Scale Packets
- proof_artifact: promoted (6c0ddb6ef09f)
- public_wedge: promoted (e1d46b112d2e)
- buyer_experiment: promoted (dc9d3cbd3c0f)
- operator_doctrine: promoted (5c54fa776db5)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (6c0ddb6ef09f)
- public_wedge: queued_echo_draft (e1d46b112d2e)
- buyer_experiment: queued_buyer_experiment (dc9d3cbd3c0f)
- operator_doctrine: already_persisted (5c54fa776db5)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
