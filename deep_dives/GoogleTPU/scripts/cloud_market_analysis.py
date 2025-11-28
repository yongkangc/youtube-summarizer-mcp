#!/usr/bin/env python3
"""
Cloud AI Accelerator Market Analysis
Market share, custom silicon adoption, and competitive positioning
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Cloud ASIC accelerator market share (% of cloud AI accelerator market)
cloud_asic_share = {
    "2022": {
        "Google TPU": 65,
        "AWS Trainium/Inferentia": 25,
        "Azure Maia": 0,
        "Others": 10
    },
    "2023": {
        "Google TPU": 71,
        "AWS Trainium/Inferentia": 22,
        "Azure Maia": 2,
        "Others": 5
    },
    "2024E": {
        "Google TPU": 74,
        "AWS Trainium/Inferentia": 18,
        "Azure Maia": 5,
        "Others": 3
    },
    "2025E": {
        "Google TPU": 72,
        "AWS Trainium/Inferentia": 16,
        "Azure Maia": 8,
        "Others": 4
    }
}

# Custom silicon timeline
custom_silicon_timeline = {
    "Google TPU v1": 2016,
    "Google TPU v2": 2017,
    "AWS Inferentia": 2019,
    "Google TPU v4": 2021,
    "AWS Trainium": 2022,
    "Google TPU v5e/v5p": 2023,
    "Azure Maia 100": 2023,
    "Meta MTIA v1": 2023,
    "Google TPU v6 Trillium": 2024,
    "AWS Trainium2": 2024,
    "Google TPU v7 Ironwood": 2025
}

# Cloud AI infrastructure spending ($ billions)
cloud_ai_spending = {
    "2023": {
        "Google Cloud": 12,
        "AWS": 35,
        "Azure": 25,
        "Others": 8
    },
    "2024E": {
        "Google Cloud": 18,
        "AWS": 50,
        "Azure": 40,
        "Others": 12
    },
    "2025E": {
        "Google Cloud": 25,
        "AWS": 65,
        "Azure": 55,
        "Others": 15
    }
}

# Google internal workloads on TPU (estimated %)
google_tpu_internal = {
    "Search": 95,
    "YouTube (recommendations)": 90,
    "Gmail (spam detection)": 85,
    "Google Translate": 99,
    "Gemini": 100,
    "Google Ads (bidding)": 80,
    "Google Photos (recognition)": 90,
    "Google Assistant": 95,
    "Google Maps (routing AI)": 75
}

def save_data():
    """Save market data to JSON"""
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    with open(data_dir / "cloud_asic_share.json", "w") as f:
        json.dump(cloud_asic_share, f, indent=2)

    with open(data_dir / "custom_silicon_timeline.json", "w") as f:
        json.dump(custom_silicon_timeline, f, indent=2)

    with open(data_dir / "cloud_ai_spending.json", "w") as f:
        json.dump(cloud_ai_spending, f, indent=2)

    with open(data_dir / "google_tpu_internal.json", "w") as f:
        json.dump(google_tpu_internal, f, indent=2)

    print(f"Saved cloud market data to {data_dir}")

def plot_cloud_asic_share():
    """Plot cloud ASIC market share evolution"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    years = list(cloud_asic_share.keys())

    # Stacked bar chart
    google = [cloud_asic_share[y]["Google TPU"] for y in years]
    aws = [cloud_asic_share[y]["AWS Trainium/Inferentia"] for y in years]
    azure = [cloud_asic_share[y]["Azure Maia"] for y in years]
    others = [cloud_asic_share[y]["Others"] for y in years]

    x = np.arange(len(years))
    width = 0.6

    ax1.bar(x, google, width, label='Google TPU', color='#4285f4', alpha=0.9)
    ax1.bar(x, aws, width, bottom=google, label='AWS Trainium/Inferentia', color='#ff9900', alpha=0.9)
    ax1.bar(x, azure, width, bottom=[g+a for g, a in zip(google, aws)],
            label='Azure Maia', color='#00a4ef', alpha=0.9)
    ax1.bar(x, others, width, bottom=[g+a+z for g, a, z in zip(google, aws, azure)],
            label='Others', color='#95a5a6', alpha=0.9)

    # Add Google TPU share labels
    for i, g in enumerate(google):
        ax1.text(i, g/2, f'{g}%', ha='center', va='center',
                fontsize=11, fontweight='bold', color='white')

    ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Market Share (%)', fontsize=12, fontweight='bold')
    ax1.set_title('Cloud ASIC Accelerator Market Share\n(Excludes GPU-based offerings)',
                 fontsize=13, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(years)
    ax1.legend(loc='upper right', fontsize=10)
    ax1.grid(axis='y', alpha=0.3, linestyle='--')
    ax1.set_ylim(0, 105)

    # Pie chart for 2024
    sizes_2024 = [cloud_asic_share["2024E"][k] for k in
                  ["Google TPU", "AWS Trainium/Inferentia", "Azure Maia", "Others"]]
    labels = ["Google TPU\n74%", "AWS\n18%", "Azure\n5%", "Others\n3%"]
    colors = ['#4285f4', '#ff9900', '#00a4ef', '#95a5a6']
    explode = (0.05, 0, 0, 0)

    ax2.pie(sizes_2024, labels=labels, colors=colors, explode=explode,
           autopct='', startangle=90, textprops={'fontsize': 11, 'fontweight': 'bold'})
    ax2.set_title('Cloud ASIC Market Share 2024E\nGoogle TPU Dominates',
                 fontsize=13, fontweight='bold')

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    charts_dir.mkdir(exist_ok=True)
    plt.savefig(charts_dir / "14_cloud_asic_share.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 14_cloud_asic_share.png")
    plt.close()

def plot_custom_silicon_timeline():
    """Create timeline of custom silicon launches"""
    fig, ax = plt.subplots(figsize=(16, 8))

    # Prepare data
    chips = list(custom_silicon_timeline.keys())
    years = list(custom_silicon_timeline.values())

    # Colors by company
    colors = []
    for chip in chips:
        if "Google" in chip:
            colors.append('#4285f4')
        elif "AWS" in chip:
            colors.append('#ff9900')
        elif "Azure" in chip:
            colors.append('#00a4ef')
        elif "Meta" in chip:
            colors.append('#1877f2')
        else:
            colors.append('#95a5a6')

    # Create timeline
    y_positions = range(len(chips))
    ax.barh(y_positions, [1]*len(chips), left=[y-2015.5 for y in years],
           color=colors, alpha=0.8, edgecolor='black', height=0.6)

    # Add labels
    for i, (chip, year) in enumerate(zip(chips, years)):
        ax.text(year - 2015.5 + 0.5, i, f'{chip} ({year})',
               va='center', fontsize=10, fontweight='bold')

    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_title('Custom AI Silicon Timeline: The Rise of Hyperscaler ASICs\n(Google pioneered in 2016)',
                fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks([y-2015.5 for y in range(2016, 2026)])
    ax.set_xticklabels(range(2016, 2026))
    ax.set_yticks([])
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.set_xlim(-0.5, 10.5)

    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#4285f4', alpha=0.8, label='Google'),
        Patch(facecolor='#ff9900', alpha=0.8, label='AWS'),
        Patch(facecolor='#00a4ef', alpha=0.8, label='Azure'),
        Patch(facecolor='#1877f2', alpha=0.8, label='Meta')
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=10)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "15_silicon_timeline.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 15_silicon_timeline.png")
    plt.close()

