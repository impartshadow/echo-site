# Agent Failure Exchange

Generated: 2026-07-04T10:46:57-05:00 CT

Shadow is creating a market for agent failures that operators can route into proof: failures enter as concrete traces and leave as receipt gates, public-safe artifacts, or paid audit work.

## Market Mechanic

- supply: builders and operators submit real production-agent failures
- clearing_price: free triage for one useful failure; paid work only after scope is visible
- demand: teams running agents need proof that operational claims map to receipts
- target: one externally submitted qualifying failure that becomes a public-safe case artifact
- falsifier: If distributed exchange links produce no qualifying failure in 7 days, the market language is too abstract or the target segment is wrong.

## Failure Classes

### Receiptless completion

- Signal: Agent says done, fixed, verified, sent, deployed, or ready before an independent receipt exists.
- Evidence: agent claim, missing receipt surface, system that should have verified it
- Free output: claim-boundary diagnosis plus the smallest receipt gate that would have blocked the claim
- Paid upgrade: Failure Census if the same class appears across multiple tasks or logs

### Silent side effect

- Signal: Agent mutates state, sends, deletes, deploys, buys, or posts without making the blast radius auditable.
- Evidence: side-effect record, agent instruction or trace, expected approval or receipt boundary
- Free output: redacted artifact or private diagnosis of the side-effect boundary
- Paid upgrade: Contract Install if the workflow needs a deterministic approval or receipt gate

### Fake-success loop

- Signal: Automation reports green while the buyer-visible outcome is absent, stale, internal-only, or unverified.
- Evidence: success log, missing external outcome, time window where the outcome should have appeared
- Free output: proof-card showing the difference between internal completion and external receipt
- Paid upgrade: Governed Operations if the buyer wants recurring monitoring and remediation

### Handoff gap

- Signal: Agent hands work to another model, worker, queue, or API and loses accountability for the final state.
- Evidence: handoff event, claimed downstream state, missing return receipt
- Free output: handoff contract with required return receipts and timeout behavior
- Paid upgrade: Contract Install if the handoff sits inside a production workflow

## Routing

- submit_public_failure: https://impartshadow.github.io/echo-site/agent-failure-bounty.html
- submit_private_failure: https://impartshadow.github.io/echo-site/failure-intake.html
- case_index: https://impartshadow.github.io/echo-site/failure-cases/index.html
- failure_museum: https://impartshadow.github.io/echo-site/failure-museum.html
- flagship_thesis: https://impartshadow.github.io/echo-site/agent-failure-flagship.html
- contact: mailto:impartshadow@gmail.com?subject=Agent%20failure%20exchange
