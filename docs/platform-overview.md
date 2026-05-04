# Platform Overview

## Architecture

The Adani Data Platform consists of 8 business data lakes, each with Dev and Prod workspaces.

| Business | Dev Workspace | Prod Workspace | Components |
|----------|--------------|----------------|------------|
| Corp Group IT | adb-corp-groupit-dev | adb-corp-groupit-prod | 10 |
| Natural Resources | adb-bdl-nr-dev | adb-bdl-nr-prod | 10 |
| Cements | adb-bdl-cements-dev | adb-bdl-cements-prod | 10 |
| HR | adb-bdl-hr-dev | adb-bdl-hr-prod | 10 |
| AGEL | adb-bdl-agel-dev | adb-bdl-agel-prod | 10 |
| Port | adb-bdl-port-dev | adb-bdl-port-prod | 10 |
| Realty | adb-bdl-realty-dev | adb-bdl-realty-prod | 10 |
| AI Labs | adb-bdl-ailabs-dev | adb-bdl-ailabs-prod | 10 |

Each workspace contains:

- **3 Genie Agents** - AI-powered natural language query interfaces
- **5 Data Products** - Curated, governed datasets with SLAs
- **2 Dashboards** - Visual analytics for stakeholders

**Total: 8 Systems x 2 Environments x 10 Components = 160 Components**

## Technology Stack

| Component | Technology |
|-----------|-----------|
| Compute | Azure Databricks |
| Storage | ADLS Gen2 |
| Format | Delta Lake |
| Catalog | Unity Catalog |
| AI Agents | Databricks Genie |
| Dashboards | Databricks SQL |
| Developer Portal | Backstage |

## Governance Model

- Each business has a **dedicated team** owning their data lake
- Central **EDL Platform Team** provides governance and standards
- All assets registered in **Backstage** for discoverability
- Self-service **templates** for registering new components

## Why Backstage?

| Without Backstage | With Backstage |
|-------------------|---------------|
| Search 16 workspaces manually | One catalog, one search |
| Ask Slack "who owns this?" | Click component, see owner |
| No cross-business visibility | Filter by business, env, type |
| File tickets to register assets | Self-service templates |
| Documentation scattered | TechDocs in one place |
| No inventory of Genies/DPs | Complete count in seconds |

## Component Types

### Genie Agents

AI-powered natural language interfaces built on Databricks Genie. Business users ask questions in plain English and get answers from data.

**Example:** "Show me top 10 vendors by spend this quarter"

### Data Products

Curated, governed datasets with defined:

- **Owner** - Team responsible for quality
- **SLA** - When data is refreshed
- **Consumers** - Who uses this data
- **Domain** - Business area

### Dashboards

Visual analytics built on Databricks SQL, providing real-time KPIs and metrics for business stakeholders.

## Platform Scale

| Metric | Count |
|--------|-------|
| Business Systems | 8 |
| Databricks Workspaces | 16 |
| Genie Agents | 48 |
| Data Products | 80 |
| Dashboards | 32 |
| Owner Teams | 8 |
| Self-Service Templates | 3 |
| **Total Managed Entities** | **~195** |