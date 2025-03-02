from pulumi_pagerduty import Team, User, TeamMembership
from typing import List, Dict

class PagerDutyTeam:
    def __init__(self, name: str, description: str):
        self.team = Team(
            "primary-team",
            name=name,
            description=description
        )

    def add_members(self, members: List[Dict[str, str]]):
        self.users = []
        self.memberships = []
        
        for member in members:
            user = User(
                f"user-{member['email']}",
                email=member['email'],
                name=member['name'],
                role=member.get('role', 'user')
            )
            self.users.append(user)

            membership = TeamMembership(
                f"membership-{member['email']}",
                team_id=self.team.id,
                user_id=user.id,
                role=member.get('team_role', 'manager')
            )
            self.memberships.append(membership)

        return self.users 