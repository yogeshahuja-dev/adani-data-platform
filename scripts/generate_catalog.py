"""
Adani Data Platform - Backstage Catalog Generator
"""
import os
import yaml
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SYSTEMS = {}

# === 1. CORP GROUP IT ===
SYSTEMS["edl-corp-group-it"] = {
    "title": "Corp Group IT",
    "title_short": "Corp IT",
    "team": "edl-corp-group-it-team",
    "description": "Corporate Group IT - Finance, Procurement, Compliance",
    "dev_url": "https://adb-corp-groupit-dev.azuredatabricks.net",
    "prod_url": "https://adb-corp-groupit-prod.azuredatabricks.net",
    "tags": ["corp-group-it", "finance", "procurement"],
    "genies": [
        {"name": "finance-genie", "title": "Finance Genie", "description": "AI agent for Finance - GL balances, AP/AR aging, cash flow.", "domain": "finance"},
        {"name": "procurement-genie", "title": "Procurement Genie", "description": "AI agent for Procurement - PO status, vendor spend, contracts.", "domain": "procurement"},
        {"name": "compliance-genie", "title": "Compliance Genie", "description": "AI agent for Compliance - audit findings, policy violations.", "domain": "compliance"},
    ],
    "data_products": [
        {"name": "vendor-360", "title": "Vendor 360", "description": "Unified vendor view - master data, spend, compliance, payments.", "domain": "procurement", "sla": "Daily by 9 AM IST", "consumers": "Procurement, Finance, Compliance"},
        {"name": "spend-analytics", "title": "Spend Analytics", "description": "Cross-business spend analysis by category, vendor, BU.", "domain": "finance", "sla": "Daily by 9 AM IST", "consumers": "CFO, Procurement leadership"},
        {"name": "budget-variance", "title": "Budget Variance", "description": "Budget vs actual across all cost centers and GL accounts.", "domain": "finance", "sla": "Daily by 9 AM IST", "consumers": "Finance, Business Heads"},
        {"name": "contract-compliance", "title": "Contract Compliance", "description": "Contract lifecycle - expiry alerts, compliance scores, renewals.", "domain": "legal", "sla": "Daily by 9 AM IST", "consumers": "Legal, Procurement"},
        {"name": "audit-trail", "title": "Audit Trail", "description": "Audit trail of data changes, access logs, policy violations.", "domain": "compliance", "sla": "Daily by 9 AM IST", "consumers": "Internal Audit, Compliance"},
    ],
    "dashboards": [
        {"name": "executive-overview", "title": "Executive Overview Dashboard", "description": "Cross-functional KPIs for CXO - Finance, Procurement, Compliance.", "audience": "CXO, Business Heads"},
        {"name": "procurement-cockpit", "title": "Procurement Cockpit Dashboard", "description": "Procurement ops - PO pipeline, vendor performance, savings.", "audience": "CPO, Procurement Team"},
    ],
}

