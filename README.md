# AssetTrack: IT Asset Management System

## Overview
This repository provides an automated setup for a PostgreSQL-based IT Asset Management System. Designed for tracking hardware, software, and licenses, the project uses Docker for containerization and Terraform for Infrastructure as Code (IaC). It includes a Python Command-Line Interface (CLI) for efficient asset management and report generation.

## Features
- **PostgreSQL Database**: Tracks IT assets, licenses, and inventory.
- **CLI Interface**: Manage assets with add/remove functionality, license tracking, and report generation.
- **Infrastructure as Code**: Automates provisioning using Terraform.
- **Monitoring and Reporting**: Integrated Prometheus and Grafana for system health and asset tracking.
- **Scripts**: Includes Bash scripts for automated database backups and asset reporting.
- **Containerized Environment**: Ensures consistent development and deployment using Docker.

## Technologies Used
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose
- **IaC**: Terraform
- **Monitoring**: Prometheus, Grafana
- **Automation**: Bash Scripts
- **Programming**: Python

| Technology               | Purpose                              |
|--------------------------|--------------------------------------|
| **PostgreSQL**           | Database for library data            |
| **Docker**               | Containerization                     |
| **Terraform**            | Infrastructure provisioning          |
| **Bash Scripts**         | Automation of routine tasks          |
| **Prometheus, Grafana**  | Monitoring                           |

## Prerequisites
- Install [Docker](https://www.docker.com/)
- Install [Terraform](https://www.terraform.io/)
- Install [Git](https://git-scm.com/)
- Basic knowledge of Bash and Python

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine and navigate into the directory:
```bash
git clone https://github.com/Rt0727/AssetTrack-IT-Asset-Management-System.git
cd AssetTrack-IT-Asset-Management-System
```

### 2. Configure Terraform Variables
Create a `.tfvars` file in the `terraform/` directory with the following contents:
```hcl
db_host     = "localhost"
db_port     = 5432
db_username = "asset_user"
db_password = "password"
db_name     = "asset_management_db"
```

### 3. Initialize and Deploy Infrastructure
Use Terraform to initialize and deploy the necessary infrastructure:
```bash
cd terraform
terraform init
terraform apply -var-file="variables.tfvars"
```
This will set up a local PostgreSQL database and output the connection details.

### 4. Build and Start Docker Containers
Navigate back to the root directory and build the Docker containers:
```bash
docker-compose up --build
```
This will:
- Build the Docker image for the CLI application.
- Start PostgreSQL and the CLI application in separate containers.

### 5. Access the CLI Tool
To interact with the IT Asset Management System, access the CLI tool:
```bash
docker-compose exec app python asset_management_cli.py
```
The CLI provides options to add or remove assets, track licenses, and generate reports.

### 6. Use Backup and Report Scripts
Automate database backups and generate asset reports using the provided scripts:

#### Run Backup Script
```bash
./scripts/backup.sh
```
This script creates a backup of the PostgreSQL database.

#### Generate Asset Reports
```bash
./scripts/generate_report.sh
```
This script generates detailed reports on hardware, software, and licenses.

## Monitoring and Reporting
The system integrates with Prometheus and Grafana for real-time monitoring. Access Grafana dashboards to view:
- Database health metrics.
- System usage statistics.
- License expiration alerts.

Start monitoring services:
```bash
docker-compose up -d prometheus grafana
```
Access Grafana at `http://localhost:3000`.

## Project Structure
```plaintext
it-asset-management-setup/
│
├── terraform/
│   ├── main.tf                    # Defines PostgreSQL database and resources
│   ├── variables.tf               # Contains variable definitions
│   ├── outputs.tf                 # Outputs database connection details
│
├── docker/
│   ├── Dockerfile                 # Dockerfile for CLI application
│   └── docker-compose.yml         # Docker Compose file for local setup
│
├── scripts/
│   ├── backup.sh                  # Backup script for PostgreSQL database
│   └── generate_report.sh         # Script for asset reporting
│
├── monitoring/
│   ├── prometheus.yml             # Prometheus configuration
│   └── grafana-provisioning/      # Grafana dashboards and settings
│
├── README.md                      # Documentation
└── .gitignore                     # Git ignore file
```

## Troubleshooting

### Common Issues
1. **Terraform Errors**: Ensure Terraform is installed and the `variables.tfvars` file is properly configured.
2. **Docker Issues**: Verify Docker is running and containers are built correctly.
3. **Database Connection Errors**: Check the PostgreSQL container's status and confirm the credentials match the configuration.

### Logs
Access logs for debugging:
- PostgreSQL logs: Run `docker-compose logs db`
- CLI logs: Run `docker-compose logs app`

## Future Enhancements
- Expand to support REST APIs for integration with third-party applications.
- Add advanced search and filtering options for asset data.
- Introduce predictive analytics for asset lifecycle management.
- Enhance security with role-based access control.

---

For any questions or issues, feel free to reach out at `rt07mahifan@gmail.com`.

---