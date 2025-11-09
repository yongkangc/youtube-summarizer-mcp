#!/usr/bin/env python3
"""
Generate CapEx analysis showing AI infrastructure investment surge.
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
    'google': '#4285F4',
    'microsoft': '#00A4EF',
    'amazon': '#FF9900',
    'meta': '#0668E1',
}

DATA_DIR = '../data'
CHARTS_DIR = '../charts'

def create_capex_data():
    """Create CapEx historical and projection data."""
    data = {
        'year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
        # Google CapEx (billions)
        'google_capex': [9.9, 10.2, 13.2, 25.1, 23.5, 22.3, 24.6, 31.5, 32.3, 52.5, 92.0],
        'google_revenue': [74.5, 90.3, 110.9, 136.8, 161.9, 182.5, 257.6, 282.8, 307.4, 350.0, 380.0],
        # Competitor CapEx (billions) - approximate
        'microsoft_capex': [5.9, 8.3, 8.1, 11.6, 13.9, 15.4, 20.6, 23.9, 28.1, 44.5, 80.0],
        'amazon_capex': [4.6, 6.7, 11.9, 13.4, 16.9, 40.1, 61.0, 63.6, 52.7, 75.0, 90.0],
        'meta_capex': [2.5, 4.5, 6.7, 13.9, 13.0, 15.1, 18.6, 31.4, 28.1, 39.0, 60.0],
    }

    df = pd.DataFrame(data)
    df['google_capex_pct'] = (df['google_capex'] / df['google_revenue']) * 100
    df['is_projection'] = df['year'] >= 2025

    return df

def create_capex_breakdown():
    """Create breakdown of Google's CapEx by category."""
    data = {
        'year': [2021, 2022, 2023, 2024, 2025],
        'servers': [12.3, 18.9, 19.4, 35.0, 61.3],  # ~2/3 of technical infrastructure
        'data_centers': [8.2, 9.5, 9.7, 13.1, 23.0],  # ~1/3 of technical infrastructure
        'other': [4.1, 3.1, 3.2, 4.4, 7.7],
    }
    return pd.DataFrame(data)

