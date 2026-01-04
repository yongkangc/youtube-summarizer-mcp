#!/usr/bin/env python3
"""
Generate all visualization charts for Nvidia-Groq deep dive.
"""

import json
import os

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 7)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

# Color palette
COLORS = {
    'nvidia': '#76B900',  # Nvidia green
    'groq': '#FF6B35',    # Orange
    'amd': '#ED1C24',     # AMD red
    'cerebras': '#4A90D9', # Blue
    'google': '#4285F4',   # Google blue
    'aws': '#FF9900',      # AWS orange
    'inference': '#2ECC71', # Green
    'training': '#3498DB',  # Blue
    'hbm': '#9B59B6',       # Purple
    'sram': '#E74C3C',      # Red
}

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, '..', 'data')
CHARTS_DIR = os.path.join(SCRIPT_DIR, '..', 'charts')
os.makedirs(CHARTS_DIR, exist_ok=True)


def load_json(filename):
    """Load JSON data file."""
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'r') as f:
        return json.load(f)


def plot_inference_market_growth():
    """Chart 1: AI Inference Market Growth 2024-2030."""
    print("Generating Chart 1: Inference Market Growth...")

    years = [2024, 2025, 2026, 2027, 2028, 2029, 2030]
    # Interpolate from $97B (2024) to $255B (2030) at 17-19% CAGR
    inference_market = [97, 115, 136, 161, 190, 220, 255]
    training_market = [50, 58, 67, 78, 95, 120, 150]

    fig, ax = plt.subplots(figsize=(12, 7))

    x = np.arange(len(years))
    width = 0.35

    bars1 = ax.bar(x - width/2, inference_market, width, label='AI Inference',
                   color=COLORS['inference'], alpha=0.85, edgecolor='black')
    bars2 = ax.bar(x + width/2, training_market, width, label='AI Training',
                   color=COLORS['training'], alpha=0.85, edgecolor='black')

    # Add value labels
    for bar, val in zip(bars1, inference_market):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
                f'${val}B', ha='center', va='bottom', fontweight='bold', fontsize=9)

    for bar, val in zip(bars2, training_market):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
                f'${val}B', ha='center', va='bottom', fontweight='bold', fontsize=9)

    # Add ratio annotation for 2030
    ax.annotate(f'Inference = {inference_market[-1]/training_market[-1]:.1f}x Training',
                xy=(6, 255), xytext=(4.5, 280),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
                fontsize=11, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='yellow', alpha=0.7))

    ax.set_xlabel('Year', fontweight='bold')
    ax.set_ylabel('Market Size ($ Billions)', fontweight='bold')
    ax.set_title('AI Inference Market Projected to Reach $255B by 2030\n17-19% CAGR, Surpassing Training as Primary Workload',
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.legend(loc='upper left', fontsize=11)
    ax.set_ylim(0, 320)

    plt.tight_layout()
    output_file = os.path.join(CHARTS_DIR, '01_inference_market_growth.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_file}")
    plt.close()


def plot_bandwidth_comparison():
    """Chart 2: Memory Bandwidth Comparison (HBM vs SRAM)."""
    print("Generating Chart 2: Bandwidth Comparison...")

    chips = ['H100\n(HBM3)', 'H200\n(HBM3e)', 'B200\n(HBM3e)', 'Rubin Ultra\n(HBM4e)', 'Groq LPU\n(SRAM)']
    bandwidth = [3.35, 4.8, 8.0, 32, 80]
    colors = [COLORS['hbm'], COLORS['hbm'], COLORS['hbm'], COLORS['hbm'], COLORS['sram']]

    fig, ax = plt.subplots(figsize=(12, 7))

    bars = ax.barh(chips, bandwidth, color=colors, alpha=0.85, edgecolor='black', height=0.6)

    # Add value labels
    for bar, val in zip(bars, bandwidth):
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                f'{val} TB/s', ha='left', va='center', fontweight='bold', fontsize=11)

    # Add ratio annotation
    ax.annotate('Groq: 23x H100 bandwidth',
                xy=(80, 4), xytext=(50, 3.3),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
                fontsize=11, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow', alpha=0.8))

    ax.set_xlabel('Memory Bandwidth (TB/s)', fontweight='bold')
    ax.set_title('SRAM Delivers Massive Bandwidth Advantage\nCritical for Memory-Bound Inference Workloads',
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(0, 95)

    # Add legend
    hbm_patch = mpatches.Patch(color=COLORS['hbm'], label='HBM-based (GPU)', alpha=0.85)
    sram_patch = mpatches.Patch(color=COLORS['sram'], label='SRAM-based (LPU)', alpha=0.85)
    ax.legend(handles=[hbm_patch, sram_patch], loc='lower right', fontsize=10)

    plt.tight_layout()
    output_file = os.path.join(CHARTS_DIR, '02_bandwidth_comparison.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_file}")
    plt.close()


def plot_groq_valuation():
    """Chart 3: Groq Valuation Trajectory."""
    print("Generating Chart 3: Groq Valuation...")

    rounds = ['Series C\n(Apr 2021)', 'Series D\n(Aug 2024)', 'Series E\n(Sep 2025)', 'Nvidia Deal\n(Dec 2025)']
    valuations = [1.0, 2.8, 6.9, 20.0]
    amounts = [0.3, 0.64, 0.75, 20.0]  # Funding amounts

    fig, ax = plt.subplots(figsize=(12, 7))

    x = np.arange(len(rounds))

    # Valuation bars
    bars = ax.bar(x, valuations, color=COLORS['groq'], alpha=0.85, edgecolor='black', width=0.6)

    # Add value labels
    for bar, val in zip(bars, valuations):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                f'${val}B', ha='center', va='bottom', fontweight='bold', fontsize=12)

    # Add growth annotations
    ax.annotate('7.1x in 16 months',
                xy=(2.5, 13.5), xytext=(1.5, 16),
                arrowprops=dict(arrowstyle='->', color='darkred', lw=2),
                fontsize=12, fontweight='bold', color='darkred',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow', alpha=0.8))

    ax.set_xlabel('Funding Round', fontweight='bold')
    ax.set_ylabel('Valuation ($ Billions)', fontweight='bold')
    ax.set_title('Groq Valuation: From $1B Unicorn to $20B Nvidia Exit\nFastest Valuation Jump in AI Hardware History',
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(rounds)
    ax.set_ylim(0, 24)

    plt.tight_layout()
    output_file = os.path.join(CHARTS_DIR, '03_groq_valuation.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_file}")
    plt.close()


def plot_api_pricing_decline():
    """Chart 4: API Pricing Decline Over Time."""
    print("Generating Chart 4: API Pricing Decline...")

    dates = ['Nov 2021', 'Mar 2023', 'Nov 2023', 'Jun 2024', 'Jan 2025', 'Jan 2026']
    prices = [60.0, 30.0, 10.0, 2.0, 0.3, 0.06]  # Cost per million tokens (equivalent performance)

    fig, ax = plt.subplots(figsize=(12, 7))

    ax.semilogy(dates, prices, marker='o', markersize=12, linewidth=3,
                color=COLORS['inference'], markeredgecolor='black', markeredgewidth=2)

    # Add value labels
    for i, (date, price) in enumerate(zip(dates, prices)):
        offset = 1.3 if i < 3 else 0.7
        ax.text(i, price * offset, f'${price:.2f}', ha='center', fontweight='bold', fontsize=10)

    # Add annotations
    ax.annotate('GPT-3 Launch\n$60/M tokens',
                xy=(0, 60), xytext=(1, 80),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.5),
                fontsize=10, ha='center')

    ax.annotate('1,000x\nreduction',
                xy=(5, 0.06), xytext=(4, 0.2),
                arrowprops=dict(arrowstyle='->', color='darkgreen', lw=2),
                fontsize=12, fontweight='bold', color='darkgreen',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.7))

    ax.set_xlabel('Date', fontweight='bold')
    ax.set_ylabel('Cost per Million Tokens ($) - Log Scale', fontweight='bold')
    ax.set_title('API Inference Pricing Collapsed 1,000x in 3 Years\nDriving Massive Volume Growth',
                 fontsize=14, fontweight='bold', pad=15)
    ax.grid(True, alpha=0.3, which='both')

    plt.tight_layout()
    output_file = os.path.join(CHARTS_DIR, '04_api_pricing_decline.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_file}")
    plt.close()


def plot_nvidia_roadmap():
    """Chart 5: Nvidia Architecture Roadmap."""
    print("Generating Chart 5: Nvidia Roadmap...")

    architectures = ['H100\n(2022)', 'H200\n(2024)', 'B200\n(2025)', 'B300\n(H2 2025)', 'Rubin\n(H2 2026)', 'Rubin Ultra\n(H2 2027)']
    bandwidth = [3.35, 4.8, 8.0, 10.0, 13.0, 32.0]
    capacity = [80, 141, 192, 288, 288, 1024]

    fig, ax1 = plt.subplots(figsize=(14, 7))

    x = np.arange(len(architectures))
    width = 0.35

    # Bandwidth bars
    bars1 = ax1.bar(x - width/2, bandwidth, width, label='Bandwidth (TB/s)',
                    color=COLORS['nvidia'], alpha=0.85, edgecolor='black')
    ax1.set_ylabel('Memory Bandwidth (TB/s)', fontweight='bold', color=COLORS['nvidia'])
    ax1.tick_params(axis='y', labelcolor=COLORS['nvidia'])
    ax1.set_ylim(0, 40)

    # Add bandwidth labels
    for bar, val in zip(bars1, bandwidth):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{val}', ha='center', va='bottom', fontweight='bold', fontsize=9, color=COLORS['nvidia'])

    # Capacity on secondary axis
    ax2 = ax1.twinx()
    bars2 = ax2.bar(x + width/2, capacity, width, label='Capacity (GB)',
                    color='#3498DB', alpha=0.85, edgecolor='black')
    ax2.set_ylabel('Memory Capacity (GB)', fontweight='bold', color='#3498DB')
    ax2.tick_params(axis='y', labelcolor='#3498DB')
    ax2.set_ylim(0, 1200)

    # Add capacity labels
    for bar, val in zip(bars2, capacity):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 15,
                f'{val}', ha='center', va='bottom', fontweight='bold', fontsize=9, color='#3498DB')

    # Groq reference line
    ax1.axhline(y=80, color=COLORS['sram'], linestyle='--', linewidth=2, alpha=0.7)
    ax1.text(5.5, 81, 'Groq LPU: 80 TB/s', ha='right', va='bottom',
             fontsize=10, color=COLORS['sram'], fontweight='bold')

    ax1.set_xlabel('Architecture (Timeline)', fontweight='bold')
    ax1.set_title("Nvidia's Roadmap: Rubin Ultra (2027) Closes Bandwidth Gap\nBut SRAM Maintains 2.5x Advantage",
                  fontsize=14, fontweight='bold', pad=15)
    ax1.set_xticks(x)
    ax1.set_xticklabels(architectures)

    # Combined legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)

    plt.tight_layout()
    output_file = os.path.join(CHARTS_DIR, '05_nvidia_roadmap.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_file}")
    plt.close()


def plot_competitive_landscape():
    """Chart 6: Competitive Landscape - Market Share by Segment."""
    print("Generating Chart 6: Competitive Landscape...")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Training market share (left)
    training_labels = ['Nvidia', 'Google TPU', 'AMD', 'Others']
    training_shares = [92, 3, 3, 2]
    training_colors = [COLORS['nvidia'], COLORS['google'], COLORS['amd'], '#95A5A6']

    wedges, texts, autotexts = ax1.pie(training_shares, labels=training_labels, autopct='%1.0f%%',
                                        colors=training_colors, startangle=90, textprops={'fontsize': 11})
    for autotext in autotexts:
        autotext.set_fontweight('bold')
    ax1.set_title('AI Training Market Share (2024)\nNvidia Dominates at 92%',
                  fontsize=12, fontweight='bold', pad=10)

    # Inference market share (right)
    inference_labels = ['Nvidia', 'Custom ASICs', 'AMD/Other GPUs', 'SRAM\n(Groq/Cerebras)']
    inference_shares = [70, 15, 10, 5]
    inference_colors = [COLORS['nvidia'], COLORS['google'], COLORS['amd'], COLORS['sram']]

    wedges2, texts2, autotexts2 = ax2.pie(inference_shares, labels=inference_labels, autopct='%1.0f%%',
                                           colors=inference_colors, startangle=90, textprops={'fontsize': 11})
    for autotext in autotexts2:
        autotext.set_fontweight('bold')
    ax2.set_title('AI Inference Market Share (2024)\nMore Fragmented - SRAM Emerging',
                  fontsize=12, fontweight='bold', pad=10)

    plt.suptitle('Training vs Inference: Different Competitive Dynamics',
                 fontsize=14, fontweight='bold', y=1.02)

    plt.tight_layout()
    output_file = os.path.join(CHARTS_DIR, '06_competitive_landscape.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_file}")
    plt.close()


def main():
    """Generate all charts."""
    print("\n" + "="*60)
    print("Generating Charts for Nvidia-Groq Deep Dive")
    print("="*60 + "\n")

    plot_inference_market_growth()
    plot_bandwidth_comparison()
    plot_groq_valuation()
    plot_api_pricing_decline()
    plot_nvidia_roadmap()
    plot_competitive_landscape()

    print("\n" + "="*60)
    print("All charts generated successfully!")
    print(f"Output directory: {CHARTS_DIR}")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()
