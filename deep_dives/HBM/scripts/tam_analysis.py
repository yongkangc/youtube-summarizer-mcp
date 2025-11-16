#!/usr/bin/env python3
"""
HBM Total Addressable Market (TAM) Analysis
Analyzes market size, growth drivers, and projections through 2030
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# TAM data by segment ($ billions)
tam_by_segment = {
    "2023": {
        "AI Training": 2.8,
        "AI Inference": 0.6,
        "HPC/Supercomputing": 0.4,
        "Graphics/Gaming": 0.2,
        "Total": 4.0
    },
    "2024": {
        "AI Training": 10.3,
        "AI Inference": 2.7,
        "HPC/Supercomputing": 1.2,
        "Graphics/Gaming": 0.6,
        "Total": 14.8
    },
    "2025": {
        "AI Training": 18.5,
        "AI Inference": 6.3,
        "HPC/Supercomputing": 2.4,
        "Graphics/Gaming": 1.3,
        "Total": 28.5
    },
    "2026": {
        "AI Training": 26.5,
        "AI Inference": 10.2,
        "HPC/Supercomputing": 3.5,
        "Graphics/Gaming": 1.8,
        "Total": 42.0
    },
    "2027": {
        "AI Training": 32.0,
        "AI Inference": 14.5,
        "HPC/Supercomputing": 4.5,
        "Graphics/Gaming": 2.5,
        "Total": 53.5
    },
    "2028": {
        "AI Training": 38.0,
        "AI Inference": 20.0,
        "HPC/Supercomputing": 5.5,
        "Graphics/Gaming": 3.0,
        "Total": 66.5
    },
    "2030": {
        "AI Training": 48.0,
        "AI Inference": 32.0,
        "HPC/Supercomputing": 7.0,
        "Graphics/Gaming": 4.0,
        "Total": 91.0
    }
}

# Market drivers and unit economics
market_drivers = {
    "AI_accelerator_shipments": {
        "2023": 1.5,  # Million units
        "2024": 3.2,
        "2025": 5.5,
        "2026": 8.0,
        "2027": 10.5,
        "2030": 18.0
    },
    "avg_hbm_content_per_gpu": {
        "2023": 80,  # GB
        "2024": 128,
        "2025": 192,
        "2026": 256,
        "2027": 320,
        "2030": 512
    },
    "hbm_asp_per_gb": {
        "2023": 33,  # Dollars
        "2024": 36,
        "2025": 32,
        "2026": 28,
        "2027": 24,
        "2030": 18
    }
}

# Supply-demand balance
supply_demand = {
    "2024": {"demand": 14.8, "supply": 12.5, "utilization": 118},
    "2025": {"demand": 28.5, "supply": 26.0, "utilization": 110},
    "2026": {"demand": 42.0, "supply": 40.5, "utilization": 104},
    "2027": {"demand": 53.5, "supply": 54.0, "utilization": 99},
}

def save_data():
    """Save TAM data to JSON files"""
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    with open(data_dir / "tam_by_segment.json", "w") as f:
        json.dump(tam_by_segment, f, indent=2)

    with open(data_dir / "market_drivers.json", "w") as f:
        json.dump(market_drivers, f, indent=2)

    with open(data_dir / "supply_demand.json", "w") as f:
        json.dump(supply_demand, f, indent=2)

    print(f"✓ Saved TAM data to {data_dir}")

def plot_tam_growth():
    """Plot total addressable market growth"""
    years = list(tam_by_segment.keys())
    segments = ["AI Training", "AI Inference", "HPC/Supercomputing", "Graphics/Gaming"]

    data = {seg: [tam_by_segment[y][seg] for y in years] for seg in segments}
    total = [tam_by_segment[y]["Total"] for y in years]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Stacked area chart
    colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12']
    ax1.stackplot(range(len(years)),
                  data["AI Training"],
                  data["AI Inference"],
                  data["HPC/Supercomputing"],
                  data["Graphics/Gaming"],
                  labels=segments,
                  colors=colors,
                  alpha=0.8)

    ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Market Size ($ Billions)', fontsize=12, fontweight='bold')
    ax1.set_title('HBM TAM by Application Segment', fontsize=13, fontweight='bold')
    ax1.set_xticks(range(len(years)))
    ax1.set_xticklabels(years, rotation=45)
    ax1.legend(loc='upper left', fontsize=10)
    ax1.grid(axis='y', alpha=0.3, linestyle='--')

    # Total market growth
    ax2.plot(range(len(years)), total, marker='o', linewidth=3,
            markersize=10, color='#8e44ad', label='Total HBM Market')

    for i, (year, val) in enumerate(zip(years, total)):
        ax2.text(i, val + 3, f'${val:.1f}B', ha='center', fontsize=10, fontweight='bold')

    # Calculate and display CAGR
    cagr_2023_2027 = ((tam_by_segment["2027"]["Total"] / tam_by_segment["2023"]["Total"]) ** (1/4) - 1) * 100
    cagr_2023_2030 = ((tam_by_segment["2030"]["Total"] / tam_by_segment["2023"]["Total"]) ** (1/7) - 1) * 100

    ax2.text(0.05, 0.95, f'CAGR 2023-27: {cagr_2023_2027:.1f}%\nCAGR 2023-30: {cagr_2023_2030:.1f}%',
            transform=ax2.transAxes, fontsize=11, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7),
            verticalalignment='top')

    ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Total TAM ($ Billions)', fontsize=12, fontweight='bold')
    ax2.set_title('Total HBM Market Growth (2023-2030)', fontsize=13, fontweight='bold')
    ax2.set_xticks(range(len(years)))
    ax2.set_xticklabels(years, rotation=45)
    ax2.grid(True, alpha=0.3, linestyle='--')
    ax2.legend(loc='upper left', fontsize=10)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    charts_dir.mkdir(exist_ok=True)
    plt.savefig(charts_dir / "hbm_tam_analysis.png", dpi=300, bbox_inches='tight')
    print(f"✓ Saved chart: hbm_tam_analysis.png")
    plt.close()

def plot_unit_economics():
    """Plot unit economics and market drivers"""
    years = [2023, 2024, 2025, 2026, 2027, 2030]

    shipments = [market_drivers["AI_accelerator_shipments"][str(y)] for y in years]
    hbm_per_gpu = [market_drivers["avg_hbm_content_per_gpu"][str(y)] for y in years]
    asp = [market_drivers["hbm_asp_per_gb"][str(y)] for y in years]

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

    # AI accelerator shipments
    ax1.bar(range(len(years)), shipments, color='#3498db', alpha=0.8, edgecolor='black')
    for i, val in enumerate(shipments):
        ax1.text(i, val + 0.3, f'{val:.1f}M', ha='center', fontsize=9, fontweight='bold')
    ax1.set_xticks(range(len(years)))
    ax1.set_xticklabels(years, rotation=45)
    ax1.set_ylabel('Units (Millions)', fontsize=11, fontweight='bold')
    ax1.set_title('AI Accelerator Shipments', fontsize=12, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)

    # HBM content per GPU
    ax2.plot(range(len(years)), hbm_per_gpu, marker='s', linewidth=2.5,
            markersize=8, color='#e74c3c')
    for i, val in enumerate(hbm_per_gpu):
        ax2.text(i, val + 15, f'{val}GB', ha='center', fontsize=9, fontweight='bold')
    ax2.set_xticks(range(len(years)))
    ax2.set_xticklabels(years, rotation=45)
    ax2.set_ylabel('HBM Capacity (GB)', fontsize=11, fontweight='bold')
    ax2.set_title('Avg HBM Content per AI GPU', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)

    # ASP per GB
    ax3.plot(range(len(years)), asp, marker='o', linewidth=2.5,
            markersize=8, color='#2ecc71')
    for i, val in enumerate(asp):
        ax3.text(i, val + 1.5, f'${val}', ha='center', fontsize=9, fontweight='bold')
    ax3.set_xticks(range(len(years)))
    ax3.set_xticklabels(years, rotation=45)
    ax3.set_ylabel('Price per GB ($)', fontsize=11, fontweight='bold')
    ax3.set_title('HBM ASP per GB (Declining)', fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3)

    # Revenue per accelerator
    revenue_per_unit = [(hbm_per_gpu[i] * asp[i]) for i in range(len(years))]
    ax4.bar(range(len(years)), revenue_per_unit, color='#f39c12', alpha=0.8, edgecolor='black')
    for i, val in enumerate(revenue_per_unit):
        ax4.text(i, val + 100, f'${val:.0f}', ha='center', fontsize=9, fontweight='bold')
    ax4.set_xticks(range(len(years)))
    ax4.set_xticklabels(years, rotation=45)
    ax4.set_ylabel('HBM Revenue per GPU ($)', fontsize=11, fontweight='bold')
    ax4.set_title('HBM $ Content per Accelerator', fontsize=12, fontweight='bold')
    ax4.grid(axis='y', alpha=0.3)

    plt.suptitle('HBM Market Drivers & Unit Economics', fontsize=14, fontweight='bold', y=1.00)
    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "hbm_unit_economics.png", dpi=300, bbox_inches='tight')
    print(f"✓ Saved chart: hbm_unit_economics.png")
    plt.close()

def plot_supply_demand():
    """Plot supply-demand balance and utilization"""
    years = list(supply_demand.keys())
    demand_vals = [supply_demand[y]["demand"] for y in years]
    supply_vals = [supply_demand[y]["supply"] for y in years]
    util_vals = [supply_demand[y]["utilization"] for y in years]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Supply vs Demand
    x = np.arange(len(years))
    width = 0.35

    bars1 = ax1.bar(x - width/2, demand_vals, width, label='Demand',
                    color='#e74c3c', alpha=0.8, edgecolor='black')
    bars2 = ax1.bar(x + width/2, supply_vals, width, label='Supply',
                    color='#2ecc71', alpha=0.8, edgecolor='black')

    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}B',
                    ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Market Size ($ Billions)', fontsize=12, fontweight='bold')
    ax1.set_title('HBM Supply vs Demand Balance', fontsize=13, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(years)
    ax1.legend(loc='upper left', fontsize=11)
    ax1.grid(axis='y', alpha=0.3)

    # Utilization rate
    ax2.plot(range(len(years)), util_vals, marker='o', linewidth=3,
            markersize=10, color='#9b59b6')
    ax2.axhline(y=100, color='red', linestyle='--', linewidth=2, alpha=0.7, label='100% Utilization')

    for i, val in enumerate(util_vals):
        color = '#e74c3c' if val > 100 else '#2ecc71'
        ax2.text(i, val + 2, f'{val}%', ha='center', fontsize=11,
                fontweight='bold', color=color)

    ax2.fill_between(range(len(years)), 100, util_vals,
                     where=[u > 100 for u in util_vals],
                     alpha=0.3, color='red', label='Tight Supply')

    ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Capacity Utilization (%)', fontsize=12, fontweight='bold')
    ax2.set_title('HBM Industry Utilization Rate', fontsize=13, fontweight='bold')
    ax2.set_xticks(range(len(years)))
    ax2.set_xticklabels(years)
    ax2.legend(loc='upper right', fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(95, 125)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "hbm_supply_demand.png", dpi=300, bbox_inches='tight')
    print(f"✓ Saved chart: hbm_supply_demand.png")
    plt.close()

if __name__ == "__main__":
    print("Generating HBM TAM analysis...")
    save_data()
    plot_tam_growth()
    plot_unit_economics()
    plot_supply_demand()
    print("\n✓ TAM analysis complete!")
