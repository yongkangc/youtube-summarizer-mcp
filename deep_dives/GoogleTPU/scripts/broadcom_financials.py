#!/usr/bin/env python3
"""
Broadcom TPU Financials and Supply Chain Analysis
Revenue projections, supply chain economics, and partnership dynamics
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Broadcom AI revenue data ($ billions)
broadcom_revenue = {
    "2022": {
        "total_ai": 1.5,
        "google_tpu": 1.0,
        "networking": 0.4,
        "other_custom": 0.1,
        "notes": "Early TPU ramp"
    },
    "2023": {
        "total_ai": 4.0,
        "google_tpu": 2.5,
        "networking": 1.2,
        "other_custom": 0.3,
        "notes": "TPU v4/v5 deployment"
    },
    "2024E": {
        "total_ai": 12.0,
        "google_tpu": 7.5,
        "networking": 3.5,
        "other_custom": 1.0,
        "notes": "TPU v5p/v6 ramp, Meta MTIA"
    },
    "2025E": {
        "total_ai": 15.0,
        "google_tpu": 9.0,
        "networking": 4.5,
        "other_custom": 1.5,
        "notes": "TPU v7 Ironwood, MediaTek diversification begins"
    },
    "2026E": {
        "total_ai": 18.0,
        "google_tpu": 10.0,
        "networking": 6.0,
        "other_custom": 2.0,
        "notes": "Mature TPU ecosystem"
    }
}

# Supply chain division of labor
supply_chain_roles = {
    "Google": {
        "contributions": [
            "TPU architecture definition",
            "Matrix Multiply Unit (MXU) RTL design",
            "SparseCore accelerator design",
            "XLA compiler optimization",
            "Interconnect (ICI) protocol",
            "Workload characterization"
        ],
        "value_capture": "Internal cost savings, GCP differentiation"
    },
    "Broadcom": {
        "contributions": [
            "Physical IP (standard cells, I/O)",
            "SerDes (112G → 224G high-speed I/O)",
            "Memory controllers (HBM interface)",
            "TSMC coordination and tape-out",
            "Package design",
            "Test development"
        ],
        "value_capture": "$7-10B+ annual revenue, ~40% gross margin"
    },
    "TSMC": {
        "contributions": [
            "Wafer fabrication (5nm, 3nm)",
            "Advanced packaging (CoWoS)",
            "Yield optimization"
        ],
        "value_capture": "Wafer revenue, packaging fees"
    },
    "HBM Suppliers": {
        "contributions": [
            "HBM2e, HBM3 memory stacks",
            "SK hynix, Samsung, Micron"
        ],
        "value_capture": "Memory revenue at 35-40% margins"
    },
    "MediaTek (emerging)": {
        "contributions": [
            "TPU v7 inference chip design (rumored)",
            "TSMC relationship leverage",
            "Cost-competitive SerDes"
        ],
        "value_capture": "Diversification of Google supply chain"
    }
}

# Custom ASIC market projections
asic_market = {
    "2023": {"total": 120, "hyperscaler_asics": 15},
    "2024": {"total": 180, "hyperscaler_asics": 30},
    "2025": {"total": 220, "hyperscaler_asics": 50},
    "2026": {"total": 260, "hyperscaler_asics": 75},
    "2027": {"total": 300, "hyperscaler_asics": 100}
}

def save_data():
    """Save financial data to JSON"""
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    with open(data_dir / "broadcom_revenue.json", "w") as f:
        json.dump(broadcom_revenue, f, indent=2)

    with open(data_dir / "supply_chain_roles.json", "w") as f:
        json.dump(supply_chain_roles, f, indent=2)

    with open(data_dir / "asic_market.json", "w") as f:
        json.dump(asic_market, f, indent=2)

    print(f"Saved Broadcom financial data to {data_dir}")

def plot_broadcom_revenue():
    """Plot Broadcom AI revenue growth and breakdown"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    years = list(broadcom_revenue.keys())
    total = [broadcom_revenue[y]["total_ai"] for y in years]
    google = [broadcom_revenue[y]["google_tpu"] for y in years]
    networking = [broadcom_revenue[y]["networking"] for y in years]
    other = [broadcom_revenue[y]["other_custom"] for y in years]

    # Stacked bar chart
    x = np.arange(len(years))
    width = 0.6

    ax1.bar(x, google, width, label='Google TPU', color='#4285f4', alpha=0.9)
    ax1.bar(x, networking, width, bottom=google, label='AI Networking', color='#ea4335', alpha=0.9)
    ax1.bar(x, other, width, bottom=[g+n for g, n in zip(google, networking)],
            label='Other Custom (Meta, etc.)', color='#fbbc04', alpha=0.9)

    # Add total labels
    for i, (y, t) in enumerate(zip(years, total)):
        ax1.text(i, t + 0.3, f'${t:.1f}B', ha='center', fontsize=10, fontweight='bold')

    ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Revenue ($ Billions)', fontsize=12, fontweight='bold')
    ax1.set_title('Broadcom AI Revenue Breakdown\n(TPU + Networking + Custom Silicon)',
                 fontsize=13, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(years)
    ax1.legend(loc='upper left', fontsize=10)
    ax1.grid(axis='y', alpha=0.3, linestyle='--')

    # Growth trajectory
    ax2.plot(range(len(years)), total, marker='o', linewidth=3,
            markersize=10, color='#34a853', label='Total AI Revenue')
    ax2.plot(range(len(years)), google, marker='s', linewidth=2,
            markersize=8, color='#4285f4', label='Google TPU Revenue')

    for i, (t, g) in enumerate(zip(total, google)):
        ax2.text(i, t + 0.5, f'${t:.1f}B', ha='center', fontsize=9, fontweight='bold')

    # Add CAGR
    cagr_total = ((total[-1] / total[0]) ** (1/(len(years)-1)) - 1) * 100
    cagr_google = ((google[-1] / google[0]) ** (1/(len(years)-1)) - 1) * 100

    ax2.text(0.05, 0.95, f'Total AI CAGR: {cagr_total:.0f}%\nTPU CAGR: {cagr_google:.0f}%',
            transform=ax2.transAxes, fontsize=11, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7),
            verticalalignment='top')

    ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Revenue ($ Billions)', fontsize=12, fontweight='bold')
    ax2.set_title('Broadcom AI Revenue Growth Trajectory',
                 fontsize=13, fontweight='bold')
    ax2.set_xticks(range(len(years)))
    ax2.set_xticklabels(years)
    ax2.legend(loc='upper left', fontsize=10)
    ax2.grid(True, alpha=0.3, linestyle='--')

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    charts_dir.mkdir(exist_ok=True)
    plt.savefig(charts_dir / "10_broadcom_revenue.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 10_broadcom_revenue.png")
    plt.close()

