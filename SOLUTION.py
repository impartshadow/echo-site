import json
from dataclasses import dataclass, field
from typing import Tuple, Dict, Optional

@dataclass
class ShadowBet:
    """
    Models the state of the Shadow Public Falsification Bounty.
    Encapsulates the 'substack_notes' channel metrics and 'Live demand language' scores.
    """
    bet_id: str
    channel: str
    outcome_progress: Tuple[int, int]
    due_date: str
    meta_channels: str
    live_demands: Dict[str, float]
    last_sync: str

    def __post_init__(self):
        # Normalize the outcome tuple if passed as single int
        if isinstance(self.outcome_progress, int):
            self.outcome_progress = (self.outcome_progress, 1)

        # Ensure live_demands are populated for the 'owned_brief' meta-channel
        if self.meta_channels == "owned_brief":
            self.live_demands["production_coordination_economics_evaluation"] = 6.8
            self.live_demands["co_existence_co_intelligence_book_operational"] = 5.1
            self.live_demands["accountability_compliance_confirmed_control"] = 3.4
            self.live_demands["arxiv_inversion_trust_architecture"] = 3.4
            self.live_demands["best_of_delivery_deployer_echo"] = 2.55

        # Normalize bet_id if generic
        if self.bet_id == "bet":
            self.bet_id = "shadow:falsification-bounty:v1"

    def increment_humans(self) -> int:
        """Increments the current outcome count by one."""
        current = self.outcome_progress[0]
        total = self.outcome_progress[1]
        self.outcome_progress = (current + 1, total)
        return current + 1

    def get_machine_proof(self) -> str:
        """Formats the state for the Machine Proof artifact."""
        progress = self.outcome_progress[0]
        total = self.outcome_progress[1]
        data = {
            "bet_id": self.bet_id,
            "channel": self.channel,
            "progress": f"{progress}/{total}",
            "due": self.due_date,
            "demands": self.live_demands,
            "sync": self.last_sync
        }
        return json.dumps(data, indent=2)

    def get_human_proof(self) -> str:
        """Generates the specific string artifact for Human Proof."""
        score = self.live_demands.get("production_coordination_economics_evaluation")
        return f'`production coordination economics evaluation` (score={score}; channels={self.meta_channels})'

    def validate_falsification(self) -> bool:
        """Returns True if the outcome counter meets the expectation."""
        return self.outcome_progress[0] >= self.outcome_progress[1]

def main():
    """
    Entry point to instantiate the state and output the JSON proof
    for the Shadow acquisition bet.
    """
    bet = ShadowBet(
        bet_id="shadow:falsification-bounty:v1",
        channel="substack_notes",
        outcome_progress=(0, 1),
        due_date="2026-09-12T08:21:04.976358+00:00",
        meta_channels="owned_brief",
        last_sync="2026-09-05T08:24:18.956721+00:00",
        live_demands={
            "bet_version": 1.0,
            "falsifier": "null"
        }
    )

    # Simulate the current state and output the Machine Proof
    # This represents the artifact available at .../shadow-proof.json
    print(bet.get_machine_proof())

    # Uncomment next line to print the specific Human Demand Language string
    # print(bet.get_human_proof())

if __name__ == "__main__":
    main()