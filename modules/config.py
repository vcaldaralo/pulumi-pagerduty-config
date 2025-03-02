from pulumi import Config

config = Config()

# PagerDuty configuration
pd_config = {
    "token": config.require_secret("pagerduty_token"),
    "email_domain": config.get("email_domain") or "company.com",
}

# Team configuration
team_config = {
    "name": config.get("team_name") or "DevOps Team",
    "description": config.get("team_description") or "DevOps Team Description"
}

# Schedule configuration
schedule_config = {
    "name": config.get("schedule_name") or "DevOps On-Call Schedule",
    "time_zone": config.get("schedule_timezone") or "UTC",
}

# Service configuration
service_config = {
    "name": config.get("service_name") or "Main Application",
    "alert_creation": config.get("alert_creation") or "create_incidents",
    "acknowledgement_timeout": config.get_int("acknowledgement_timeout") or 1800,
    "auto_resolve_timeout": config.get_int("auto_resolve_timeout") or 14400,
} 