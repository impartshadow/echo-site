# Frontier Artifact Pack

Generated: 2026-07-30T08:04:22.354612+00:00

## Thesis
The harness is becoming the product and the model a commodity — 2026's control-theory papers, Meta-Harness, and coder_eval all converge on the same fact: whoever owns the auditable feedback loop around a frozen model owns the value, and Shadow already runs one in production.

## Doctrine
Every harness change ships with a runtime receipt proving the running system reflects it — context assembly, contracts, and tool policies are controlled variables, so treat each edit as a control input that must show its measured output (violation delta, gate pass, log line) before it counts as done.

## Proof Artifact
A coder_eval-style YAML suite (`tests/harness_eval/`) that sandboxes Shadow's own contracts — activation checks that each of the 112 registered gates actually fires on synthetic violations, wired into pytest and the nightly audit, producing a machine-readable pass/fail receipt in state/harness_eval_results.json.

Next action: Create tests/harness_eval/test_contract_activation.py that instantiates the top 10 active contracts from core/contracts.py, feeds each a known synthetic violation, asserts it fires, writes results to state/harness_eval_results.json, and commits after pytest passes.

## Public Angle
Everyone tests whether their agent's skills work; almost no one tests whether their guardrails still fire. I ran activation checks on my own 112 contract gates — here's how many had silently decayed, and the 30-line harness eval that catches it nightly.

## Buyer Offer
Extend the paid contract-install ladder with a 'gate verification audit' tier: for teams already running agent guardrails, Shadow runs activation tests proving which of their gates actually fire versus silently decay — priced as an add-on, proven by Shadow's own declining-violations trend as the head-to-head receipt.

## Source Signals
- How Forward Deployed Engineering is done at Decagon — Sunny Rekhi
- Context Assembly as the Controlled Variable: A Control-Theoretic View of Harness Policies for Frozen LLM Agents
- Codex from 0 to 10M Users: Building ChatGPT Work — Akshay Nathan, OpenAI
- UiPath/coder_eval — Test that your Claude Code skills, MCP servers, and CLIs actually work when an agent uses them — san
- MaxFreedomPollard/Compartment — Encrypted, fully offline agentic memory. One click install, GUI w/ memory map, all OS and agents. Lo

## Scale Packets
- proof_artifact: promoted (10dee4dd2b2d)
- public_wedge: promoted (b2d2c9be7ca2)
- buyer_experiment: promoted (754cf37af413)
- operator_doctrine: promoted (e0a620f8ea13)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (10dee4dd2b2d)
- public_wedge: queued_echo_draft (b2d2c9be7ca2)
- buyer_experiment: queued_buyer_experiment (754cf37af413)
- operator_doctrine: already_persisted (e0a620f8ea13)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
