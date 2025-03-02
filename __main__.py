import pulumi
from modules.team import PagerDutyTeam
from modules.schedule import PagerDutySchedule
from modules.escalation_policy import PagerDutyEscalationPolicy
from modules.service import PagerDutyService
from modules.config import team_config, schedule_config, service_config

# Create team
team = PagerDutyTeam(
    name=team_config["name"],
    description=team_config["description"]
)

# Add team members
team_members = [
    {
        "email": "user1@company.com",
        "name": "User One",
        "role": "admin",
        "team_role": "manager"
    },
    {
        "email": "user2@company.com",
        "name": "User Two",
        "role": "user",
        "team_role": "responder"
    }
]

users = team.add_members(team_members)

# Create schedule
schedule = PagerDutySchedule(
    name=schedule_config["name"],
    time_zone=schedule_config["time_zone"],
    team_id=team.team.id
)

# Create rotation
user_ids = [user.id for user in users]
schedule.create_rotation(
    users=user_ids,
    rotation_virtual_start="2024-01-01T00:00:00Z"
)

# Create escalation policy
escalation_policy = PagerDutyEscalationPolicy(
    name="Primary Escalation Policy",
    team_id=team.team.id
)
escalation_policy.update_schedule_target(schedule.schedule.id)

# Create service
service = PagerDutyService(
    name=service_config["name"],
    escalation_policy_id=escalation_policy.policy.id,
    team_id=team.team.id,
    alert_creation=service_config["alert_creation"],
    acknowledgement_timeout=service_config["acknowledgement_timeout"],
    auto_resolve_timeout=service_config["auto_resolve_timeout"]
)

# Create service integration
integration = service.create_integration(
    integration_type="events_api_v2",
    integration_name="Application Monitoring"
)

# Export important values
pulumi.export('team_id', team.team.id)
pulumi.export('schedule_id', schedule.schedule.id)
pulumi.export('escalation_policy_id', escalation_policy.policy.id)
pulumi.export('service_id', service.service.id)
pulumi.export('integration_key', integration.integration_key) 