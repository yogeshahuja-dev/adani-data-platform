"""
Creates all ATGL files for demo
"""
import os
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def save(filepath, data):
    full_path = os.path.join(BASE_DIR, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    print(f"  + {filepath}")

# System
save("systems/bdl-atgl.yaml", {
    "apiVersion": "backstage.io/v1alpha1",
    "kind": "System",
    "metadata": {
        "name": "bdl-atgl",
        "title": "BDL - Adani Total Gas (ATGL)",
        "description": "Business Data Lake for Adani Total Gas.\nDomains: Gas Distribution, Pipeline Operations, CNG Stations, PNG Connections.\nWorkspaces: Dev + Prod on Azure Databricks.",
        "tags": ["bdl", "atgl", "gas", "distribution", "pipeline"],
        "links": [
            {"url": "https://adb-bdl-atgl-dev.azuredatabricks.net", "title": "Dev Workspace", "icon": "dashboard"},
            {"url": "https://adb-bdl-atgl-prod.azuredatabricks.net", "title": "Prod Workspace", "icon": "dashboard"},
        ],
    },
    "spec": {"owner": "bdl-atgl-team"},
})

# Workspaces
for env in ["dev", "prod"]:
    env_label = "Development" if env == "dev" else "Production"
    url = f"https://adb-bdl-atgl-{env}.azuredatabricks.net"
    save(f"workspaces/bdl-atgl-{env}.yaml", {
        "apiVersion": "backstage.io/v1alpha1",
        "kind": "Resource",
        "metadata": {
            "name": f"bdl-atgl-{env}-workspace",
            "title": f"Adani Total Gas (ATGL) - {env_label} Workspace",
            "description": f"{env_label} Databricks workspace for Adani Total Gas.",
            "tags": ["databricks", "workspace", env, "atgl", "gas"],
            "annotations": {"adani.com/business": "bdl-atgl", "adani.com/environment": env},
            "links": [{"url": url, "title": f"Open {env_label} Workspace", "icon": "dashboard"}],
        },
        "spec": {"type": "databricks-workspace", "owner": "bdl-atgl-team", "system": "bdl-atgl"},
    })

# Genies
genies = [
    {"name": "pipeline-genie", "title": "Pipeline Genie", "domain": "pipeline", "desc": "AI agent for Pipeline Operations - flow rates, pressure, leak detection."},
    {"name": "cng-genie", "title": "CNG Genie", "domain": "cng", "desc": "AI agent for CNG Stations - dispensing volumes, station uptime, queues."},
    {"name": "png-genie", "title": "PNG Genie", "domain": "png", "desc": "AI agent for PNG Connections - new connections, billing, complaints."},
]

for env in ["dev", "prod"]:
    env_label = "Development" if env == "dev" else "Production"
    lifecycle = "development" if env == "dev" else "production"
    url = f"https://adb-bdl-atgl-{env}.azuredatabricks.net"
    for g in genies:
        save(f"genies/bdl-atgl/{env}/{g['name']}.yaml", {
            "apiVersion": "backstage.io/v1alpha1",
            "kind": "Component",
            "metadata": {
                "name": f"bdl-atgl-{env}-{g['name']}",
                "title": f"{g['title']} (ATGL - {env.capitalize()})",
                "description": f"{g['desc']}\nBusiness: Adani Total Gas | Environment: {env_label}",
                "tags": ["genie", "ai-agent", env, "atgl", "gas", g["domain"]],
                "annotations": {"adani.com/business": "bdl-atgl", "adani.com/environment": env, "adani.com/component-type": "genie", "adani.com/domain": g["domain"]},
                "links": [{"url": f"{url}/genie", "title": f"Open Genie in {env_label} Workspace", "icon": "dashboard"}],
            },
            "spec": {
                "type": "genie",
                "lifecycle": lifecycle,
                "owner": "bdl-atgl-team",
                "dependsOn": [f"resource:default/bdl-atgl-{env}-workspace"],
            },
        })

# Data Products
dps = [
    {"name": "gas-throughput", "title": "Gas Throughput", "domain": "operations", "sla": "Daily by 7 AM IST", "consumers": "Operations, Commercial", "desc": "Gas throughput analytics - volume by pipeline, city, customer segment."},
    {"name": "cng-station-metrics", "title": "CNG Station Metrics", "domain": "cng", "sla": "Real-time", "consumers": "Operations, Finance", "desc": "CNG station performance - dispensing volume, uptime, queue time, revenue."},
    {"name": "png-connections", "title": "PNG Connections", "domain": "png", "sla": "Daily by 8 AM IST", "consumers": "Sales, Operations", "desc": "PNG new connections - applications, installations, activations by city."},
    {"name": "pipeline-safety", "title": "Pipeline Safety", "domain": "safety", "sla": "Real-time", "consumers": "Safety Team, COO", "desc": "Pipeline safety metrics - leak incidents, pressure anomalies, inspections."},
    {"name": "billing-revenue", "title": "Billing Revenue", "domain": "finance", "sla": "Daily by 9 AM IST", "consumers": "CFO, Commercial", "desc": "Billing and revenue analytics - collections, outstanding, segment-wise revenue."},
]

for env in ["dev", "prod"]:
    env_label = "Development" if env == "dev" else "Production"
    lifecycle = "development" if env == "dev" else "production"
    url = f"https://adb-bdl-atgl-{env}.azuredatabricks.net"
    for dp in dps:
        save(f"data-products/bdl-atgl/{env}/{dp['name']}.yaml", {
            "apiVersion": "backstage.io/v1alpha1",
            "kind": "Component",
            "metadata": {
                "name": f"bdl-atgl-{env}-{dp['name']}",
                "title": f"{dp['title']} (ATGL - {env.capitalize()})",
                "description": f"{dp['desc']}\nConsumers: {dp['consumers']}\nBusiness: Adani Total Gas | Environment: {env_label}",
                "tags": ["data-product", env, "atgl", "gas", dp["domain"]],
                "annotations": {"adani.com/business": "bdl-atgl", "adani.com/environment": env, "adani.com/component-type": "data-product", "adani.com/sla": dp["sla"]},
                "links": [{"url": f"{url}/explore/data", "title": f"View in {env_label} Workspace", "icon": "dashboard"}],
            },
            "spec": {
                "type": "data-product",
                "lifecycle": lifecycle,
                "owner": "bdl-atgl-team",
                "dependsOn": [f"resource:default/bdl-atgl-{env}-workspace"],
            },
        })

# Dashboards
dashboards = [
    {"name": "gas-ops-dashboard", "title": "Gas Operations Dashboard", "audience": "COO, Operations", "desc": "Gas operations overview - pipeline flow, CNG stations, PNG connections."},
    {"name": "revenue-dashboard", "title": "Revenue Dashboard", "audience": "CFO, Commercial", "desc": "Revenue analytics - billing, collections, segment performance."},
]

for env in ["dev", "prod"]:
    env_label = "Development" if env == "dev" else "Production"
    lifecycle = "development" if env == "dev" else "production"
    url = f"https://adb-bdl-atgl-{env}.azuredatabricks.net"
    for db in dashboards:
        save(f"dashboards/bdl-atgl/{env}/{db['name']}.yaml", {
            "apiVersion": "backstage.io/v1alpha1",
            "kind": "Component",
            "metadata": {
                "name": f"bdl-atgl-{env}-{db['name']}",
                "title": f"{db['title']} (ATGL - {env.capitalize()})",
                "description": f"{db['desc']}\nAudience: {db['audience']}\nBusiness: Adani Total Gas | Environment: {env_label}",
                "tags": ["dashboard", env, "atgl", "gas", "reporting"],
                "annotations": {"adani.com/business": "bdl-atgl", "adani.com/environment": env, "adani.com/component-type": "dashboard", "adani.com/audience": db["audience"]},
                "links": [{"url": f"{url}/sql/dashboards", "title": f"Open Dashboard in {env_label} Workspace", "icon": "dashboard"}],
            },
            "spec": {
                "type": "dashboard",
                "lifecycle": lifecycle,
                "owner": "bdl-atgl-team",
                "dependsOn": [f"resource:default/bdl-atgl-{env}-workspace"],
            },
        })

# Org update file (separate so we don't break existing)
save("org/atgl-team.yaml", {
    "apiVersion": "backstage.io/v1alpha1",
    "kind": "Group",
    "metadata": {
        "name": "bdl-atgl-team",
        "description": "Adani Total Gas (ATGL) - Gas Distribution, Pipeline, CNG, PNG",
    },
    "spec": {"type": "team", "parent": "adani-group", "children": []},
})

# User file
save("org/ganesh.yaml", {
    "apiVersion": "backstage.io/v1alpha1",
    "kind": "User",
    "metadata": {
        "name": "ganesh-kumar",
        "annotations": {},
    },
    "spec": {
        "profile": {"displayName": "Ganesh Kumar", "email": "ganesh.kumar@adani.com"},
        "memberOf": ["bdl-atgl-team"],
    },
})

print("\n" + "=" * 50)
print("ATGL FILES CREATED!")
print("=" * 50)
print("  System: 1")
print("  Workspaces: 2")
print("  Genies: 6 (3 dev + 3 prod)")
print("  Data Products: 10 (5 dev + 5 prod)")
print("  Dashboards: 4 (2 dev + 2 prod)")
print("  Team: 1")
print("  User: 1")
print("  TOTAL: 25 files")