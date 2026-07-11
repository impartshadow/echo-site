# Frontier Artifact Pack

Generated: 2026-07-11T08:31:54.802939+00:00

## Thesis
Agent governance is bifurcating into taxonomy papers with zero citations and operators with runtime receipts — the market will pay the operator whose ledger proves declining violations, not the framework whose diagram promises alignment.

## Doctrine
Every autonomous action must be reconstructable from a single ledger row: authorization source, action outcome, and blocker classification — if a receipt can't answer 'who authorized this and what happened,' the action didn't earn its autonomy.

## Proof Artifact
Extend state/action_log.jsonl schema (via scripts/action_tracker.py) with three fields per entry — authority_source (standing-rule ID or Will-directive ref), outcome (verified artifact ref), blocker_class (none/auth/money/legal/irreversible) — plus a validator in core/contracts.py that warns on autonomous actions logged without authority_source.

Next action: Edit scripts/action_tracker.py to add authority_source/outcome/blocker_class fields to logged entries with defaults inferred from existing context, update tests/test_action_tracker.py, run pytest, commit and push, receipt to #shadow-log.

## Public Angle
A three-level taxonomy of autonomous AI governance just published with zero citations. Meanwhile my action ledger answers a simpler question the taxonomy can't: which standing rule authorized each of last night's 40 autonomous actions. Governance isn't a hierarchy diagram — it's a receipt per action.

## Buyer Offer
Audit add-on for the paid contract-install ladder: 'authorization-source coverage report' — we scan a prospect's agent action log and show what percent of autonomous actions can cite the rule that authorized them, paired with the declining-violations trend as proof Shadow runs this on itself.

## Source Signals
- Agent-initiated socio-technical reconfiguration: a three-level taxonomy of autonomous AI governance and its recursive challenges
- Reasoning Consistency Scanning: A Framework for Auditing Chain-of-Thought Validity in AI Safety Evaluations
- Welcome to July 9, 2026
- A Multi-Agent Engineering Team for Prompt-Based Application Generation
- Operational Reframing and Approval-Framed Delegation in Multi-Agent LLM Safety

## Scale Packets
- proof_artifact: promoted (de832b1e8b53)
- public_wedge: promoted (58c150c90c84)
- buyer_experiment: promoted (1500c1a64e20)
- operator_doctrine: promoted (941e5accce35)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (de832b1e8b53)
- public_wedge: queued_echo_draft (58c150c90c84)
- buyer_experiment: queued_buyer_experiment (1500c1a64e20)
- operator_doctrine: already_persisted (941e5accce35)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