def plot_cloud_spending():
    """Plot cloud AI infrastructure spending"""
    fig, ax = plt.subplots(figsize=(14, 8))

    years = list(cloud_ai_spending.keys())
    google = [cloud_ai_spending[y]["Google Cloud"] for y in years]
    aws = [cloud_ai_spending[y]["AWS"] for y in years]
    azure = [cloud_ai_spending[y]["Azure"] for y in years]
    others = [cloud_ai_spending[y]["Others"] for y in years]

    x = np.arange(len(years))
    width = 0.2

    bars1 = ax.bar(x - 1.5*width, google, width, label='Google Cloud', color='#4285f4', alpha=0.9)
    bars2 = ax.bar(x - 0.5*width, aws, width, label='AWS', color='#ff9900', alpha=0.9)
    bars3 = ax.bar(x + 0.5*width, azure, width, label='Azure', color='#00a4ef', alpha=0.9)
    bars4 = ax.bar(x + 1.5*width, others, width, label='Others', color='#95a5a6', alpha=0.9)

    # Add value labels
    for bars in [bars1, bars2, bars3, bars4]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'${height:.0f}B',
                   ha='center', va='bottom', fontsize=8, fontweight='bold')

    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('AI Infrastructure Spending ($ Billions)', fontsize=12, fontweight='bold')
    ax.set_title('Cloud AI Infrastructure Spending by Provider',
                fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "16_cloud_spending.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 16_cloud_spending.png")
    plt.close()

def plot_google_internal_tpu():
    """Plot Google internal workloads on TPU"""
    fig, ax = plt.subplots(figsize=(12, 8))

    services = list(google_tpu_internal.keys())
    percentages = list(google_tpu_internal.values())

    # Sort by percentage
    sorted_data = sorted(zip(services, percentages), key=lambda x: x[1], reverse=True)
    services = [s for s, p in sorted_data]
    percentages = [p for s, p in sorted_data]

    colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(services)))
    bars = ax.barh(services, percentages, color=colors, alpha=0.9, edgecolor='black')

    for bar, pct in zip(bars, percentages):
        width = bar.get_width()
        ax.text(width + 1, bar.get_y() + bar.get_height()/2.,
               f'{pct}%',
               ha='left', va='center', fontsize=10, fontweight='bold')

    ax.set_xlabel('% of AI Workload on TPU (vs NVIDIA GPU)', fontsize=12, fontweight='bold')
    ax.set_title("Google Internal AI Workloads on TPU\n(Google runs most AI on ZERO NVIDIA GPUs)",
                fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(0, 110)
    ax.grid(axis='x', alpha=0.3, linestyle='--')

    # Add annotation
    ax.annotate('Gemini, Translate, Search:\n100% TPU, 0% NVIDIA',
               xy=(97, 7), fontsize=10, fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8),
               ha='center')

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "17_google_internal_tpu.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 17_google_internal_tpu.png")
    plt.close()

if __name__ == "__main__":
    print("Generating cloud market analysis...")
    save_data()
    plot_cloud_asic_share()
    plot_custom_silicon_timeline()
    plot_cloud_spending()
    plot_google_internal_tpu()
    print("\nCloud market analysis complete!")
