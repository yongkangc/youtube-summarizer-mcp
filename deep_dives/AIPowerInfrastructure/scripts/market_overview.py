#!/usr/bin/env python3
"""
AI Power Infrastructure Market Overview
Grid bottleneck analysis, demand surge, and opportunity cost calculations
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Grid bottleneck data - ERCOT example (2024-2025)
grid_bottleneck = {
    "ercot_monthly_requests_gw": {
        "Jan 2024": 15,
        "Apr 2024": 22,
        "Jul 2024": 35,
        "Oct 2024": 48,
        "Jan 2025": 55,
        "Apr 2025": 62,
        "Jul 2025": 70,
        "Oct 2025": 78
    },
    "ercot_monthly_approved_gw": {
        "Jan 2024": 0.3,
        "Apr 2024": 0.4,
        "Jul 2024": 0.5,
        "Oct 2024": 0.6,
        "Jan 2025": 0.7,
        "Apr 2025": 0.8,
        "Jul 2025": 0.9,
        "Oct 2025": 1.1
    },
    "notes": "Source: ERCOT Large Flexible Load Task Force (LFLTF) 2024-2025"
}

# Interconnection timeline by generation type (years)
interconnection_timelines = {
    "generation_type": ["Solar", "Wind", "Battery Storage", "Natural Gas (Grid)", "Onsite Gas", "Nuclear SMR"],
    "avg_years_to_power": [5.2, 4.8, 4.5, 4.0, 0.5, 8.0],
    "range_low": [3.5, 3.0, 3.0, 2.5, 0.25, 6.0],
    "range_high": [7.0, 6.5, 6.0, 6.0, 1.5, 12.0],
    "notes": "Lawrence Berkeley National Lab, SemiAnalysis estimates"
}

# AI power demand growth (GW)
ai_power_demand = {
    "year": [2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030],
    "us_ai_datacenter_gw": [3, 8, 15, 28, 45, 65, 85, 110],
    "global_ai_datacenter_gw": [8, 20, 40, 75, 120, 175, 230, 300],
    "notes": "SemiAnalysis AI Datacenter Energy Dilemma projections"
}

# Opportunity cost analysis
opportunity_cost = {
    "revenue_per_mw_annual": 11_000_000,  # $11M per MW per year
    "datacenter_sizes_mw": [100, 200, 500, 1000],
    "delay_months": [6, 12, 18, 24, 36],
    "notes": "Based on AI cloud revenue estimates"
}

# Major BYOG deployments
major_deployments = {
    "xAI Colossus 1": {"mw": 150, "location": "Memphis, TN", "year": 2024, "provider": "Solaris/VoltaGrid"},
    "xAI Colossus 2": {"mw": 500, "location": "Memphis, TN", "year": 2025, "provider": "Solaris/Doosan"},
    "Oracle/Crusoe Abilene": {"mw": 2300, "location": "Abilene, TX", "year": 2025, "provider": "GEV/Solar Turbines"},
    "Meta New Albany": {"mw": 400, "location": "Ohio", "year": 2025, "provider": "Williams/Mixed"},
    "Vantage Shackelford": {"mw": 2300, "location": "Shackelford, TX", "year": 2026, "provider": "VoltaGrid"}
}


def save_data():
    """Save market data to JSON"""
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    with open(data_dir / "grid_bottleneck.json", "w") as f:
        json.dump(grid_bottleneck, f, indent=2)

    with open(data_dir / "interconnection_timelines.json", "w") as f:
        json.dump(interconnection_timelines, f, indent=2)

    with open(data_dir / "ai_power_demand.json", "w") as f:
        json.dump(ai_power_demand, f, indent=2)

    with open(data_dir / "opportunity_cost.json", "w") as f:
        json.dump(opportunity_cost, f, indent=2)

    with open(data_dir / "major_deployments.json", "w") as f:
        json.dump(major_deployments, f, indent=2)

    print(f"Saved market overview data to {data_dir}")


def plot_grid_bottleneck():
    """Plot ERCOT load requests vs approvals"""
    fig, ax = plt.subplots(figsize=(14, 8))

    months = list(grid_bottleneck["ercot_monthly_requests_gw"].keys())
    requests = list(grid_bottleneck["ercot_monthly_requests_gw"].values())
    approved = list(grid_bottleneck["ercot_monthly_approved_gw"].values())

    x = np.arange(len(months))
    width = 0.35

    bars1 = ax.bar(x - width/2, requests, width, label='Load Requests (GW)',
                   color='#e74c3c', alpha=0.9, edgecolor='black')
    bars2 = ax.bar(x + width/2, approved, width, label='Approved (GW)',
                   color='#27ae60', alpha=0.9, edgecolor='black')

    # Add value labels
    for bar in bars1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{height:.0f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

    for bar in bars2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{height:.1f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax.set_xlabel('Month', fontsize=12, fontweight='bold')
    ax.set_ylabel('Gigawatts (GW)', fontsize=12, fontweight='bold')
    ax.set_title('ERCOT Datacenter Load: Requests vs Approvals\n(The Grid is Sold Out)',
                fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(months, rotation=45, ha='right')
    ax.legend(loc='upper left', fontsize=11)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    # Add annotation
    ax.annotate('78 GW requested\nvs 1.1 GW approved\n(70:1 ratio!)',
               xy=(7, 78), xytext=(5, 60),
               fontsize=11, fontweight='bold',
               arrowprops=dict(arrowstyle='->', color='red', lw=2),
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    charts_dir.mkdir(exist_ok=True)
    plt.savefig(charts_dir / "01_grid_bottleneck.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 01_grid_bottleneck.png")
    plt.close()


def plot_interconnection_timeline():
    """Plot years to power by generation type"""
    fig, ax = plt.subplots(figsize=(12, 8))

    types = interconnection_timelines["generation_type"]
    avg_years = interconnection_timelines["avg_years_to_power"]
    low = interconnection_timelines["range_low"]
    high = interconnection_timelines["range_high"]

    # Calculate error bars
    yerr_low = [avg - l for avg, l in zip(avg_years, low)]
    yerr_high = [h - avg for avg, h in zip(avg_years, high)]

    colors = ['#f39c12', '#3498db', '#9b59b6', '#e74c3c', '#27ae60', '#1abc9c']

    bars = ax.barh(types, avg_years, xerr=[yerr_low, yerr_high],
                   color=colors, alpha=0.85, edgecolor='black', linewidth=1.5,
                   capsize=5, error_kw={'lw': 2})

    # Highlight onsite gas
    bars[4].set_edgecolor('gold')
    bars[4].set_linewidth(3)

    for bar, val in zip(bars, avg_years):
        width = bar.get_width()
        ax.text(width + 0.5, bar.get_y() + bar.get_height()/2.,
               f'{val:.1f} years', ha='left', va='center',
               fontsize=11, fontweight='bold')

    ax.set_xlabel('Years to Commercial Operation', fontsize=12, fontweight='bold')
    ax.set_title('Interconnection Timeline by Generation Type\n(Onsite Gas = 6 months vs 5+ years for grid)',
                fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.set_xlim(0, 14)

    # Add annotation
    ax.annotate('BYOG: Deploy in months,\nnot years!',
               xy=(0.5, 4), xytext=(3, 3),
               fontsize=11, fontweight='bold',
               arrowprops=dict(arrowstyle='->', color='green', lw=2),
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.9))

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "02_interconnection_timeline.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 02_interconnection_timeline.png")
    plt.close()


def plot_ai_power_demand():
    """Plot AI datacenter power demand growth"""
    fig, ax = plt.subplots(figsize=(14, 8))

    years = ai_power_demand["year"]
    us_demand = ai_power_demand["us_ai_datacenter_gw"]
    global_demand = ai_power_demand["global_ai_datacenter_gw"]

    ax.fill_between(years, 0, global_demand, alpha=0.3, color='#3498db', label='Global AI Datacenter')
    ax.fill_between(years, 0, us_demand, alpha=0.6, color='#e74c3c', label='US AI Datacenter')

    ax.plot(years, global_demand, marker='o', linewidth=3, markersize=10, color='#3498db')
    ax.plot(years, us_demand, marker='s', linewidth=3, markersize=10, color='#e74c3c')

    for i, (y, us, gl) in enumerate(zip(years, us_demand, global_demand)):
        ax.text(y, gl + 8, f'{gl} GW', ha='center', fontsize=9, fontweight='bold', color='#3498db')
        ax.text(y, us + 5, f'{us} GW', ha='center', fontsize=9, fontweight='bold', color='#e74c3c')

    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('AI Datacenter Power Demand (GW)', fontsize=12, fontweight='bold')
    ax.set_title('AI Power Demand Explosion\n(US: 3 GW → 110 GW by 2030 = 37x growth)',
                fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper left', fontsize=11)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_ylim(0, 350)

    # Add CAGR annotation
    us_cagr = ((us_demand[-1] / us_demand[0]) ** (1/7) - 1) * 100
    ax.text(2027, 200, f'US AI Power CAGR: {us_cagr:.0f}%\n(Unprecedented growth)',
           fontsize=12, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "03_ai_power_demand.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 03_ai_power_demand.png")
    plt.close()


def plot_opportunity_cost():
    """Plot opportunity cost of waiting for grid power"""
    fig, ax = plt.subplots(figsize=(14, 8))

    rev_per_mw = opportunity_cost["revenue_per_mw_annual"]
    sizes = opportunity_cost["datacenter_sizes_mw"]
    delays = opportunity_cost["delay_months"]

    # Create heatmap data
    cost_matrix = np.zeros((len(sizes), len(delays)))
    for i, size in enumerate(sizes):
        for j, delay in enumerate(delays):
            # Lost revenue = size * revenue_per_mw * (delay_months / 12)
            cost_matrix[i, j] = (size * rev_per_mw * delay / 12) / 1e9  # Convert to billions

    im = ax.imshow(cost_matrix, cmap='Reds', aspect='auto')

    # Add labels
    ax.set_xticks(np.arange(len(delays)))
    ax.set_yticks(np.arange(len(sizes)))
    ax.set_xticklabels([f'{d} months' for d in delays])
    ax.set_yticklabels([f'{s} MW' for s in sizes])

    # Add value annotations
    for i in range(len(sizes)):
        for j in range(len(delays)):
            text = ax.text(j, i, f'${cost_matrix[i, j]:.1f}B',
                          ha='center', va='center', fontsize=11, fontweight='bold',
                          color='white' if cost_matrix[i, j] > 15 else 'black')

    ax.set_xlabel('Delay (Months Waiting for Grid)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Datacenter Size (MW)', fontsize=12, fontweight='bold')
    ax.set_title('Opportunity Cost of Waiting for Grid Power\n(Lost Revenue at $11M/MW/year)',
                fontsize=14, fontweight='bold', pad=20)

    # Add colorbar
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Lost Revenue ($ Billions)', fontsize=11, fontweight='bold')

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "04_opportunity_cost.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 04_opportunity_cost.png")
    plt.close()


if __name__ == "__main__":
    print("Generating market overview analysis...")
    save_data()
    plot_grid_bottleneck()
    plot_interconnection_timeline()
    plot_ai_power_demand()
    plot_opportunity_cost()
    print("\nMarket overview analysis complete!")