def plot_supply_chain_sankey():
    """Create supply chain visualization (simplified flow chart)"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.axis('off')

    # Define boxes
    boxes = {
        "Google": {"pos": (0.1, 0.7), "color": "#4285f4", "width": 0.15},
        "Broadcom": {"pos": (0.4, 0.7), "color": "#ea4335", "width": 0.15},
        "MediaTek\n(Emerging)": {"pos": (0.4, 0.3), "color": "#fbbc04", "width": 0.15},
        "TSMC": {"pos": (0.7, 0.5), "color": "#34a853", "width": 0.12},
        "HBM\nSuppliers": {"pos": (0.85, 0.5), "color": "#673ab7", "width": 0.12},
        "TPU\nChip": {"pos": (0.7, 0.8), "color": "#00bcd4", "width": 0.1},
    }

    # Draw boxes
    for name, props in boxes.items():
        rect = plt.Rectangle((props["pos"][0] - props["width"]/2, props["pos"][1] - 0.08),
                             props["width"], 0.16,
                             facecolor=props["color"], alpha=0.8,
                             edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(props["pos"][0], props["pos"][1], name,
               ha='center', va='center', fontsize=11, fontweight='bold', color='white')

    # Draw arrows (simplified)
    arrows = [
        ((0.175, 0.7), (0.325, 0.7), "Architecture\nMXU Design"),
        ((0.475, 0.7), (0.64, 0.78), "SerDes\nPackaging"),
        ((0.475, 0.38), (0.64, 0.52), "v7 Inference\n(Rumored)"),
        ((0.76, 0.5), (0.79, 0.5), ""),
        ((0.7, 0.72), (0.7, 0.58), "Fab"),
    ]

    for start, end, label in arrows:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', lw=2, color='gray'))
        if label:
            mid = ((start[0] + end[0])/2, (start[1] + end[1])/2 + 0.05)
            ax.text(mid[0], mid[1], label, ha='center', fontsize=8)

    # Add value annotations
    annotations = [
        (0.4, 0.88, "Broadcom TPU Revenue: $7-10B (2024-25)", "#ea4335"),
        (0.7, 0.92, "TSMC 5nm → 3nm", "#34a853"),
        (0.1, 0.55, "Google: Architecture + Workloads", "#4285f4"),
        (0.4, 0.18, "MediaTek: Cost diversification", "#fbbc04"),
    ]

    for x, y, text, color in annotations:
        ax.text(x, y, text, ha='center', fontsize=9, fontweight='bold',
               bbox=dict(boxstyle='round', facecolor=color, alpha=0.3))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title('Google TPU Supply Chain Ecosystem\n(Division of Labor & Value Capture)',
                fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "11_supply_chain.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 11_supply_chain.png")
    plt.close()

def plot_asic_market():
    """Plot custom ASIC market growth"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    years = list(asic_market.keys())
    total = [asic_market[y]["total"] for y in years]
    hyperscaler = [asic_market[y]["hyperscaler_asics"] for y in years]
    hyperscaler_pct = [h/t*100 for h, t in zip(hyperscaler, total)]

    # Total market and hyperscaler segment
    ax1.fill_between(range(len(years)), 0, total, alpha=0.3, color='#3498db', label='Total AI Chip Market')
    ax1.fill_between(range(len(years)), 0, hyperscaler, alpha=0.8, color='#e74c3c', label='Hyperscaler Custom ASICs')
    ax1.plot(range(len(years)), total, marker='o', linewidth=2, markersize=8, color='#3498db')
    ax1.plot(range(len(years)), hyperscaler, marker='s', linewidth=2, markersize=8, color='#e74c3c')

    for i, (t, h) in enumerate(zip(total, hyperscaler)):
        ax1.text(i, t + 5, f'${t}B', ha='center', fontsize=9, fontweight='bold', color='#3498db')
        ax1.text(i, h + 5, f'${h}B', ha='center', fontsize=9, fontweight='bold', color='#e74c3c')

    ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Market Size ($ Billions)', fontsize=12, fontweight='bold')
    ax1.set_title('AI Chip Market: Total vs Custom ASIC Segment',
                 fontsize=13, fontweight='bold')
    ax1.set_xticks(range(len(years)))
    ax1.set_xticklabels(years)
    ax1.legend(loc='upper left', fontsize=10)
    ax1.grid(True, alpha=0.3, linestyle='--')

    # Hyperscaler ASIC share of total
    bars = ax2.bar(years, hyperscaler_pct, color='#9b59b6', alpha=0.8, edgecolor='black')

    for bar, val in zip(bars, hyperscaler_pct):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
               f'{val:.1f}%',
               ha='center', va='bottom', fontsize=10, fontweight='bold')

    ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Custom ASIC Share of Total AI Chip Market (%)', fontsize=12, fontweight='bold')
    ax2.set_title('Rise of Custom Silicon\n(Hyperscaler ASICs as % of Total Market)',
                 fontsize=13, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3, linestyle='--')
    ax2.set_ylim(0, 40)

    # Add annotation
    ax2.annotate('Custom silicon\neating into\nGPU market share',
                xy=(4, 33), fontsize=10, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8),
                ha='center')

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "12_asic_market.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 12_asic_market.png")
    plt.close()

