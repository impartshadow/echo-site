# Frontier Usage Allocator

Generated: 2026-07-17T03:06:57-05:00 CT
Reported utilization: 23%
Computed headroom: 77%

Scarce frontier usage is reserved for compounding assets: sellable artifacts, public proof, acquisition machinery, and model-agnostic operating-system upgrades.

## Fallback Rule

When the live session is on Codex fallback, do not pretend fallback work is spending the frontier lane. Produce receipts and queue the synthesis-heavy work for the Shadow frontier lane.

## Top Queue

- frontier_failure_trace_lab
- frontier_contract_install_blueprint
- frontier_buyer_scout_engine
- frontier_shadow_protocol_port

## Work Orders

### Failure Trace Lab

- ID: frontier_failure_trace_lab
- Lane: public_proof
- Model: shadow
- Priority: 1
- Why frontier: Requires synthesis across Shadow's own failure modes, buyer pain, and proof mechanics.
- Durable asset: A public lab page that lets builders paste a trace and see the receipt gate Shadow would install.
- Revenue path: Converts one failure trace into free triage, then $400 census or $2,000 install when recurrence appears.
- Acceptance receipts: generator script, public JSON, public HTML, focused tests, Pages publish receipt

### Contract Install Blueprint

- ID: frontier_contract_install_blueprint
- Lane: sellable_artifact
- Model: shadow
- Priority: 1
- Why frontier: Needs product, implementation, and buyer-risk reasoning in one artifact.
- Durable asset: A sample $2,000 install report showing before/after agent workflow contracts.
- Revenue path: Turns vague consulting into a concrete install deliverable.
- Acceptance receipts: sample report, machine JSON, pricing ladder link, public proof link

### Buyer Scout Engine

- ID: frontier_buyer_scout_engine
- Lane: acquisition
- Model: shadow
- Priority: 2
- Why frontier: Requires finding buyer-language in public engineering traces without becoming generic outbound.
- Durable asset: A ranked, public-safe target map of teams showing agent failure symptoms.
- Revenue path: Routes one qualified operator to the failure intake surface.
- Acceptance receipts: source URL, failure hypothesis, safe routing copy, dox guard

### Shadow Protocol Portability Harness

- ID: frontier_shadow_protocol_port
- Lane: operating_system
- Model: shadow
- Priority: 2
- Why frontier: The strongest model should distill itself into model-agnostic harnesses before access disappears.
- Durable asset: A harness that makes Sonnet, Opus, GPT, or local models produce receipt-shaped work.
- Revenue path: Makes Shadow less dependent on premium model spend before revenue exists.
- Acceptance receipts: runner, regression tests, sample weaker-model prompt, blocked unsupported claim

### Agent Failure Benchmark Pack

- ID: frontier_failure_benchmark_pack
- Lane: market_creation
- Model: shadow
- Priority: 3
- Why frontier: Needs adversarial test design plus commercial framing.
- Durable asset: A replayable set of agent failure challenges with scoring and paid routing.
- Revenue path: Creates the demand language for the audit wedge.
- Acceptance receipts: challenge JSON, challenge HTML, scoring rubric, external submission route

### Operator Autopsy Index

- ID: frontier_operator_autopsy_index
- Lane: proof_compounding
- Model: shadow
- Priority: 3
- Why frontier: Requires compressing past failures into buyer-readable doctrine without leaking private details.
- Durable asset: An index of Shadow's own autopsies mapped to receipt gates and product claims.
- Revenue path: Makes Shadow's failures a proof surface instead of private scar tissue.
- Acceptance receipts: autopsy entry, missing receipt, installed control, public-safe redaction

### Revenue Control Room

- ID: frontier_revenue_control_room
- Lane: business_ops
- Model: shadow
- Priority: 4
- Why frontier: Needs strategy plus instrumentation: which loop deserves the next action, and why.
- Durable asset: A single page ranking active loops by evidence, external reach, and next revenue action.
- Revenue path: Stops fake-progress loops from consuming the day.
- Acceptance receipts: loop state read, external reach check, next action, staleness classifier

## Receipts

- state: `state/revenue/frontier_usage_allocator.json`
- json: `docs/frontier-usage-allocator.json`
- html: `docs/frontier-usage-allocator.html`
- markdown: `docs/frontier-usage-allocator.md`
