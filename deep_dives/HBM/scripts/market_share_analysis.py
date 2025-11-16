#!/usr/bin/env python3
"""
HBM Market Share Analysis
Generates market share data and visualizations for SK hynix, Samsung, and Micron
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Market share data based on industry reports (TrendForce, Semianalysis)
market_share_data = {
    "2023": {
        "SK hynix": 53,
        "Samsung": 42,
        "Micron": 5
    },
    "2024": {
        "SK hynix": 52,
        "Samsung": 36,
        "Micron": 12
    },
    "2025E": {
        "SK hynix": 51,
        "Samsung": 27,
        "Micron": 22
    },
    "2026E": {
        "SK hynix": 50,
        "Samsung": 28,
        "Micron": 22
    }
}

# HBM revenue projections ($ billions)
hbm_revenue = {
    "2023": {
        "Total": 4.0,
        "SK hynix": 2.12,
        "Samsung": 1.68,
        "Micron": 0.20
    },
    "2024": {
        "Total": 14.8,
        "SK hynix": 7.70,
        "Samsung": 5.33,
        "Micron": 1.78
    },
    "2025E": {
        "Total": 28.5,
        "SK hynix": 14.54,
        "Samsung": 7.70,
        "Micron": 6.27
    },
    "2026E": {
        "Total": 42.0,
        "SK hynix": 21.0,
        "Samsung": 11.76,
        "Micron": 9.24
    },
    "2027E": {
        "Total": 53.5,
        "SK hynix": 26.75,
        "Samsung": 14.98,
        "Micron": 11.77
    }
}

def save_data():
    """Save market data to JSON files"""
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    with open(data_dir / "market_share.json", "w") as f:
        json.dump(market_share_data, f, indent=2)

    with open(data_dir / "hbm_revenue.json", "w") as f:
        json.dump(hbm_revenue, f, indent=2)

    print(f"✓ Saved market data to {data_dir}")

def plot_market_share():
    """Generate market share evolution chart"""
    years = list(market_share_data.keys())
    sk_hynix = [market_share_data[y]["SK hynix"] for y in years]
    samsung = [market_share_data[y]["Samsung"] for y in years]
    micron = [market_share_data[y]["Micron"] for y in years]

    fig, ax = plt.subplots(figsize=(12, 7))
    x = np.arange(len(years))
    width = 0.25

    bars1 = ax.bar(x - width, sk_hynix, width, label='SK hynix', color='#1f77b4', alpha=0.8)
    bars2 = ax.bar(x, samsung, width, label='Samsung', color='#ff7f0e', alpha=0.8)
    bars3 = ax.bar(x + width, micron, width, label='Micron', color='#2ca02c', alpha=0.8)

    # Add value labels on bars
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.0f}%',
                   ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Market Share (%)', fontsize=12, fontweight='bold')
    ax.set_title('HBM Market Share by Supplier (2023-2026E)',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.legend(loc='upper right', fontsize=11)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_ylim(0, 65)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    charts_dir.mkdir(exist_ok=True)
    plt.savefig(charts_dir / "hbm_market_share.png", dpi=300, bbox_inches='tight')
    print(f"✓ Saved chart: hbm_market_share.png")
    plt.close()

def plot_revenue_growth():
    """Generate HBM revenue growth chart"""
    years = list(hbm_revenue.keys())
    sk_hynix = [hbm_revenue[y]["SK hynix"] for y in years]
    samsung = [hbm_revenue[y]["Samsung"] for y in years]
    micron = [hbm_revenue[y]["Micron"] for y in years]
    total = [hbm_revenue[y]["Total"] for y in years]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Stacked area chart
    ax1.fill_between(range(len(years)), 0, sk_hynix,
                     label='SK hynix', alpha=0.7, color='#1f77b4')
    ax1.fill_between(range(len(years)), sk_hynix,
                     [sk_hynix[i] + samsung[i] for i in range(len(years))],
                     label='Samsung', alpha=0.7, color='#ff7f0e')
    ax1.fill_between(range(len(years)),
                     [sk_hynix[i] + samsung[i] for i in range(len(years))],
                     total,
                     label='Micron', alpha=0.7, color='#2ca02c')

    ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Revenue ($ Billions)', fontsize=12, fontweight='bold')
    ax1.set_title('HBM Revenue by Supplier (Stacked)', fontsize=13, fontweight='bold')
    ax1.set_xticks(range(len(years)))
    ax1.set_xticklabels(years, rotation=0)
    ax1.legend(loc='upper left', fontsize=10)
    ax1.grid(axis='y', alpha=0.3, linestyle='--')

    # Total market growth line chart
    ax2.plot(range(len(years)), total, marker='o', linewidth=3,
            markersize=8, color='#d62728', label='Total HBM Market')

    for i, (year, val) in enumerate(zip(years, total)):
        ax2.text(i, val + 2, f'${val:.1f}B', ha='center', fontsize=10, fontweight='bold')

    # Add CAGR annotation
    cagr = ((total[-1] / total[0]) ** (1/(len(years)-1)) - 1) * 100
    ax2.text(0.5, 0.95, f'CAGR: {cagr:.1f}%',
            transform=ax2.transAxes, fontsize=12, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),
            verticalalignment='top', horizontalalignment='center')

    ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Total Revenue ($ Billions)', fontsize=12, fontweight='bold')
    ax2.set_title('Total HBM Market Growth', fontsize=13, fontweight='bold')
    ax2.set_xticks(range(len(years)))
    ax2.set_xticklabels(years, rotation=0)
    ax2.grid(True, alpha=0.3, linestyle='--')
    ax2.legend(loc='upper left', fontsize=10)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "hbm_revenue_growth.png", dpi=300, bbox_inches='tight')
    print(f"✓ Saved chart: hbm_revenue_growth.png")
    plt.close()

if __name__ == "__main__":
    print("Generating HBM market share analysis...")
    save_data()
    plot_market_share()
    plot_revenue_growth()
    print("\n✓ Market share analysis complete!")
