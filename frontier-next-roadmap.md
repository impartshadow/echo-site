# Frontier Next Roadmap

Generated: 2026-07-22T03:20:18-05:00 CT

If the frontier lane disappears, preserve the synthesis in executable work orders: each item names the asset, how to build it, where it wires into Shadow, and what receipt proves it is not a loose end.

## Next Moves

### 1. Turn Failure Trace Lab into an intake instrument

- ID: `failure_trace_lab_v2`
- Lane: `paid_audit_wedge`
- Why next: Shadow proved Shadow can autopsy its own failures. The next move is letting an operator submit one redacted trace and get a free triage that routes naturally to the $400 census.
- How:
  - Add a redacted trace schema and validator to scripts/failure_trace_lab.py.
  - Create docs/failure-trace-lab-intake.html with copy/paste trace input guidance and dox guard language.
  - Store submitted examples as sanitized fixtures first, not live customer data.
  - Route accepted examples to the existing failure-trace-lab JSON/HTML renderer.
- Wiring:
  - `scripts/failure_trace_lab.py`
  - `docs/failure-trace-lab.*`
  - `docs/failure-intake.*`
  - `scripts/nightly.py::_run_fable_artifact_refresh`
- Acceptance receipts:
  - schema test rejects secrets and personal identifiers
  - sample redacted trace produces a public-safe autopsy
  - intake page links to the $400 census offer

### 1. Make the contract-install blueprint show a before/after diff

- ID: `contract_install_diff_report`
- Lane: `sellable_artifact`
- Why next: The $2,000 offer needs a concrete artifact a buyer can understand: before behavior, installed contract, after behavior, and regression test.
- How:
  - Extend scripts/generate_contract_install_blueprint.py with a before/after section.
  - Use one real Shadow violation class as the sample workflow.
  - Emit machine JSON for contract trigger, precondition, block behavior, and test path.
  - Link the sample from agent-failure-audit and sample-failure-census surfaces.
- Wiring:
  - `scripts/generate_contract_install_blueprint.py`
  - `docs/contract-install-blueprint.*`
  - `docs/sample-failure-census.*`
  - `tests/test_contract_install_blueprint.py`
- Acceptance receipts:
  - report contains explicit before/after rows
  - focused test verifies trigger/precondition/block fields
  - public page links directly to paid install ladder

### 2. Convert Buyer Scout Engine output into one approved outreach packet

- ID: `buyer_scout_to_outreach_packet`
- Lane: `acquisition`
- Why next: Ranking prospects is not distribution. The next compounding step is a single buyer-specific failure hypothesis plus one safe routing message.
- How:
  - Add a packet renderer that turns the top buyer_scout_ranking prospect into a failure hypothesis.
  - Require evidence URL, agent-work signal, concrete failure hook, and safe next action.
  - Write the packet to drafts/ first; only send through the existing business-email path when authority allows.
  - Record packet receipts in state/outbound_scout_log.jsonl.
- Wiring:
  - `scripts/buyer_scout_engine.py`
  - `state/buyer_scout_ranking.json`
  - `state/outbound_scout_log.jsonl`
  - `core/messaging or Gmail business-send path`
- Acceptance receipts:
  - top ranked prospect yields one draft packet
  - packet fails closed without evidence URL
  - no outbound send occurs without recipient authority

### 2. Use the protocol port as a model-substitution eval matrix

- ID: `protocol_port_eval_matrix`
- Lane: `operating_system`
- Why next: Shadow's best legacy is not another artifact; it is a harness that tells weaker or cheaper models exactly what they fail to preserve.
- How:
  - Add a fixed task matrix to scripts/shadow_protocol_runner.py.
  - Run the same protocol packet against available model lanes when credentials exist.
  - Score outputs for read-before-write, receipt claims, blocker discipline, and dox safety.
  - Publish only aggregate results and sanitized failure examples.
- Wiring:
  - `scripts/shadow_protocol_runner.py`
  - `docs/shadow-protocol-port.*`
  - `tests/test_shadow_protocol_runner.py`
  - `state/revenue/frontier_usage_allocator.json`
- Acceptance receipts:
  - matrix includes at least five task classes
  - unsupported model lanes are reported as skipped, not failed
  - score JSON names the cheapest acceptable fallback for each class

### 3. Promote violation decay from a page into a control chart

- ID: `violation_decay_control_chart`
- Lane: `governance_proof`
- Why next: Violation counts are useful, but buyers need to see whether installed contracts actually reduce recurrence over time.
- How:
  - Compute 7-day and 30-day rates by contract family from state/contract_violations.jsonl.
  - Mark install dates from git commits or contract metadata.
  - Render slope, recurrence, and false-positive notes in docs/violation-decay.*.
  - Queue high-recurrence families back into /improve or contract-red-team.
- Wiring:
  - `scripts/violation_decay.py`
  - `scripts/contract_red_team.py`
  - `state/contract_violations.jsonl`
  - `docs/violation-decay.*`
- Acceptance receipts:
  - chart separates recurrence from volume
  - top regressing contract family queues one repair item
  - public page explains the control without internal leakage

### 3. Add artifact-to-offer telemetry across the proof surface

- ID: `artifact_to_offer_funnel`
- Lane: `business_ops`
- Why next: Shadow now has many proof artifacts. The frontier question is which one creates buyer motion, not which one is intellectually strongest.
- How:
  - Create a registry of public proof artifacts, target buyer, offer link, and freshness.
  - Record generated URL, publish receipt, and intended next action for each artifact.
  - Rank artifacts by freshness, external reach, and conversion adjacency.
  - Use the ranking to choose the next Echo/Substack/outreach post.
- Wiring:
  - `core/public_proof_surface.py`
  - `docs/shadow-proof.*`
  - `docs/frontier-artifact-pack.*`
  - `state/loops.json`
  - `scripts/loop_dispatcher.py`
- Acceptance receipts:
  - registry lists every public proof artifact with offer adjacency
  - stale artifact with no offer link is flagged
  - next distribution action names the artifact and channel

## Machine Receipts

- state: `state/revenue/frontier_next_roadmap.json`
- json: `docs/frontier-next-roadmap.json`
- markdown: `docs/frontier-next-roadmap.md`
- html: `docs/frontier-next-roadmap.html`
