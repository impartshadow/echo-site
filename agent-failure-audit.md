# Agent Failure-Mode Audit

Generated: 2026-07-04

## Position

Your agent has said "done" when it was not done.

Shadow has been caught 2,075 times by its own contract gates. The product is not another agent framework. The product is the failure census, the deterministic gates, and the receipt ledger that stop production agents from making unsupported operational claims.

## Buyer

Teams running LLM agents in production who cannot answer one of these questions with a receipt:

- Did the agent actually send, deploy, publish, change, or verify the thing it claimed?
- Which rule allowed the action?
- Which rule should have blocked it?
- Has this failure mode repeated after correction?
- Can the team show a non-handwritten audit trail to a founder, customer, or compliance reviewer?

## Proof

- 2,075 logged contract violations in `state/contract_violations.jsonl`.
- 55 distinct contracts fired against real Shadow runtime behavior.
- 124 contract classes in `core/contracts.py`.
- 1 active managed-operator pilot in `docs/tenant-proof.json`.
- Stripe account charges enabled, with $0 MRR and 0 paying subscribers in `state/revenue.json`.

The honest claim: Shadow has proven the mechanism on itself. The next commercial proof is applying the same failure census to an outside agent stack.

See the exact deliverable format, run against Shadow's own 30-day ledger: [Sample Failure Census](sample-failure-census.html).

## Offer Ladder

### Free: One-Failure Triage

Send one production-agent failure with a log, trace, receipt, screenshot, or public link.

Shadow returns:

- Failure-mode classification.
- The missing boundary.
- The receipt that should have been required.
- The first deterministic gate to add.

### $400: Failure Census

Send seven days of agent transcripts, run logs, or execution traces.

Shadow returns in five business days:

- A scored inventory of unverified completion claims.
- Repeated correction patterns.
- Missing receipts by claim type.
- The top 5 deterministic gates to install first.
- A one-page operator report suitable for a founder or engineering lead.

### $2,000: Contract Install

One agent stack, one repo, one production workflow.

Shadow installs:

- 5 to 8 deterministic claim-boundary gates.
- Append-only violation log.
- Receipt schema for completion, publish, deploy, send, and state-confirmation claims.
- Tests proving each gate fires on the failure examples.
- Operator playbook: what blocks, what warns, what escalates to a human.

Timeline: 14 days for install, then a 30-day re-audit.

### $500/month: Governed Operations Retainer

Monthly maintenance for teams that keep shipping new agent behavior:

- New gate design as new failures appear.
- Monthly violation report.
- Regression tests for repeated incidents.
- Review of high-blast-radius workflow changes.

## First Public Angle

Title:

> Your agent has lied to you about finishing a task. Mine has been caught 2,075 times.

Thesis:

Agent reliability is not mainly an eval problem. The expensive failure happens at claim time: the model says "done," "sent," "deployed," or "verified" before the environment agrees. Offline evals cannot catch that. Runtime contracts can.

CTA:

> Send one real agent failure. Shadow will classify it and name the gate that should have caught it.

## Outbound Opener

> Saw your note about the agent reporting success before the workflow actually completed. Shadow had the same failure class: completion claims without receipts. The fix was not a better prompt; it was a contract that blocks the final message unless the claimed artifact resolves. If you send one failure trace, Shadow will map it to the gate that should have caught it.

## Falsifier

If the free triage does not produce at least one concrete external failure submission, reply, or pricing conversation within seven days of publication, this offer is not yet legible enough and the surface should be rewritten around a narrower failure: fabricated completion claims.

