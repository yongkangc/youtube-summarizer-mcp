#!/usr/bin/env python3
"""
Generate cloud business analysis comparing Google Cloud with AWS and Azure.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)

COLORS = {
    'gcp': '#34A853',
    'aws': '#FF9900',
    'azure': '#00A4EF',
}

DATA_DIR = '../data'
CHARTS_DIR = '../charts'

def create_cloud_data():
    """Create cloud revenue comparison data."""
    data = {
        'year': [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
        # Google Cloud Platform (billions)
        'gcp_revenue': [4.0, 5.8, 8.9, 13.1, 19.2, 26.3, 33.1, 50.0],
        'gcp_growth': [None, 0.45, 0.53, 0.47, 0.47, 0.37, 0.26, 0.51],
        'gcp_operating_income': [None, None, None, None, -5.6, -2.3, -0.9, 6.5],
        # AWS (billions) - approximate
        'aws_revenue': [17.5, 25.7, 35.0, 45.4, 62.2, 80.1, 90.8, 108.0],
        'aws_growth': [None, 0.47, 0.36, 0.30, 0.37, 0.29, 0.13, 0.19],
        # Azure (billions) - approximate, Microsoft doesn't break out exact numbers
        'azure_revenue': [12.0, 18.0, 25.0, 35.0, 50.0, 68.0, 85.0, 102.0],
        'azure_growth': [None, 0.50, 0.39, 0.40, 0.43, 0.36, 0.25, 0.20],
    }
    return pd.DataFrame(data)

def create_market_share_data():
    """Create cloud market share data."""
    data = {
        'year': [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
        'aws_share': [0.34, 0.33, 0.33, 0.32, 0.33, 0.34, 0.32, 0.31],
        'azure_share': [0.14, 0.16, 0.18, 0.20, 0.21, 0.23, 0.23, 0.24],
        'gcp_share': [0.05, 0.06, 0.08, 0.09, 0.09, 0.10, 0.11, 0.11],
        'others_share': [0.47, 0.45, 0.41, 0.39, 0.37, 0.33, 0.34, 0.34],
    }
    return pd.DataFrame(data)

def plot_cloud_comparison():
    """Create Chart 4: Cloud revenue vs competitors."""
    print("Generating Chart 4: Cloud Revenue vs Competitors...")

    df = create_cloud_data()
    share_df = create_market_share_data()

    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

    # Chart 1: Revenue comparison
    ax1 = fig.add_subplot(gs[0, :])

    width = 0.25
    x = np.arange(len(df))

    bars1 = ax1.bar(x - width, df['aws_revenue'], width, label='AWS',
                    color=COLORS['aws'], alpha=0.8, edgecolor='black')
    bars2 = ax1.bar(x, df['azure_revenue'], width, label='Azure',
                    color=COLORS['azure'], alpha=0.8, edgecolor='black')
    bars3 = ax1.bar(x + width, df['gcp_revenue'], width, label='Google Cloud',
                    color=COLORS['gcp'], alpha=0.8, edgecolor='black')

    # Add value labels
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'${height:.0f}B',
                    ha='center', va='bottom', fontsize=8, fontweight='bold')

    ax1.set_xlabel('Year', fontweight='bold')
    ax1.set_ylabel('Annual Revenue (Billions USD)', fontweight='bold')
    ax1.set_title('Cloud Revenue Comparison: AWS vs Azure vs Google Cloud (2017-2024)',
                  fontsize=14, fontweight='bold', pad=15)
    ax1.set_xticks(x)
    ax1.set_xticklabels(df['year'])
    ax1.legend(fontsize=11, loc='upper left', framealpha=0.9)
    ax1.grid(True, alpha=0.3, axis='y')

    # Chart 2: Growth rates comparison
    ax2 = fig.add_subplot(gs[1, 0])

    ax2.plot(df['year'][1:], df['gcp_growth'][1:] * 100, marker='o', linewidth=2.5,
             color=COLORS['gcp'], markersize=8, label='Google Cloud', linestyle='-')
    ax2.plot(df['year'][1:], df['aws_growth'][1:] * 100, marker='s', linewidth=2.5,
             color=COLORS['aws'], markersize=8, label='AWS', linestyle='--')
    ax2.plot(df['year'][1:], df['azure_growth'][1:] * 100, marker='^', linewidth=2.5,
             color=COLORS['azure'], markersize=8, label='Azure', linestyle='-.')

    # Add annotation
    ax2.annotate('GCP: Fastest\nGrowth (51%)',
                xy=(2024, 51), xytext=(2023, 60),
                arrowprops=dict(arrowstyle='->', color='green', lw=2),
                fontsize=10, ha='center', color='green', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='green', alpha=0.9))

    ax2.set_xlabel('Year', fontweight='bold')
    ax2.set_ylabel('YoY Growth Rate (%)', fontweight='bold')
    ax2.set_title('Cloud Revenue Growth Rates', fontsize=12, fontweight='bold', pad=10)
    ax2.legend(fontsize=10, loc='upper right', framealpha=0.9)
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(0, 65)

    # Chart 3: Market share over time
    ax3 = fig.add_subplot(gs[1, 1])

    ax3.stackplot(share_df['year'],
                  share_df['aws_share'] * 100,
                  share_df['azure_share'] * 100,
                  share_df['gcp_share'] * 100,
                  share_df['others_share'] * 100,
                  labels=['AWS', 'Azure', 'Google Cloud', 'Others'],
                  colors=[COLORS['aws'], COLORS['azure'], COLORS['gcp'], '#CCCCCC'],
                  alpha=0.8)

    ax3.set_xlabel('Year', fontweight='bold')
    ax3.set_ylabel('Market Share (%)', fontweight='bold')
    ax3.set_title('Cloud Market Share Evolution (2017-2024)',
                  fontsize=12, fontweight='bold', pad=10)
    ax3.legend(loc='upper left', fontsize=10, framealpha=0.9)
    ax3.grid(True, alpha=0.3, axis='y')
    ax3.set_ylim(0, 100)

    # Chart 4: Google Cloud profitability journey
    ax4 = fig.add_subplot(gs[2, :])

    # Filter out None values for profitability
    profit_years = [2021, 2022, 2023, 2024]
    profit_values = [-5.6, -2.3, -0.9, 6.5]

    colors_profit = ['red' if x < 0 else 'green' for x in profit_values]
    bars = ax4.bar(profit_years, profit_values, color=colors_profit, alpha=0.8, edgecolor='black', width=0.6)

    # Add value labels
    for i, (year, profit) in enumerate(zip(profit_years, profit_values)):
        ax4.text(year, profit + (0.3 if profit > 0 else -0.3),
                f'${profit:.1f}B',
                ha='center', va='bottom' if profit > 0 else 'top',
                fontsize=11, fontweight='bold')

    # Add zero line
    ax4.axhline(y=0, color='black', linestyle='-', linewidth=1, alpha=0.5)

    # Add annotation for profitability inflection
    ax4.annotate('First Annual\nProfit!',
                xy=(2024, 6.5), xytext=(2023.5, 10),
                arrowprops=dict(arrowstyle='->', color='green', lw=2.5),
                fontsize=12, ha='center', color='green', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.7', facecolor='lightgreen', edgecolor='green', alpha=0.9))

    ax4.set_xlabel('Year', fontweight='bold')
    ax4.set_ylabel('Operating Income (Billions USD)', fontweight='bold')
    ax4.set_title('Google Cloud Operating Profitability Journey: Loss to Profit',
                  fontsize=14, fontweight='bold', pad=15)
    ax4.grid(True, alpha=0.3, axis='y')
    ax4.set_xlim(2020.5, 2024.5)

    # Add overall title
    fig.suptitle('Google Cloud Platform: Competitive Analysis & Growth Trajectory',
                fontsize=16, fontweight='bold', y=0.995)

    # Save
    os.makedirs(CHARTS_DIR, exist_ok=True)
    output_file = os.path.join(CHARTS_DIR, 'cloud_revenue_vs_competitors.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.savefig(output_file.replace('.png', '.svg'), format='svg', bbox_inches='tight')
    print(f"Saved: {output_file}")
    plt.close()

def main():
    """Main execution."""
    print("\n" + "="*60)
    print("Generating Cloud Analysis Charts")
    print("="*60 + "\n")

    os.makedirs(CHARTS_DIR, exist_ok=True)

    plot_cloud_comparison()

    print("\n" + "="*60)
    print("Cloud analysis charts generation complete!")
    print("="*60 + "\n")

if __name__ == '__main__':
    main()
