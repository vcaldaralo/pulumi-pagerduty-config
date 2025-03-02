from pulumi_pagerduty import EscalationPolicy
from typing import List

class PagerDutyEscalationPolicy:
    def __init__(self, name: str, team_id: str):
        self.policy = EscalationPolicy(
            "primary-escalation-policy",
            name=name,
            team_id=team_id,
            num_loops=3,
            rules=[{
                "escalation_delay_in_minutes": 10,
                "targets": [
                    {
                        "type": "schedule_reference",
                        "id": None  # Will be set when schedule is created
                    },
                    {
                        "type": "user_reference",
                        "id": None 
                    },
                ],
            }]            
        )

    def update_schedule_target(self, schedule_id: str):
        self.policy.rules[0].targets[0]["id"] = schedule_id
        return self.policy 