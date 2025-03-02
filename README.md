# PagerDuty Configuration Management with Pulumi

This project provides Infrastructure as Code (IaC) management for PagerDuty configurations using Pulumi and Python. It allows you to manage teams, schedules, escalation policies, services, and integrations in a version-controlled, automated way.

## Features

- Team and team member management
- On-call schedule creation with rotations
- Escalation policy configuration
- Service and integration setup
- Configuration management through Pulumi
- Modular and maintainable code structure

## Prerequisites

- Python 3.7+
- Pulumi CLI
- PagerDuty account and API token

## Project Structure

```bash
pagerduty-pulumi/
├── Pulumi.yaml
├── requirements.txt
├── main.py
└── modules/
    ├── init.py
    ├── team.py
    ├── schedule.py
    ├── escalation_policy.py
    ├── service.py
    └── config.py
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd pagerduty-pulumi
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

1. Set up your PagerDuty token:

```bash
pulumi config set pagerduty:token <your-token> --secret
```

2. Configure other settings as needed:

```bash
pulumi config set email_domain your-company.com
pulumi config set team_name "Your Team Name"
pulumi config set schedule_name "Your Schedule Name"
pulumi config set schedule_timezone "UTC"
```

## Usage

1. Review the configuration in `modules/config.py`
2. Update team members in `__main__.py` as needed
3. Deploy the infrastructure:

```bash
pulumi up
```

4. To destroy the infrastructure:

```bash
pulumi destroy
```

## Available Configurations

### Team Configuration

- `team_name`: Name of the team
- `team_description`: Description of the team

### Schedule Configuration

- `schedule_name`: Name of the on-call schedule
- `schedule_timezone`: Timezone for the schedule (default: UTC)

### Service Configuration

- `service_name`: Name of the service
- `alert_creation`: Alert creation behavior
- `acknowledgement_timeout`: Timeout for acknowledgements (in seconds)
- `auto_resolve_timeout`: Auto-resolution timeout (in seconds)

## Modules

### Team Module

Manages PagerDuty teams and team members.

### Schedule Module

Handles on-call schedule creation and rotation management.

### Escalation Policy Module

Configures escalation policies and rules.

### Service Module

Manages services and their integrations.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