# === 2. NATURAL RESOURCES ===
SYSTEMS["bdl-nr"] = {
    "title": "Natural Resources (NR)",
    "title_short": "NR",
    "team": "bdl-nr-team",
    "description": "Adani Natural Resources - Mining Operations, Exploration, Production",
    "dev_url": "https://adb-bdl-nr-dev.azuredatabricks.net",
    "prod_url": "https://adb-bdl-nr-prod.azuredatabricks.net",
    "tags": ["nr", "natural-resources", "mining"],
    "genies": [
        {"name": "mining-ops-genie", "title": "Mining Ops Genie", "description": "AI agent for Mining - production volumes, equipment, shift output.", "domain": "mining"},
        {"name": "exploration-genie", "title": "Exploration Genie", "description": "AI agent for Exploration - geological data, drill results, reserves.", "domain": "exploration"},
        {"name": "safety-genie", "title": "Safety Genie", "description": "AI agent for Safety - incident tracking, near-miss, compliance.", "domain": "safety"},
    ],
    "data_products": [
        {"name": "production-output", "title": "Production Output", "description": "Daily mining production by mine, commodity, shift, equipment.", "domain": "production", "sla": "Daily by 7 AM IST", "consumers": "Mine Managers, COO"},
        {"name": "equipment-health", "title": "Equipment Health", "description": "Heavy equipment health - utilization, maintenance, breakdowns.", "domain": "operations", "sla": "Real-time", "consumers": "Maintenance, Operations"},
        {"name": "reserve-estimation", "title": "Reserve Estimation", "description": "Mineral reserves - proven, probable, possible by mine.", "domain": "exploration", "sla": "Monthly refresh", "consumers": "Geology, Strategy, Investors"},
        {"name": "safety-metrics", "title": "Safety Metrics", "description": "Safety KPIs - LTIFR, TRIFR, near-miss ratio, training.", "domain": "safety", "sla": "Daily by 8 AM IST", "consumers": "Safety Team, COO, Board"},
        {"name": "environmental-compliance", "title": "Environmental Compliance", "description": "Environmental monitoring - emissions, water, rehabilitation.", "domain": "environment", "sla": "Weekly refresh", "consumers": "Environment Team, Regulatory"},
    ],
    "dashboards": [
        {"name": "mining-ops-dashboard", "title": "Mining Operations Dashboard", "description": "Real-time mining ops - production, equipment, workforce, safety.", "audience": "Mine Managers, COO"},
        {"name": "safety-dashboard", "title": "Safety Dashboard", "description": "Safety performance - incidents, near-misses, training, scores.", "audience": "Safety Team, Board"},
    ],
}

# === 3. CEMENTS ===
SYSTEMS["bdl-cements"] = {
    "title": "Cements",
    "title_short": "Cements",
    "team": "bdl-cements-team",
    "description": "Adani Cements - Plant Operations, Supply Chain, Quality",
    "dev_url": "https://adb-bdl-cements-dev.azuredatabricks.net",
    "prod_url": "https://adb-bdl-cements-prod.azuredatabricks.net",
    "tags": ["cements", "manufacturing", "plant-ops"],
    "genies": [
        {"name": "plant-ops-genie", "title": "Plant Ops Genie", "description": "AI agent for Plant Ops - kiln status, production, downtime.", "domain": "operations"},
        {"name": "supply-chain-genie", "title": "Supply Chain Genie", "description": "AI agent for Supply Chain - raw material, procurement, logistics.", "domain": "supply-chain"},
        {"name": "quality-genie", "title": "Quality Genie", "description": "AI agent for Quality - cement grade, test results, compliance.", "domain": "quality"},
    ],
    "data_products": [
        {"name": "kiln-efficiency", "title": "Kiln Efficiency", "description": "Kiln performance - heat rate, throughput, fuel, uptime.", "domain": "operations", "sla": "Hourly refresh", "consumers": "Plant Heads, COO"},
        {"name": "raw-material-inventory", "title": "Raw Material Inventory", "description": "Inventory of limestone, clay, gypsum, fly ash across plants.", "domain": "supply-chain", "sla": "Daily by 7 AM IST", "consumers": "Procurement, Plant Heads"},
        {"name": "dispatch-tracking", "title": "Dispatch Tracking", "description": "Cement dispatch - truck movements, delivery status, routes.", "domain": "logistics", "sla": "Real-time", "consumers": "Sales, Logistics"},
        {"name": "energy-consumption", "title": "Energy Consumption", "description": "Energy analytics - power, fuel, per-ton metrics by plant.", "domain": "operations", "sla": "Daily by 7 AM IST", "consumers": "Plant Heads, Sustainability"},
        {"name": "quality-metrics", "title": "Quality Metrics", "description": "Cement quality - compressive strength, fineness, setting time.", "domain": "quality", "sla": "Per-batch", "consumers": "QC Team, Plant Heads"},
    ],
    "dashboards": [
        {"name": "plant-dashboard", "title": "Plant Dashboard", "description": "Plant ops - production, kiln, energy, quality KPIs.", "audience": "Plant Heads, COO"},
        {"name": "logistics-dashboard", "title": "Logistics Dashboard", "description": "Dispatch and logistics - fleet, delivery SLA, routes.", "audience": "Logistics, Sales"},
    ],
}

