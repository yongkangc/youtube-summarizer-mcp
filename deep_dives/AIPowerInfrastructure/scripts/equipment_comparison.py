#!/usr/bin/env python3
"""
AI Power Infrastructure Equipment Comparison
Investment-focused technology overview: Aeros, IGTs, RICEs, Fuel Cells, CCGTs
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Technology comparison data (investment-focused summary)
technology_comparison = {
    "Aeroderivative Gas Turbine": {
        "example_products": ["GE LM2500 (34MW)", "GE LM6000 (57MW)", "MHI FT8 (30MW)"],
        "capex_per_kw_low": 1700,
        "capex_per_kw_high": 2000,
        "lead_time_months_low": 18,
        "lead_time_months_high": 36,
        "ramp_minutes": 10,
        "heat_rate_btu_kwh": 9500,
        "efficiency_pct": 36,
        "best_for": "Bridge power, fast deployment, backup conversion",
        "key_suppliers": ["GE Vernova", "Mitsubishi Power", "Siemens Energy", "Boom Supersonic"]
    },
    "Industrial Gas Turbine (IGT)": {
        "example_products": ["Solar Titan 250 (23MW)", "Solar Titan 130 (16.5MW)", "Siemens SGT-800 (61MW)"],
        "capex_per_kw_low": 1500,
        "capex_per_kw_high": 1800,
        "lead_time_months_low": 12,
        "lead_time_months_high": 36,
        "ramp_minutes": 20,
        "heat_rate_btu_kwh": 10000,
        "efficiency_pct": 34,
        "best_for": "Cost-effective baseload, modular deployment",
        "key_suppliers": ["Caterpillar (Solar)", "Siemens Energy", "GE Vernova"]
    },
    "Reciprocating Engine (RICE)": {
        "example_products": ["Jenbacher J624 (4.5MW)", "Wärtsilä 34SG (11MW)", "Bergen B36:45 (11MW)"],
        "capex_per_kw_low": 1700,
        "capex_per_kw_high": 2000,
        "lead_time_months_low": 15,
        "lead_time_months_high": 24,
        "ramp_minutes": 10,
        "heat_rate_btu_kwh": 8500,
        "efficiency_pct": 40,
        "best_for": "High redundancy (small units), flexible load, truck-mountable",
        "key_suppliers": ["INNIO (Jenbacher)", "Wärtsilä", "Caterpillar", "Bergen Engines"]
    },
    "Solid Oxide Fuel Cell (SOFC)": {
        "example_products": ["Bloom Energy Server (325kW modules)"],
        "capex_per_kw_low": 3000,
        "capex_per_kw_high": 4000,
        "lead_time_months_low": 3,
        "lead_time_months_high": 12,
        "ramp_minutes": 60,
        "heat_rate_btu_kwh": 6500,
        "efficiency_pct": 52,
        "best_for": "Urban sites (no combustion = easy permitting), speed to power",
        "key_suppliers": ["Bloom Energy"]
    },
    "Heavy-Duty CCGT (H-Class)": {
        "example_products": ["GE HA.02 (600MW)", "Siemens H/HL (500-600MW)", "Doosan DGT6 (400MW)"],
        "capex_per_kw_low": 800,
        "capex_per_kw_high": 1200,
        "lead_time_months_low": 24,
        "lead_time_months_high": 36,
        "ramp_minutes": 60,
        "heat_rate_btu_kwh": 6000,
        "efficiency_pct": 62,
        "best_for": "Large permanent installations, lowest $/MWh at scale",
        "key_suppliers": ["GE Vernova", "Siemens Energy", "Mitsubishi Power", "Doosan Enerbility"]
    }
}

# Use case mapping
use_case_mapping = {
    "Bridge Power (6-18 months)": {
        "winner": "Aeroderivative Gas Turbine",
        "runner_up": "Reciprocating Engine (RICE)",
        "reason": "Fast deployment, can convert to backup later"
    },
    "Permanent Islanded (GW-scale)": {
        "winner": "Heavy-Duty CCGT (H-Class)",
        "runner_up": "Industrial Gas Turbine (IGT)",
        "reason": "Lowest TCO at scale, highest efficiency"
    },
    "Urban / Permitting-Constrained": {
        "winner": "Solid Oxide Fuel Cell (SOFC)",
        "runner_up": "Reciprocating Engine (RICE)",
        "reason": "No combustion = no air permitting delays"
    },
    "High Redundancy (N+1+1)": {
        "winner": "Reciprocating Engine (RICE)",
        "runner_up": "Industrial Gas Turbine (IGT)",
        "reason": "Small units enable flexible redundancy"
    },
    "Emergency / Rental": {
        "winner": "Aeroderivative Gas Turbine",
        "runner_up": "Reciprocating Engine (RICE)",
        "reason": "Truck-mountable, available from rental fleets"
    }
}

# Manufacturer-technology mapping
manufacturer_technology_map = {
    "GE Vernova": ["Aeroderivative Gas Turbine", "Heavy-Duty CCGT (H-Class)", "Industrial Gas Turbine (IGT)"],
    "Siemens Energy": ["Aeroderivative Gas Turbine", "Heavy-Duty CCGT (H-Class)", "Industrial Gas Turbine (IGT)"],
    "Caterpillar (Solar/CAT)": ["Industrial Gas Turbine (IGT)", "Reciprocating Engine (RICE)"],
    "Bloom Energy": ["Solid Oxide Fuel Cell (SOFC)"],
    "Wärtsilä": ["Reciprocating Engine (RICE)"],
    "INNIO (Jenbacher)": ["Reciprocating Engine (RICE)"],
    "Mitsubishi Power": ["Aeroderivative Gas Turbine", "Heavy-Duty CCGT (H-Class)"],
    "Doosan Enerbility": ["Heavy-Duty CCGT (H-Class)"],
    "Boom Supersonic": ["Aeroderivative Gas Turbine"]
}


def save_data():
    """Save equipment data to JSON"""
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    with open(data_dir / "technology_comparison.json", "w") as f:
        json.dump(technology_comparison, f, indent=2)

    with open(data_dir / "use_case_mapping.json", "w") as f:
        json.dump(use_case_mapping, f, indent=2)

    with open(data_dir / "manufacturer_technology_map.json", "w") as f:
        json.dump(manufacturer_technology_map, f, indent=2)

    print(f"Saved equipment comparison data to {data_dir}")


def plot_technology_comparison_table():
    """Create visual comparison table"""
    fig, ax = plt.subplots(figsize=(18, 10))
    ax.axis('off')

    # Table data
    columns = ['Technology', 'CapEx\n($/kW)', 'Lead Time\n(months)', 'Ramp\n(min)',
               'Efficiency', 'Best For']

    rows = []
    for tech, data in technology_comparison.items():
        rows.append([
            tech.replace(" Gas Turbine", "\nGas Turbine").replace(" (IGT)", "\n(IGT)").replace(" (RICE)", "\n(RICE)").replace(" (SOFC)", "\n(SOFC)").replace(" (H-Class)", "\n(H-Class)"),
            f"${data['capex_per_kw_low']:,}-{data['capex_per_kw_high']:,}",
            f"{data['lead_time_months_low']}-{data['lead_time_months_high']}",
            f"{data['ramp_minutes']}",
            f"{data['efficiency_pct']}%",
            data['best_for'][:40] + "..." if len(data['best_for']) > 40 else data['best_for']
        ])

    table = ax.table(cellText=rows, colLabels=columns, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 2.5)

    # Style table
    for j in range(len(columns)):
        table[(0, j)].set_facecolor('#2c3e50')
        table[(0, j)].set_text_props(color='white', fontweight='bold')

    # Color rows by technology type
    colors = ['#d5f4e6', '#ffeaa7', '#dfe6e9', '#fab1a0', '#74b9ff']
    for i in range(1, len(rows) + 1):
        for j in range(len(columns)):
            table[(i, j)].set_facecolor(colors[i-1])

    ax.set_title('BYOG Technology Comparison Matrix\n(Investment-Focused Summary)',
                fontsize=16, fontweight='bold', pad=20)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    charts_dir.mkdir(exist_ok=True)
    plt.savefig(charts_dir / "05_technology_comparison_table.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 05_technology_comparison_table.png")
    plt.close()


def plot_cost_vs_speed_scatter():
    """Scatter plot of CapEx vs deployment speed"""
    fig, ax = plt.subplots(figsize=(12, 8))

    techs = list(technology_comparison.keys())
    capex_avg = [(technology_comparison[t]["capex_per_kw_low"] + technology_comparison[t]["capex_per_kw_high"]) / 2
                 for t in techs]
    lead_time_avg = [(technology_comparison[t]["lead_time_months_low"] + technology_comparison[t]["lead_time_months_high"]) / 2
                     for t in techs]
    efficiency = [technology_comparison[t]["efficiency_pct"] for t in techs]

    colors = ['#3498db', '#2ecc71', '#e74c3c', '#9b59b6', '#f39c12']
    sizes = [e * 10 for e in efficiency]  # Size by efficiency

    for i, (tech, x, y, c, s) in enumerate(zip(techs, lead_time_avg, capex_avg, colors, sizes)):
        ax.scatter(x, y, s=s*3, c=c, alpha=0.7, edgecolors='black', linewidth=2, label=tech)
        # Add efficiency label
        ax.annotate(f'{efficiency[i]}% eff', (x, y), textcoords="offset points",
                   xytext=(0, 15), ha='center', fontsize=9, fontweight='bold')

    ax.set_xlabel('Lead Time (Months)', fontsize=12, fontweight='bold')
    ax.set_ylabel('CapEx ($/kW)', fontsize=12, fontweight='bold')
    ax.set_title('Cost vs Speed Tradeoff\n(Bubble size = Efficiency)',
                fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, alpha=0.3, linestyle='--')

    # Add quadrant labels
    ax.axhline(y=2000, color='gray', linestyle='--', alpha=0.5)
    ax.axvline(x=18, color='gray', linestyle='--', alpha=0.5)
    ax.text(8, 3800, 'FAST + EXPENSIVE\n(Bloom)', ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    ax.text(8, 1000, 'FAST + CHEAP\n(Sweet Spot)', ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    ax.text(30, 3800, 'SLOW + EXPENSIVE\n(Avoid)', ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))
    ax.text(30, 1000, 'SLOW + CHEAP\n(CCGT)', ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "06_cost_vs_speed_scatter.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 06_cost_vs_speed_scatter.png")
    plt.close()


def plot_use_cases():
    """Plot best technology by use case"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.axis('off')

    # Table data
    columns = ['Use Case', 'Best Technology', 'Runner-Up', 'Key Reason']
    rows = []
    for use_case, data in use_case_mapping.items():
        rows.append([
            use_case,
            data['winner'].replace(" Gas Turbine", "").replace(" (H-Class)", ""),
            data['runner_up'].replace(" Gas Turbine", "").replace(" (H-Class)", ""),
            data['reason']
        ])

    table = ax.table(cellText=rows, colLabels=columns, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.2, 2.2)

    # Style
    for j in range(len(columns)):
        table[(0, j)].set_facecolor('#2c3e50')
        table[(0, j)].set_text_props(color='white', fontweight='bold')

    for i in range(1, len(rows) + 1):
        table[(i, 0)].set_facecolor('#ecf0f1')
        table[(i, 1)].set_facecolor('#d5f4e6')  # Winner - green
        table[(i, 2)].set_facecolor('#ffeaa7')  # Runner-up - yellow
        table[(i, 3)].set_facecolor('#f8f9fa')

    ax.set_title('Technology Selection by Use Case\n(Match Technology to Your Deployment Scenario)',
                fontsize=16, fontweight='bold', pad=20)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "07_technology_use_cases.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 07_technology_use_cases.png")
    plt.close()


