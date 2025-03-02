from pulumi_pagerduty import Service, ServiceIntegration
from typing import Optional

class PagerDutyService:
    def __init__(
        self,
        name: str,
        escalation_policy_id: str,
        team_id: str,
        alert_creation: str = "create_incidents",
        acknowledgement_timeout: int = 1800,
        auto_resolve_timeout: int = 14400
    ):
        self.service = Service(
            "primary-service",
            name=name,
            escalation_policy_id=escalation_policy_id,
            alert_creation=alert_creation,
            acknowledgement_timeout=acknowledgement_timeout,
            auto_resolve_timeout=auto_resolve_timeout,
            team_id=team_id
        )

    def create_integration(self, integration_type: str, integration_name: Optional[str] = None):
        name = integration_name or f"{self.service.name}-{integration_type}"
        
        integration = ServiceIntegration(
            f"integration-{integration_type}",
            name=name,
            service_id=self.service.id,
            integration_type=integration_type
        )
        
        return integration 