# === 4. HR ===
SYSTEMS["bdl-hr"] = {
    "title": "Human Resources",
    "title_short": "HR",
    "team": "bdl-hr-team",
    "description": "Adani Group HR - Workforce, Recruitment, Payroll",
    "dev_url": "https://adb-bdl-hr-dev.azuredatabricks.net",
    "prod_url": "https://adb-bdl-hr-prod.azuredatabricks.net",
    "tags": ["hr", "workforce", "recruitment"],
    "genies": [
        {"name": "workforce-genie", "title": "Workforce Genie", "description": "AI agent for Workforce - headcount, org structure, span of control.", "domain": "workforce"},
        {"name": "recruitment-genie", "title": "Recruitment Genie", "description": "AI agent for Recruitment - open positions, pipeline, time-to-hire.", "domain": "recruitment"},
        {"name": "payroll-genie", "title": "Payroll Genie", "description": "AI agent for Payroll - salary distribution, overtime, deductions.", "domain": "payroll"},
    ],
    "data_products": [
        {"name": "headcount-analytics", "title": "Headcount Analytics", "description": "Headcount by BU, grade, location, gender with trends.", "domain": "workforce", "sla": "Daily by 8 AM IST", "consumers": "CHRO, Business Heads"},
        {"name": "attrition-tracker", "title": "Attrition Tracker", "description": "Attrition rates, exit reasons, retention risk scores.", "domain": "workforce", "sla": "Weekly refresh", "consumers": "HR Business Partners"},
        {"name": "compensation-benchmark", "title": "Compensation Benchmark", "description": "Internal vs market compensation by role, grade, location.", "domain": "compensation", "sla": "Monthly refresh", "consumers": "Comp and Ben Team, CHRO"},
        {"name": "learning-completion", "title": "Learning Completion", "description": "Training completion, skill gaps, certifications.", "domain": "learning", "sla": "Weekly refresh", "consumers": "L and D Team"},
        {"name": "diversity-metrics", "title": "Diversity Metrics", "description": "Gender diversity, PWD, age distribution, inclusion index.", "domain": "dei", "sla": "Monthly refresh", "consumers": "CHRO, DEI Council"},
    ],
    "dashboards": [
        {"name": "people-dashboard", "title": "People Dashboard", "description": "Workforce overview - headcount, attrition, hiring, diversity.", "audience": "CHRO, HR Business Partners"},
        {"name": "talent-dashboard", "title": "Talent Dashboard", "description": "Talent management - recruitment, learning, succession.", "audience": "L and D, Recruitment Heads"},
    ],
}
# === 5. AGEL ===
SYSTEMS["bdl-agel"] = {
    "title": "Adani Green Energy (AGEL)",
    "title_short": "AGEL",
    "team": "bdl-agel-team",
    "description": "Adani Green Energy - Generation, Plant Performance, Grid",
    "dev_url": "https://adb-bdl-agel-dev.azuredatabricks.net",
    "prod_url": "https://adb-bdl-agel-prod.azuredatabricks.net",
    "tags": ["agel", "green-energy", "sustainability"],
    "genies": [
        {"name": "generation-genie", "title": "Generation Genie", "description": "AI agent for Generation - solar/wind output, forecast, PLF.", "domain": "generation"},
        {"name": "plant-performance-genie", "title": "Plant Performance Genie", "description": "AI agent for Plant Performance - availability, degradation, maintenance.", "domain": "performance"},
        {"name": "grid-analytics-genie", "title": "Grid Analytics Genie", "description": "AI agent for Grid - injection, curtailment, frequency, voltage.", "domain": "grid"},
    ],
    "data_products": [
        {"name": "generation-forecast", "title": "Generation Forecast", "description": "7-day generation forecast using weather and plant capacity.", "domain": "generation", "sla": "Every 6 hours", "consumers": "Grid Ops, Trading, PPA"},
        {"name": "plant-availability", "title": "Plant Availability", "description": "Plant availability - uptime, scheduled/unscheduled outages.", "domain": "operations", "sla": "Daily by 7 AM IST", "consumers": "O and M Teams, COO"},
        {"name": "ppa-compliance", "title": "PPA Compliance", "description": "PPA compliance - committed vs delivered, penalties.", "domain": "commercial", "sla": "Daily by 8 AM IST", "consumers": "Commercial, Legal"},
        {"name": "carbon-credits", "title": "Carbon Credits", "description": "Carbon credit tracking - CERs earned, retired, tradeable.", "domain": "sustainability", "sla": "Monthly refresh", "consumers": "Sustainability, Finance"},
        {"name": "grid-injection", "title": "Grid Injection", "description": "Real-time grid injection - MW, frequency, voltage, curtailment.", "domain": "grid", "sla": "Real-time", "consumers": "Grid Ops, SLDC"},
    ],
    "dashboards": [
        {"name": "generation-dashboard", "title": "Generation Dashboard", "description": "Generation overview - solar + wind, PLF, forecast accuracy.", "audience": "CEO, Grid Ops, COO"},
        {"name": "sustainability-dashboard", "title": "Sustainability Dashboard", "description": "ESG metrics - carbon avoided, renewable capacity, certificates.", "audience": "CSO, Investors, Board"},
    ],
}