def plot_manufacturer_technology_map():
    """Create visual map of manufacturers to technologies"""
    fig, ax = plt.subplots(figsize=(16, 10))

    manufacturers = list(manufacturer_technology_map.keys())
    technologies = list(technology_comparison.keys())

    # Create matrix
    matrix = np.zeros((len(manufacturers), len(technologies)))
    for i, mfr in enumerate(manufacturers):
        for j, tech in enumerate(technologies):
            if tech in manufacturer_technology_map[mfr]:
                matrix[i, j] = 1

    # Plot heatmap
    im = ax.imshow(matrix, cmap='Greens', aspect='auto')

    ax.set_xticks(np.arange(len(technologies)))
    ax.set_yticks(np.arange(len(manufacturers)))

    # Shorten technology names
    tech_labels = [t.replace(" Gas Turbine", "").replace(" (H-Class)", "") for t in technologies]
    ax.set_xticklabels(tech_labels, rotation=45, ha='right', fontsize=10)
    ax.set_yticklabels(manufacturers, fontsize=10)

    # Add checkmarks
    for i in range(len(manufacturers)):
        for j in range(len(technologies)):
            if matrix[i, j] == 1:
                ax.text(j, i, '✓', ha='center', va='center',
                       fontsize=20, fontweight='bold', color='darkgreen')

    ax.set_title('Manufacturer-Technology Matrix\n(Who Makes What)',
                fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "08_manufacturer_technology_map.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 08_manufacturer_technology_map.png")
    plt.close()


if __name__ == "__main__":
    print("Generating equipment comparison analysis...")
    save_data()
    plot_technology_comparison_table()
    plot_cost_vs_speed_scatter()
    plot_use_cases()
    plot_manufacturer_technology_map()
    print("\nEquipment comparison analysis complete!")