def plot_capex_analysis():
    """Create Chart 5: CapEx surge analysis."""
    print("Generating Chart 5: CapEx Surge Analysis...")

    df = create_capex_data()
    breakdown_df = create_capex_breakdown()

    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

    # Chart 1: Google CapEx over time
    ax1 = fig.add_subplot(gs[0, :])

    # Separate historical and projection
    hist_mask = ~df['is_projection']
    proj_mask = df['is_projection']

    # Plot historical
    ax1.bar(df[hist_mask]['year'], df[hist_mask]['google_capex'],
            color=COLORS['google'], alpha=0.8, edgecolor='black',
            label='Historical CapEx', width=0.7)

    # Plot projection
    ax1.bar(df[proj_mask]['year'], df[proj_mask]['google_capex'],
            color=COLORS['google'], alpha=0.4, edgecolor='black', hatch='///',
            label='2025 Projection', width=0.7)

    # Add value labels
    for idx, row in df.iterrows():
        ax1.text(row['year'], row['google_capex'] + 2,
                f'${row["google_capex"]:.1f}B',
                ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Add trend line for historical data
    z = np.polyfit(df[hist_mask]['year'], df[hist_mask]['google_capex'], 2)
    p = np.poly1d(z)
    ax1.plot(df[hist_mask]['year'], p(df[hist_mask]['year']),
            "--", color='red', linewidth=2, alpha=0.7, label='Trend')

    # Add annotation for AI surge
    ax1.annotate('AI Infrastructure\nInvestment Surge\n+75% YoY',
                xy=(2024, 52.5), xytext=(2022.5, 70),
                arrowprops=dict(arrowstyle='->', color='red', lw=2.5),
                fontsize=11, ha='center', color='red', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.7', facecolor='lightyellow', edgecolor='red', alpha=0.9))

    ax1.set_xlabel('Year', fontweight='bold', fontsize=12)
    ax1.set_ylabel('Capital Expenditure (Billions USD)', fontweight='bold', fontsize=12)
    ax1.set_title('Alphabet Capital Expenditure (2015-2025): The AI Investment Surge',
                  fontsize=14, fontweight='bold', pad=15)
    ax1.legend(fontsize=11, loc='upper left', framealpha=0.9)
    ax1.grid(True, alpha=0.3, axis='y')
    ax1.set_xlim(2014.5, 2025.5)

    # Chart 2: CapEx as % of revenue
    ax2 = fig.add_subplot(gs[1, 0])

    colors_pct = [COLORS['google'] if not proj else 'orange' for proj in df['is_projection']]
    bars = ax2.bar(df['year'], df['google_capex_pct'], color=colors_pct, alpha=0.7, edgecolor='black')

    # Add value labels
    for bar, pct in zip(bars, df['google_capex_pct']):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{pct:.1f}%',
                ha='center', va='bottom', fontsize=9, fontweight='bold')

    # Add average line for historical period
    hist_avg = df[hist_mask]['google_capex_pct'].mean()
    ax2.axhline(y=hist_avg, color='navy', linestyle='--', linewidth=2,
                label=f'Historical Avg: {hist_avg:.1f}%', alpha=0.7)

    ax2.set_xlabel('Year', fontweight='bold')
    ax2.set_ylabel('CapEx as % of Revenue', fontweight='bold')
    ax2.set_title('CapEx Intensity: Growing Share of Revenue to AI Infrastructure',
                  fontsize=12, fontweight='bold', pad=10)
    ax2.legend(fontsize=10, loc='upper left')
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.set_xlim(2014.5, 2025.5)

    # Chart 3: Competitor comparison (2024-2025)
    ax3 = fig.add_subplot(gs[1, 1])

    companies = ['Alphabet', 'Microsoft', 'Amazon', 'Meta']
    capex_2024 = [52.5, 44.5, 75.0, 39.0]
    capex_2025 = [92.0, 80.0, 90.0, 60.0]

    x = np.arange(len(companies))
    width = 0.35

    bars1 = ax3.bar(x - width/2, capex_2024, width, label='2024',
                    color=[COLORS['google'], COLORS['microsoft'], COLORS['amazon'], COLORS['meta']],
                    alpha=0.8, edgecolor='black')
    bars2 = ax3.bar(x + width/2, capex_2025, width, label='2025 (Est.)',
                    color=[COLORS['google'], COLORS['microsoft'], COLORS['amazon'], COLORS['meta']],
                    alpha=0.5, edgecolor='black', hatch='///')

    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height,
                    f'${height:.0f}B',
                    ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax3.set_ylabel('Capital Expenditure (Billions USD)', fontweight='bold')
    ax3.set_title('Big Tech AI CapEx Race (2024 vs 2025)',
                  fontsize=12, fontweight='bold', pad=10)
    ax3.set_xticks(x)
    ax3.set_xticklabels(companies)
    ax3.legend(fontsize=10, framealpha=0.9)
    ax3.grid(True, alpha=0.3, axis='y')

    # Chart 4: Google CapEx breakdown by category
    ax4 = fig.add_subplot(gs[2, :])

    bottom = np.zeros(len(breakdown_df))

    colors_breakdown = ['#4285F4', '#34A853', '#FBBC04']
    labels = ['Servers (AI/ML chips, GPUs, TPUs)', 'Data Centers & Networking', 'Other Infrastructure']

    for i, (col, color, label) in enumerate(zip(['servers', 'data_centers', 'other'],
                                                 colors_breakdown, labels)):
        ax4.bar(breakdown_df['year'], breakdown_df[col], bottom=bottom,
                label=label, color=color, alpha=0.8, edgecolor='black')

        # Add value labels
        for j, (year, value) in enumerate(zip(breakdown_df['year'], breakdown_df[col])):
            if value > 3:  # Only label if segment is large enough
                ax4.text(year, bottom[j] + value/2,
                        f'${value:.1f}B',
                        ha='center', va='center', fontsize=9, fontweight='bold', color='white')

        bottom += breakdown_df[col].values

    # Add total labels on top
    for year, total in zip(breakdown_df['year'], bottom):
        ax4.text(year, total + 2,
                f'Total: ${total:.1f}B',
                ha='center', va='bottom', fontsize=10, fontweight='bold')

    ax4.set_xlabel('Year', fontweight='bold', fontsize=12)
    ax4.set_ylabel('Capital Expenditure (Billions USD)', fontweight='bold', fontsize=12)
    ax4.set_title('Google CapEx Breakdown: Servers (AI Chips) Driving Growth',
                  fontsize=14, fontweight='bold', pad=15)
    ax4.legend(fontsize=10, loc='upper left', framealpha=0.9)
    ax4.grid(True, alpha=0.3, axis='y')
    ax4.set_xlim(2020.5, 2025.5)

    # Add annotation
    ax4.annotate('2/3 of spending\non AI chips & servers',
                xy=(2025, 61.3), xytext=(2024, 75),
                arrowprops=dict(arrowstyle='->', color='darkblue', lw=2),
                fontsize=10, ha='center', color='darkblue', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', edgecolor='darkblue', alpha=0.9))

    # Add overall title
    fig.suptitle('Alphabet AI Infrastructure Investment: Unprecedented Capital Deployment',
                fontsize=16, fontweight='bold', y=0.995)

    # Save
    os.makedirs(CHARTS_DIR, exist_ok=True)
    output_file = os.path.join(CHARTS_DIR, 'capex_surge_ai.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.savefig(output_file.replace('.png', '.svg'), format='svg', bbox_inches='tight')
    print(f"Saved: {output_file}")
    plt.close()

def main():
    """Main execution."""
    print("\n" + "="*60)
    print("Generating CapEx Analysis Charts")
    print("="*60 + "\n")

    os.makedirs(CHARTS_DIR, exist_ok=True)

    plot_capex_analysis()

    print("\n" + "="*60)
    print("CapEx analysis charts generation complete!")
    print("="*60 + "\n")

if __name__ == '__main__':
    main()