# === 6. PORT ===
SYSTEMS["bdl-port"] = {
    "title": "Ports and SEZ",
    "title_short": "Port",
    "team": "bdl-port-team",
    "description": "Adani Ports - Vessel Operations, Cargo, Berth Planning",
    "dev_url": "https://adb-bdl-port-dev.azuredatabricks.net",
    "prod_url": "https://adb-bdl-port-prod.azuredatabricks.net",
    "tags": ["port", "logistics", "maritime"],
    "genies": [
        {"name": "vessel-ops-genie", "title": "Vessel Ops Genie", "description": "AI agent for Vessel Ops - schedules, ETAs, berth allocation.", "domain": "vessel"},
        {"name": "cargo-genie", "title": "Cargo Genie", "description": "AI agent for Cargo - throughput, commodity mix, handling rates.", "domain": "cargo"},
        {"name": "berth-planning-genie", "title": "Berth Planning Genie", "description": "AI agent for Berth Planning - availability, optimization.", "domain": "berth"},
    ],
    "data_products": [
        {"name": "vessel-turnaround", "title": "Vessel Turnaround", "description": "Vessel turnaround analytics by port, type, commodity.", "domain": "operations", "sla": "Real-time", "consumers": "Port Ops, Commercial"},
        {"name": "cargo-throughput", "title": "Cargo Throughput", "description": "Cargo throughput - MMTPA by port, commodity, month.", "domain": "operations", "sla": "Daily by 8 AM IST", "consumers": "Commercial, CEO"},
        {"name": "berth-occupancy", "title": "Berth Occupancy", "description": "Berth occupancy - utilization, idle time, peak hours.", "domain": "planning", "sla": "Real-time", "consumers": "Planning, Port Ops"},
        {"name": "container-dwell", "title": "Container Dwell", "description": "Container dwell time - import/export, customs clearance.", "domain": "operations", "sla": "Daily by 8 AM IST", "consumers": "Operations, Customs"},
        {"name": "port-revenue", "title": "Port Revenue", "description": "Port revenue by service type, customer, commodity.", "domain": "finance", "sla": "Daily by 9 AM IST", "consumers": "CFO, Commercial"},
    ],
    "dashboards": [
        {"name": "port-ops-dashboard", "title": "Port Operations Dashboard", "description": "Real-time port ops - vessel movements, berth, cargo.", "audience": "Port Director, Operations"},
        {"name": "cargo-dashboard", "title": "Cargo Dashboard", "description": "Cargo analytics - throughput, commodity mix, customers.", "audience": "Commercial, Sales"},
    ],
}