def plot_revenue_comparison():
    """Compare AI chip company revenues"""
    fig, ax = plt.subplots(figsize=(12, 8))

    companies = ['NVIDIA\nData Center', 'Broadcom\nAI', 'AMD\nData Center', 'Intel\nData Center']
    revenue_2024 = [100, 12, 8, 5]  # Approximate $ billions

    colors = ['#76b900', '#ea4335', '#ed1c24', '#0071c5']
    bars = ax.barh(companies, revenue_2024, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)

    for bar, val in zip(bars, revenue_2024):
        width = bar.get_width()
        ax.text(width + 1, bar.get_y() + bar.get_height()/2.,
               f'${val}B',
               ha='left', va='center', fontsize=12, fontweight='bold')

    ax.set_xlabel('2024E Revenue ($ Billions)', fontsize=12, fontweight='bold')
    ax.set_title('AI Chip Company Revenue Comparison (2024E)\nBroadcom = #2 Behind NVIDIA',
                fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3, linestyle='--')

    # Add note
    ax.annotate('Broadcom is #2 in AI chip revenue\n(mostly Google TPU + networking)',
               xy=(12, 2.2), fontsize=10, fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='#ea4335', alpha=0.2))

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "13_revenue_comparison.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 13_revenue_comparison.png")
    plt.close()

if __name__ == "__main__":
    print("Generating Broadcom financials and supply chain analysis...")
    save_data()
    plot_broadcom_revenue()
    plot_supply_chain_sankey()
    plot_asic_market()
    plot_revenue_comparison()
    print("\nBroadcom financials analysis complete!")
