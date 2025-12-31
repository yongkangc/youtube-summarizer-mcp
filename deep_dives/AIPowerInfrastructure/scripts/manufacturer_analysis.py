#!/usr/bin/env python3
"""
AI Power Infrastructure Manufacturer Analysis
Supplier positioning, order backlogs, production capacity
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Manufacturer data (2025 estimates)
manufacturer_data = {
    "GE Vernova": {
        "ticker": "GEV",
        "2025_datacenter_orders_mw": 5000,
        "total_backlog_billion": 135.3,
        "slot_reservations_gw": 62,
        "production_capacity_gw_year": 20,
        "planned_capacity_gw_year": 24,
        "capacity_year": 2026,
        "primary_products": ["LM2500 (34MW)", "LM6000 (57MW)", "HA.02 CCGT (600MW)"],
        "key_win": "29x LM2500XPRESS for Crusoe/OpenAI (July 2025)",
        "bull_case": "Blue chip BYOG play, massive backlog, pricing power",
        "notes": "Doubled dividend to $2/share, $10B buyback authorization"
    },
    "Bloom Energy": {
        "ticker": "BE",
        "2025_datacenter_orders_mw": 1500,
        "total_backlog_billion": 5.0,
        "slot_reservations_gw": 1.0,
        "production_capacity_gw_year": 1.0,
        "planned_capacity_gw_year": 2.0,
        "capacity_year": 2026,
        "primary_products": ["Energy Server (325kW modules)"],
        "key_win": "$5B Brookfield partnership (1GW for AI factories)",
        "bull_case": "Permitting arbitrage, fastest deployment, urban sites",
        "notes": "4 consecutive record revenue quarters, pivoted to profitability"
    },
    "Caterpillar (Solar)": {
        "ticker": "CAT",
        "2025_datacenter_orders_mw": 2000,
        "total_backlog_billion": 3.5,
        "slot_reservations_gw": 5,
        "production_capacity_gw_year": 1.2,
        "planned_capacity_gw_year": 3.0,
        "capacity_year": 2030,
        "primary_products": ["Titan 250 (23MW)", "Titan 130 (16.5MW)", "Jenbacher engines"],
        "key_win": "Multiple deployments via Solaris rental fleet",
        "bull_case": "Diversified exposure, rental fleet leverage, engine dominance",
        "notes": "Doubling engine production, 2.5x turbine production by 2030"
    },
    "Siemens Energy": {
        "ticker": "SMEGF",
        "2025_datacenter_orders_mw": 3000,
        "total_backlog_billion": 45.0,
        "slot_reservations_gw": 30,
        "production_capacity_gw_year": 20,
        "planned_capacity_gw_year": 30,
        "capacity_year": 2030,
        "primary_products": ["SGT-800 (61MW)", "SGT5-8000H CCGT (600MW)"],
        "key_win": "Meta New Albany deployment (SGT-400s)",
        "bull_case": "European champion, diversified portfolio, service revenue",
        "notes": "Investing in production without increasing factory footprint"
    },
    "Wärtsilä": {
        "ticker": "WRTBY",
        "2025_datacenter_orders_mw": 800,
        "total_backlog_billion": 2.5,
        "slot_reservations_gw": 3,
        "production_capacity_gw_year": 2.0,
        "planned_capacity_gw_year": 2.5,
        "capacity_year": 2027,
        "primary_products": ["34SG engine (11MW)", "50SG engine (18MW)"],
        "key_win": "800MW US datacenter contracts (2025)",
        "bull_case": "Marine-to-datacenter pivot, medium-speed engine leader",
        "notes": "Incremental expansion, 'wait and see' approach"
    },
    "Howmet Aerospace": {
        "ticker": "HWM",
        "2025_datacenter_orders_mw": 0,  # Not a generator OEM
        "total_backlog_billion": 8.5,
        "slot_reservations_gw": 0,
        "production_capacity_gw_year": 0,
        "planned_capacity_gw_year": 0,
        "capacity_year": 0,
        "primary_products": ["Single-crystal nickel turbine blades", "Vanes", "Hot section castings"],
        "key_win": "Monopoly on high-temp alloy castings for GE/Siemens/MHI",
        "bull_case": "Hidden monopoly - every turbine needs Howmet blades",
        "notes": "The 'NVIDIA of turbine blades' - supply chain bottleneck"
    },
    "Boom Supersonic": {
        "ticker": "PRIVATE",
        "2025_datacenter_orders_mw": 1200,
        "total_backlog_billion": 1.2,
        "slot_reservations_gw": 2,
        "production_capacity_gw_year": 0.2,
        "planned_capacity_gw_year": 2.0,
        "capacity_year": 2028,
        "primary_products": ["Superpower (42MW aeroderivative)"],
        "key_win": "1.2 GW contract with Crusoe",
        "bull_case": "New entrant with jet engine tech, aggressive capacity ramp",
        "notes": "Using datacenter margins to fund Mach 2 passenger jets"
    },
    "Doosan Enerbility": {
        "ticker": "034020.KS",
        "2025_datacenter_orders_mw": 1900,
        "total_backlog_billion": 12.0,
        "slot_reservations_gw": 8,
        "production_capacity_gw_year": 5,
        "planned_capacity_gw_year": 10,
        "capacity_year": 2027,
        "primary_products": ["DGT6 H-class (400MW)", "Steam turbines"],
        "key_win": "1.9 GW xAI Colossus 2 order",
        "bull_case": "Korean champion, new H-class entrant, aggressive expansion",
        "notes": "Timing H-class launch perfectly for AI demand surge"
    }
}

# Solaris Energy Infrastructure (rental fleet)
solaris_data = {
    "ticker": "SEI",
    "business_model": "Energy-as-a-Service / Rental Fleet",
    "fleet_capacity_mw": 500,
    "utilization_rate": 0.85,
    "key_customers": ["xAI", "Oracle", "Meta"],
    "short_interest_pct": 30,
    "bull_case": "Short squeeze candidate, captures emergency capex from hyperscalers",
    "notes": "Provides Solar Titan/Saturn turbines on rental basis"
}


def save_data():
    """Save manufacturer data to JSON"""
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    with open(data_dir / "manufacturer_data.json", "w") as f:
        json.dump(manufacturer_data, f, indent=2)

    with open(data_dir / "solaris_data.json", "w") as f:
        json.dump(solaris_data, f, indent=2)

    print(f"Saved manufacturer data to {data_dir}")


def plot_manufacturer_market_share():
    """Plot datacenter order market share by manufacturer"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Filter to manufacturers with datacenter orders
    mfrs = [m for m in manufacturer_data.keys() if manufacturer_data[m]["2025_datacenter_orders_mw"] > 0]
    orders = [manufacturer_data[m]["2025_datacenter_orders_mw"] for m in mfrs]

    # Sort by orders
    sorted_data = sorted(zip(mfrs, orders), key=lambda x: x[1], reverse=True)
    mfrs = [m for m, o in sorted_data]
    orders = [o for m, o in sorted_data]

    colors = plt.cm.Set3(np.linspace(0, 1, len(mfrs)))
    bars = ax.barh(mfrs, orders, color=colors, alpha=0.9, edgecolor='black', linewidth=1.5)

    for bar, val in zip(bars, orders):
        width = bar.get_width()
        ax.text(width + 50, bar.get_y() + bar.get_height()/2.,
               f'{val:,} MW', ha='left', va='center', fontsize=11, fontweight='bold')

    total = sum(orders)
    ax.set_xlabel('2025 Datacenter Orders (MW)', fontsize=12, fontweight='bold')
    ax.set_title(f'AI Power Infrastructure Market Share by Manufacturer\n(Total: {total:,} MW in 2025 orders)',
                fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3, linestyle='--')

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    charts_dir.mkdir(exist_ok=True)
    plt.savefig(charts_dir / "09_manufacturer_market_share.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 09_manufacturer_market_share.png")
    plt.close()


