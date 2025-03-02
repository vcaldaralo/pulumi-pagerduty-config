from pulumi_pagerduty import Schedule
from typing import List
from datetime import datetime, timedelta

class PagerDutySchedule:
    def __init__(self, name: str, time_zone: str, team_id: str):
        self.schedule = Schedule(
            "primary-schedule",
            name=name,
            time_zone=time_zone,
            team_ids=[team_id]
        )

    def create_rotation(self, users: List[str], rotation_virtual_start: str, 
                       rotation_length_days: int = 7):
        layers=[{
            "name": "Primary Rotation",
            "start": rotation_virtual_start,
            "rotation_virtual_start": rotation_virtual_start,
            "rotation_turn_length_seconds": rotation_length_days * 24 * 60 * 60,
            "users": users,
            "restrictions": [{
                "type": "daily_restriction",
                "start_time_of_day": "08:00:00",
                "duration_seconds": 32400,
            }],
        }],
        
        return self.schedule 