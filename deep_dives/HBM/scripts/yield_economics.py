#!/usr/bin/env python3
"""
HBM Manufacturing Yield and Economics Analysis
Analyzes yield curves, manufacturing costs, and profitability by supplier
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Yield data by supplier and generation (%)
yield_data = {
    "SK hynix": {
        "HBM3_8Hi": 75,
        "HBM3_12Hi": 68,
        "HBM3E_8Hi": 80,
        "HBM3E_12Hi": 75,
        "HBM4_12Hi": 70
    },
    "Samsung": {
        "HBM3_8Hi": 55,
        "HBM3_12Hi": 48,
        "HBM3E_8Hi": 50,
        "HBM3E_12Hi": 45,
        "HBM4_12Hi": 60
    },
    "Micron": {
        "HBM3_8Hi": None,  # Skipped
        "HBM3_12Hi": None,
        "HBM3E_8Hi": 70,
        "HBM3E_12Hi": 65,
        "HBM4_12Hi": 65
    }
}

# Cost structure per stack (indexed, HBM3E 8-Hi = 100)
cost_structure = {
    "HBM3_8Hi": {
        "wafer_cost": 85,
        "tsv_process": 20,
        "packaging": 25,
        "testing": 12,
        "total": 142
    },
    "HBM3E_8Hi": {
        "wafer_cost": 100,
        "tsv_process": 25,
        "packaging": 30,
        "testing": 15,
        "total": 170
    },
    "HBM3E_12Hi": {
        "wafer_cost": 150,
        "tsv_process": 38,
        "packaging": 50,
        "testing": 22,
        "total": 260
    },
    "HBM4_12Hi": {
        "wafer_cost": 180,
        "tsv_process": 45,
        "packaging": 65,
        "testing": 28,
        "total": 318
    }
}

# Pricing and margins ($ per stack)
economics = {
    "HBM3_8Hi": {
        "cost": 850,
        "asp": 1200,
        "gross_margin": 29.2
    },
    "HBM3E_8Hi": {
        "cost": 1020,
        "asp": 1550,
        "gross_margin": 34.2
    },
    "HBM3E_12Hi": {
        "cost": 1560,
        "asp": 2400,
        "gross_margin": 35.0
    },
    "HBM4_12Hi": {
        "cost": 1908,
        "asp": 3200,
        "gross_margin": 40.4
    }
}

# Comparison: HBM vs standard DRAM economics
hbm_vs_dram = {
    "metric": ["ASP per GB", "Gross Margin %", "Wafer Utilization", "Cycle Time (days)"],
    "Standard DRAM": [3.5, 25, 100, 45],
    "HBM3E": [32, 35, 33, 180]
}

def save_data():
    """Save yield and economics data"""
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    with open(data_dir / "yield_data.json", "w") as f:
        json.dump(yield_data, f, indent=2)

    with open(data_dir / "cost_structure.json", "w") as f:
        json.dump(cost_structure, f, indent=2)

    with open(data_dir / "economics.json", "w") as f:
        json.dump(economics, f, indent=2)

    print(f"✓ Saved yield and economics data to {data_dir}")

def plot_yield_comparison():
    """Compare yields across suppliers and generations"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # 8-Hi yields
    suppliers = ["SK hynix", "Samsung", "Micron"]
    hbm3_8hi = [yield_data[s]["HBM3_8Hi"] for s in suppliers]
    hbm3e_8hi = [yield_data[s]["HBM3E_8Hi"] for s in suppliers]

    # Replace None with 0 for Micron HBM3
    hbm3_8hi = [0 if v is None else v for v in hbm3_8hi]

    x = np.arange(len(suppliers))
    width = 0.35

    bars1 = ax1.bar(x - width/2, hbm3_8hi, width, label='HBM3',
                    color='#3498db', alpha=0.8, edgecolor='black')
    bars2 = ax1.bar(x + width/2, hbm3e_8hi, width, label='HBM3E',
                    color='#e74c3c', alpha=0.8, edgecolor='black')

    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                        f'{height:.0f}%',
                        ha='center', va='bottom', fontsize=10, fontweight='bold')

    ax1.set_ylabel('Manufacturing Yield (%)', fontsize=12, fontweight='bold')
    ax1.set_title('HBM Yield by Supplier (8-High Stacks)', fontsize=13, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(suppliers)
    ax1.legend(loc='upper left', fontsize=11)
    ax1.grid(axis='y', alpha=0.3)
    ax1.set_ylim(0, 90)

    # 12-Hi yields
    hbm3e_12hi = [yield_data[s]["HBM3E_12Hi"] for s in suppliers]
    hbm4_12hi = [yield_data[s]["HBM4_12Hi"] for s in suppliers]

    # Replace None with 0 for Micron
    hbm3e_12hi = [0 if v is None else v for v in hbm3e_12hi]
    hbm4_12hi = [0 if v is None else v for v in hbm4_12hi]

    bars3 = ax2.bar(x - width/2, hbm3e_12hi, width, label='HBM3E',
                    color='#e74c3c', alpha=0.8, edgecolor='black')
    bars4 = ax2.bar(x + width/2, hbm4_12hi, width, label='HBM4 (Est.)',
                    color='#2ecc71', alpha=0.8, edgecolor='black')

    for bars in [bars3, bars4]:
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                ax2.text(bar.get_x() + bar.get_width()/2., height + 1,
                        f'{height:.0f}%',
                        ha='center', va='bottom', fontsize=10, fontweight='bold')

    ax2.set_ylabel('Manufacturing Yield (%)', fontsize=12, fontweight='bold')
    ax2.set_title('HBM Yield by Supplier (12-High Stacks)', fontsize=13, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(suppliers)
    ax2.legend(loc='upper left', fontsize=11)
    ax2.grid(axis='y', alpha=0.3)
    ax2.set_ylim(0, 90)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    charts_dir.mkdir(exist_ok=True)
    plt.savefig(charts_dir / "hbm_yield_comparison.png", dpi=300, bbox_inches='tight')
    print(f"✓ Saved chart: hbm_yield_comparison.png")
    plt.close()

def plot_cost_structure():
    """Visualize cost structure breakdown by generation"""
    generations = list(cost_structure.keys())
    categories = ["wafer_cost", "tsv_process", "packaging", "testing"]
    labels = ["Wafer Cost", "TSV Process", "Packaging", "Testing"]

    data = {cat: [cost_structure[gen][cat] for gen in generations] for cat in categories}

    fig, ax = plt.subplots(figsize=(12, 7))

    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
    bottom = np.zeros(len(generations))

    for cat, label, color in zip(categories, labels, colors):
        values = data[cat]
        bars = ax.bar(generations, values, bottom=bottom, label=label,
                     color=color, alpha=0.85, edgecolor='black', linewidth=0.5)
        bottom += values

    # Add total cost labels
    for i, gen in enumerate(generations):
        total = cost_structure[gen]["total"]
        ax.text(i, total + 10, f'Index: {total}',
               ha='center', va='bottom', fontsize=10, fontweight='bold')

    ax.set_ylabel('Relative Cost Index', fontsize=12, fontweight='bold')
    ax.set_title('HBM Manufacturing Cost Structure by Generation\n(HBM3E 8-Hi = 100 baseline)',
                fontsize=13, fontweight='bold', pad=20)
    ax.legend(loc='upper left', fontsize=11)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    plt.xticks(rotation=15)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "hbm_cost_structure.png", dpi=300, bbox_inches='tight')
    print(f"✓ Saved chart: hbm_cost_structure.png")
    plt.close()

def plot_margins_evolution():
    """Plot ASP, cost, and gross margin evolution"""
    generations = list(economics.keys())
    costs = [economics[gen]["cost"] for gen in generations]
    asps = [economics[gen]["asp"] for gen in generations]
    margins = [economics[gen]["gross_margin"] for gen in generations]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # ASP vs Cost
    x = np.arange(len(generations))
    width = 0.35

    bars1 = ax1.bar(x - width/2, costs, width, label='Manufacturing Cost',
                    color='#e74c3c', alpha=0.8, edgecolor='black')
    bars2 = ax1.bar(x + width/2, asps, width, label='Average Selling Price',
                    color='#2ecc71', alpha=0.8, edgecolor='black')

    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + 50,
                    f'${height:.0f}',
                    ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax1.set_ylabel('Price per Stack ($)', fontsize=12, fontweight='bold')
    ax1.set_title('HBM Cost vs ASP Evolution', fontsize=13, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(generations, rotation=15)
    ax1.legend(loc='upper left', fontsize=11)
    ax1.grid(axis='y', alpha=0.3)

    # Gross margin trend
    ax2.plot(range(len(generations)), margins, marker='o', linewidth=3,
            markersize=10, color='#9b59b6', label='Gross Margin %')

    for i, val in enumerate(margins):
        ax2.text(i, val + 1, f'{val:.1f}%', ha='center', fontsize=11, fontweight='bold')

    ax2.fill_between(range(len(generations)), 0, margins, alpha=0.3, color='#9b59b6')

    ax2.set_ylabel('Gross Margin (%)', fontsize=12, fontweight='bold')
    ax2.set_title('HBM Gross Margin Expansion', fontsize=13, fontweight='bold')
    ax2.set_xticks(range(len(generations)))
    ax2.set_xticklabels(generations, rotation=15)
    ax2.legend(loc='upper left', fontsize=11)
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(0, 50)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "hbm_margins_evolution.png", dpi=300, bbox_inches='tight')
    print(f"✓ Saved chart: hbm_margins_evolution.png")
    plt.close()

def plot_hbm_vs_dram():
    """Compare HBM vs standard DRAM economics"""
    metrics = hbm_vs_dram["metric"]
    standard = hbm_vs_dram["Standard DRAM"]
    hbm = hbm_vs_dram["HBM3E"]

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()

    colors_std = '#95a5a6'
    colors_hbm = '#e74c3c'

    for i, (metric, std_val, hbm_val) in enumerate(zip(metrics, standard, hbm)):
        ax = axes[i]

        bars = ax.bar(['Standard DRAM', 'HBM3E'], [std_val, hbm_val],
                     color=[colors_std, colors_hbm], alpha=0.8,
                     edgecolor='black', linewidth=1.5)

        # Add value labels
        for bar, val in zip(bars, [std_val, hbm_val]):
            height = bar.get_height()
            if metric == "ASP per GB":
                label = f'${val:.1f}'
            elif metric in ["Gross Margin %"]:
                label = f'{val:.0f}%'
            elif metric == "Cycle Time (days)":
                label = f'{val:.0f}d'
            else:
                label = f'{val:.0f}'

            ax.text(bar.get_x() + bar.get_width()/2., height * 0.5,
                   label, ha='center', va='center', fontsize=13,
                   fontweight='bold', color='white')

        # Calculate premium/difference
        if metric == "Wafer Utilization":
            diff = std_val - hbm_val
            ax.text(0.5, 0.95, f'{diff:.0f}pp lower',
                   transform=ax.transAxes, fontsize=10, fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='orange', alpha=0.6),
                   verticalalignment='top', horizontalalignment='center')
        elif metric == "Cycle Time (days)":
            mult = hbm_val / std_val
            ax.text(0.5, 0.95, f'{mult:.1f}x longer',
                   transform=ax.transAxes, fontsize=10, fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='orange', alpha=0.6),
                   verticalalignment='top', horizontalalignment='center')
        else:
            mult = hbm_val / std_val
            ax.text(0.5, 0.95, f'{mult:.1f}x premium',
                   transform=ax.transAxes, fontsize=10, fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.6),
                   verticalalignment='top', horizontalalignment='center')

        ax.set_title(metric, fontsize=12, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)

    plt.suptitle('HBM vs Standard DRAM Economics Comparison',
                fontsize=14, fontweight='bold', y=0.995)
    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "hbm_vs_dram_economics.png", dpi=300, bbox_inches='tight')
    print(f"✓ Saved chart: hbm_vs_dram_economics.png")
    plt.close()

if __name__ == "__main__":
    print("Generating HBM yield and economics analysis...")
    save_data()
    plot_yield_comparison()
    plot_cost_structure()
    plot_margins_evolution()
    plot_hbm_vs_dram()
    print("\n✓ Yield and economics analysis complete!")
