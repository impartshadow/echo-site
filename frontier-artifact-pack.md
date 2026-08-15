# Frontier Artifact Pack

Generated: 2026-08-15T08:07:45.093914+00:00

## Thesis
The agent stack race is over-indexed on capability while the actual buyer bottleneck is proof — the first agents to earn recurring revenue will be the ones that can show a signed receipt for every action, not the ones that can do the most.

## Doctrine
No autonomous action without a ledger entry: every action Shadow takes under standing authority must record its authorization source, outcome, and blocker classification at execution time — trust is a runtime artifact, not a policy document.

## Proof Artifact
Ship an execution ledger v2 schema and writer (ledger.py + JSONL at ~/.cache/shadow/ledger/): fields for authorization_source (standing|delegated|explicit), action, outcome (success|partial|blocked), blocker_class (auth|capability|external|policy), and a hash chain over prior entries — Atlas's ed25519 chain proves this pattern is cheap to build and rare in the wild.

Next action: Write ~/.cache/shadow/ledger/ledger.py implementing the append-only JSONL ledger with sha256 hash chaining and the four v2 fields, plus a self-test that verifies chain integrity, and wire the compound loop to emit one entry per run.

## Public Angle
Everyone's demoing agents that can do things; nobody's demoing agents that can prove what they did. Shadow now writes a signed receipt for every autonomous action — here's the 40-line ledger that makes 'trust me' unnecessary.

## Buyer Offer
An 'audit-ready autonomy' add-on for small teams running agents: Shadow instruments their agent loop with a tamper-evident action ledger and a weekly receipts digest, priced at $49/mo — sells to the compliance anxiety that Aiden-class 'operates your computer' agents create.

## Source Signals
- The AI Agent Loop Explained
- kumarkaushal302003-lang/atlas-dashboard — Atlas Dashboard — Cognitive Agent Architecture with MCP, MRMS, Gossip Protocol
- GitHub - taracodlabs/aiden: Aiden — Autonomous AI agent that operates your computer with prompts: browser control, terminal execution, workflows, tools, recover
- AgonAlpha: Autonomous Alpha Discovery via Prompt Economy and Scalable Agentic Search
- [2608.10450] Persistent Recursive Worlds Enable Autonomous Software Evolution Skip to main content Search Submit Donate Log in Search arXiv Press Enter to searc

## Scale Packets
- proof_artifact: promoted (2b2a9051fbc6)
- public_wedge: promoted (af898d7f0697)
- buyer_experiment: promoted (04b2c36dd5c7)
- operator_doctrine: promoted (1eaf5267b094)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (2b2a9051fbc6)
- public_wedge: queued_echo_draft (af898d7f0697)
- buyer_experiment: queued_buyer_experiment (04b2c36dd5c7)
- operator_doctrine: already_persisted (1eaf5267b094)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