def plot_order_backlog():
    """Plot total order backlog by manufacturer"""
    fig, ax = plt.subplots(figsize=(14, 8))

    mfrs = list(manufacturer_data.keys())
    backlogs = [manufacturer_data[m]["total_backlog_billion"] for m in mfrs]

    # Sort by backlog
    sorted_data = sorted(zip(mfrs, backlogs), key=lambda x: x[1], reverse=True)
    mfrs = [m for m, b in sorted_data]
    backlogs = [b for m, b in sorted_data]

    colors = ['#e74c3c', '#3498db', '#2ecc71', '#9b59b6', '#f39c12', '#1abc9c', '#e67e22', '#34495e']
    bars = ax.bar(mfrs, backlogs, color=colors[:len(mfrs)], alpha=0.9, edgecolor='black', linewidth=1.5)

    for bar, val in zip(bars, backlogs):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'${val:.1f}B', ha='center', va='bottom', fontsize=10, fontweight='bold')

    ax.set_ylabel('Total Backlog ($ Billions)', fontsize=12, fontweight='bold')
    ax.set_title('Order Backlog by Manufacturer\n(GE Vernova dominates with $135B)',
                fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    plt.xticks(rotation=30, ha='right')

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "10_order_backlog.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 10_order_backlog.png")
    plt.close()