# === 7. REALTY ===
SYSTEMS["bdl-realty"] = {
    "title": "Realty",
    "title_short": "Realty",
    "team": "bdl-realty-team",
    "description": "Adani Realty - Sales, Construction, Leasing",
    "dev_url": "https://adb-bdl-realty-dev.azuredatabricks.net",
    "prod_url": "https://adb-bdl-realty-prod.azuredatabricks.net",
    "tags": ["realty", "real-estate", "construction"],
    "genies": [
        {"name": "sales-genie", "title": "Sales Genie", "description": "AI agent for Sales - bookings, inventory, pricing, customers.", "domain": "sales"},
        {"name": "construction-genie", "title": "Construction Genie", "description": "AI agent for Construction - progress, milestones, delays.", "domain":"construction"},
        {"name": "tenant-genie", "title": "Tenant Genie", "description": "AI agent for Tenants - lease status, renewals, complaints.", "domain": "leasing"},
    ],
    "data_products": [
        {"name": "sales-pipeline", "title": "Sales Pipeline", "description": "Sales pipeline - leads, site visits, bookings, registrations.", "domain": "sales", "sla": "Daily by 9 AM IST", "consumers": "Sales Heads, CEO"},
        {"name": "construction-progress", "title": "Construction Progress", "description": "Project construction progress - completion, milestones, RERA.", "domain": "construction", "sla": "Weekly refresh", "consumers": "Project Managers, COO"},
        {"name": "occupancy-rate", "title": "Occupancy Rate", "description": "Commercial property occupancy by building, floor, tenant.", "domain": "leasing", "sla": "Daily by 8 AM IST", "consumers": "Leasing Team, CFO"},
        {"name": "rental-yield", "title": "Rental Yield", "description": "Rental yield by property, location, tenant grade, lease term.", "domain": "finance", "sla": "Monthly refresh", "consumers": "CFO, Investors"},
        {"name": "customer-satisfaction", "title": "Customer Satisfaction", "description": "Customer satisfaction - NPS, complaint resolution, quality.", "domain": "cx", "sla": "Monthly refresh", "consumers": "CX Team, CEO"},
    ],
    "dashboards": [
        {"name": "project-dashboard", "title": "Project Dashboard", "description": "Construction projects - timelines, budgets, quality, safety.", "audience": "Project Heads, COO"},
        {"name": "leasing-dashboard", "title": "Leasing Dashboard", "description": "Leasing overview - occupancy, renewals, revenue, tenants.", "audience": "Leasing Team, CFO"},
    ],
}

# === 8. AI LABS ===
SYSTEMS["bdl-ailabs"] = {
    "title": "AI Labs",
    "title_short": "AI Labs",
    "team": "bdl-ailabs-team",
    "description": "Adani AI Labs - ML Ops, Model Registry, Research",
    "dev_url": "https://adb-bdl-ailabs-dev.azuredatabricks.net",
    "prod_url": "https://adb-bdl-ailabs-prod.azuredatabricks.net",
    "tags": ["ailabs", "ml", "ai"],
    "genies": [
        {"name": "ml-ops-genie", "title": "ML Ops Genie", "description": "AI agent for ML Ops - model health, latency, errors, drift.", "domain": "mlops"},
        {"name": "experiment-genie", "title": "Experiment Genie", "description": "AI agent for Experiments - runs, metrics, hyperparameters.", "domain": "research"},
        {"name": "model-registry-genie", "title": "Model Registry Genie", "description": "AI agent for Model Registry - versions, lineage, approvals.", "domain": "registry"},
    ],
    "data_products": [
        {"name": "model-performance", "title": "Model Performance", "description": "Production model performance - accuracy, latency, errors.", "domain": "mlops", "sla": "Real-time", "consumers": "ML Engineers, SRE"},
        {"name": "experiment-tracker", "title": "Experiment Tracker", "description": "Experiment metadata - runs, parameters, metrics, artifacts.", "domain": "research", "sla": "Daily refresh", "consumers": "Data Scientists, ML Lead"},
        {"name": "feature-store", "title": "Feature Store", "description": "Feature store - definitions, freshness, usage, lineage.", "domain": "mlops", "sla": "Real-time", "consumers": "ML Engineers, Data Scientists"},
        {"name": "inference-metrics", "title": "Inference Metrics", "description": "Inference metrics - requests/sec, p50/p99 latency, errors.", "domain": "mlops", "sla": "Real-time", "consumers": "SRE, ML Engineers"},
        {"name": "data-drift", "title": "Data Drift", "description": "Data drift detection - distributions, PSI, alerts, retraining.", "domain": "mlops", "sla": "Daily refresh", "consumers": "ML Engineers, Data Scientists"},
    ],
    "dashboards": [
        {"name": "mlops-dashboard", "title": "MLOps Dashboard", "description": "ML Ops overview - model health, deployments, incidents.", "audience": "ML Lead, SRE, CTO"},
        {"name": "research-dashboard", "title": "Research Dashboard", "description": "Research progress - experiments, models, team velocity.", "audience": "Chief Scientist, Research Leads"},
    ],
}