def plot_production_capacity():
    """Plot current vs planned production capacity"""
    fig, ax = plt.subplots(figsize=(14, 8))

    # Filter to generator OEMs only
    mfrs = [m for m in manufacturer_data.keys()
            if manufacturer_data[m]["production_capacity_gw_year"] > 0]
    current = [manufacturer_data[m]["production_capacity_gw_year"] for m in mfrs]
    planned = [manufacturer_data[m]["planned_capacity_gw_year"] for m in mfrs]

    x = np.arange(len(mfrs))
    width = 0.35

    bars1 = ax.bar(x - width/2, current, width, label='Current Capacity (GW/year)',
                   color='#3498db', alpha=0.9, edgecolor='black')
    bars2 = ax.bar(x + width/2, planned, width, label='Planned Capacity (GW/year)',
                   color='#2ecc71', alpha=0.9, edgecolor='black')

    for bar, val in zip(bars1, current):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{val:.1f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

    for bar, val in zip(bars2, planned):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{val:.1f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax.set_ylabel('Production Capacity (GW/year)', fontsize=12, fontweight='bold')
    ax.set_title('Manufacturing Capacity: Current vs Planned\n(Manufacturers ramping to meet AI demand)',
                fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(mfrs, rotation=30, ha='right')
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "11_production_capacity.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 11_production_capacity.png")
    plt.close()


def plot_investment_summary():
    """Create investment summary table"""
    fig, ax = plt.subplots(figsize=(18, 12))
    ax.axis('off')

    columns = ['Company', 'Ticker', 'Bull Case', 'Key Win', 'Risk']

    rows = []
    for mfr, data in manufacturer_data.items():
        risk = "Capacity constraints" if data["2025_datacenter_orders_mw"] > 0 else "Supply chain bottleneck"
        if mfr == "Bloom Energy":
            risk = "High CapEx, stack replacement costs"
        elif mfr == "Boom Supersonic":
            risk = "Execution risk (new entrant)"
        rows.append([
            mfr,
            data['ticker'],
            data['bull_case'][:50] + "..." if len(data['bull_case']) > 50 else data['bull_case'],
            data['key_win'][:45] + "..." if len(data['key_win']) > 45 else data['key_win'],
            risk
        ])

    table = ax.table(cellText=rows, colLabels=columns, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.2, 2.0)

    # Style
    for j in range(len(columns)):
        table[(0, j)].set_facecolor('#2c3e50')
        table[(0, j)].set_text_props(color='white', fontweight='bold')

    # Highlight key players
    highlight_colors = {
        0: '#d5f4e6',  # GE Vernova
        1: '#ffeaa7',  # Bloom
        5: '#fab1a0',  # Howmet (hidden monopoly)
    }
    for i in range(1, len(rows) + 1):
        color = highlight_colors.get(i-1, '#f8f9fa')
        for j in range(len(columns)):
            table[(i, j)].set_facecolor(color)

    ax.set_title('AI Power Infrastructure Investment Summary\n(Long-Only Focus)',
                fontsize=16, fontweight='bold', pad=20)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "12_investment_summary.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 12_investment_summary.png")
    plt.close()


if __name__ == "__main__":
    print("Generating manufacturer analysis...")
    save_data()
    plot_manufacturer_market_share()
    plot_order_backlog()
    plot_production_capacity()
    plot_investment_summary()
    print("\nManufacturer analysis complete!")