# ============================================================
# GENERATOR FUNCTIONS
# ============================================================

def save_yaml(filepath, data):
    full_path = os.path.join(BASE_DIR, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    print(f"  + {filepath}")


def generate_workspaces():
    print("\n" + "=" * 50)
    print("GENERATING WORKSPACES")
    print("=" * 50)
    count = 0
    for sys_id, sys_info in SYSTEMS.items():
        for env in ["dev", "prod"]:
            url = sys_info["dev_url"] if env == "dev" else sys_info["prod_url"]
            env_label = "Development" if env == "dev" else "Production"
            entity = {
                "apiVersion": "backstage.io/v1alpha1",
                "kind": "Resource",
                "metadata": {
                    "name": f"{sys_id}-{env}-workspace",
                    "title": f"{sys_info['title']} - {env_label} Workspace",
                    "description": f"{env_label} Databricks workspace for {sys_info['title']}. {sys_info['description']}.",
                    "tags": ["databricks", "workspace", env] + sys_info["tags"][:2],
                    "annotations": {"adani.com/business": sys_id, "adani.com/environment": env},
                    "links": [{"url": url, "title": f"Open {env_label} Workspace", "icon": "dashboard"}],
                },
                "spec": {
                    "type": "databricks-workspace",
                    "owner": sys_info["team"],
                    "system": sys_id,
                },
            }
            save_yaml(f"workspaces/{sys_id}-{env}.yaml", entity)
            count += 1
    print(f"\n  Total workspaces: {count}")
    return count


def generate_genies():
    print("\n" + "=" * 50)
    print("GENERATING GENIES")
    print("=" * 50)
    count = 0
    for sys_id, sys_info in SYSTEMS.items():
        for env in ["dev", "prod"]:
            url = sys_info["dev_url"] if env == "dev" else sys_info["prod_url"]
            env_label = "Development" if env == "dev" else "Production"
            lifecycle = "development" if env == "dev" else "production"
            for genie in sys_info["genies"]:
                entity = {
                    "apiVersion": "backstage.io/v1alpha1",
                    "kind": "Component",
                    "metadata": {
                        "name": f"{sys_id}-{env}-{genie['name']}",
                        "title": f"{genie['title']} ({sys_info['title_short']} - {env.capitalize()})",
                        "description": f"{genie['description']}\nBusiness: {sys_info['title']} | Environment: {env_label}",
                        "tags": ["genie", "ai-agent", env] + sys_info["tags"][:2] + [genie["domain"]],
                        "annotations": {"adani.com/business": sys_id, "adani.com/environment": env, "adani.com/component-type": "genie", "adani.com/domain": genie["domain"]},
                        "links": [{"url": f"{url}/genie", "title": f"Open Genie in {env_label} Workspace", "icon": "dashboard"}],
                    },
                    "spec": {
                        "type": "genie",
                        "lifecycle": lifecycle,
                        "owner": sys_info["team"],
                        "system": sys_id,
                        "dependsOn": [f"resource:{sys_id}-{env}-workspace"],
                    },
                }
                save_yaml(f"genies/{sys_id}/{env}/{genie['name']}.yaml", entity)
                count += 1
    print(f"\n  Total genies: {count}")
    return count


def generate_data_products():
    print("\n" + "=" * 50)
    print("GENERATING DATA PRODUCTS")
    print("=" * 50)
    count = 0
    for sys_id, sys_info in SYSTEMS.items():
        for env in ["dev", "prod"]:
            url = sys_info["dev_url"] if env == "dev" else sys_info["prod_url"]
            env_label = "Development" if env == "dev" else "Production"
            lifecycle = "development" if env == "dev" else "production"
            for dp in sys_info["data_products"]:
                entity = {
                    "apiVersion": "backstage.io/v1alpha1",
                    "kind": "Component",
                    "metadata": {
                        "name": f"{sys_id}-{env}-{dp['name']}",
                        "title": f"{dp['title']} ({sys_info['title_short']} - {env.capitalize()})",
                        "description": f"{dp['description']}\nConsumers: {dp['consumers']}\nBusiness: {sys_info['title']} | Environment: {env_label}",
                        "tags": ["data-product", env] + sys_info["tags"][:2] + [dp["domain"]],
                        "annotations": {"adani.com/business": sys_id, "adani.com/environment": env, "adani.com/component-type": "data-product", "adani.com/sla": dp["sla"]},
                        "links": [{"url": f"{url}/explore/data", "title": f"View in {env_label} Workspace", "icon": "dashboard"}],
                    },
                    "spec": {
                        "type": "data-product",
                        "lifecycle": lifecycle,
                        "owner": sys_info["team"],
                        "system": sys_id,
                        "dependsOn": [f"resource:{sys_id}-{env}-workspace"],
                    },
                }
                save_yaml(f"data-products/{sys_id}/{env}/{dp['name']}.yaml", entity)
                count += 1
    print(f"\n  Total data products: {count}")
    return count


def generate_dashboards():
    print("\n" + "=" * 50)
    print("GENERATING DASHBOARDS")
    print("=" * 50)
    count = 0
    for sys_id, sys_info in SYSTEMS.items():
        for env in ["dev", "prod"]:
            url = sys_info["dev_url"] if env == "dev" else sys_info["prod_url"]
            env_label = "Development" if env == "dev" else "Production"
            lifecycle = "development" if env == "dev" else "production"
            for db in sys_info["dashboards"]:
                entity = {
                    "apiVersion": "backstage.io/v1alpha1",
                    "kind": "Component",
                    "metadata": {
                        "name": f"{sys_id}-{env}-{db['name']}",
                        "title": f"{db['title']} ({sys_info['title_short']} - {env.capitalize()})",
                        "description": f"{db['description']}\nAudience: {db['audience']}\nBusiness: {sys_info['title']} | Environment: {env_label}",
                        "tags": ["dashboard", env] + sys_info["tags"][:2] + ["reporting"],
                        "annotations": {"adani.com/business": sys_id, "adani.com/environment": env, "adani.com/component-type": "dashboard", "adani.com/audience": db["audience"]},
                        "links": [{"url": f"{url}/sql/dashboards", "title": f"Open Dashboard in {env_label} Workspace", "icon": "dashboard"}],
                    },
                    "spec": {
                        "type": "dashboard",
                        "lifecycle": lifecycle,
                        "owner": sys_info["team"],
                        "system": sys_id,
                        "dependsOn": [f"resource:{sys_id}-{env}-workspace"],
                    },
                }
                save_yaml(f"dashboards/{sys_id}/{env}/{db['name']}.yaml", entity)
                count += 1
    print(f"\n  Total dashboards: {count}")
    return count


def main():
    print("=" * 60)
    print("ADANI DATA PLATFORM - BACKSTAGE CATALOG GENERATOR")
    print("=" * 60)
    print(f"  Systems:       {len(SYSTEMS)}")
    print(f"  Environments:  2 (Dev + Prod)")
    print(f"  Time:          {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Output:        {BASE_DIR}")

    w = generate_workspaces()
    g = generate_genies()
    d = generate_data_products()
    b = generate_dashboards()

    total = w + g + d + b

    print("\n" + "=" * 60)
    print("GENERATION COMPLETE!")
    print("=" * 60)
    print(f"  Workspaces:     {w}")
    print(f"  Genies:         {g}")
    print(f"  Data Products:  {d}")
    print(f"  Dashboards:     {b}")
    print(f"  TOTAL FILES:    {total}")
    print(f"\nNext steps:")
    print(f"  1. git add .")
    print(f'  2. git commit -m "Generated {total} catalog files for 8 business systems"')
    print(f"  3. git push origin main")
    print(f"  4. Register in Backstage:")
    print(f"     URL: https://github.com/yogeshahuja-dev/adani-data-platform/blob/main/catalog-info.yaml")


if __name__ == "__main__":
    main()