#!/usr/bin/env python3
"""
Generate profitability and margin analysis charts for Google (Alphabet).
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 10

# Colors
COLORS = {
    'google': '#4285F4',
    'microsoft': '#00A4EF',
    'amazon': '#FF9900',
    'meta': '#0668E1',
    'gross': '#34A853',
    'operating': '#4285F4',
    'net': '#EA4335',
}

DATA_DIR = '../data'
CHARTS_DIR = '../charts'

def create_margin_data():
    """Create historical margin data for Google."""
    data = {
        'year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
        # Approximate margins based on historical data
        'gross_margin': [0.62, 0.61, 0.62, 0.58, 0.56, 0.56, 0.57, 0.56, 0.56, 0.56],
        'operating_margin': [0.24, 0.24, 0.25, 0.24, 0.22, 0.22, 0.31, 0.27, 0.29, 0.30],
        'net_margin': [0.22, 0.21, 0.23, 0.22, 0.20, 0.19, 0.29, 0.24, 0.27, 0.28],
        'roe': [0.14, 0.14, 0.16, 0.16, 0.15, 0.17, 0.30, 0.26, 0.29, 0.35],
        'roic': [0.13, 0.13, 0.15, 0.16, 0.14, 0.15, 0.24, 0.20, 0.22, 0.20],
    }
    return pd.DataFrame(data)

def create_competitor_margins():
    """Create competitor margin comparison data."""
    data = {
        'company': ['Alphabet', 'Microsoft', 'Amazon', 'Meta'],
        'gross_margin_2024': [0.56, 0.69, 0.48, 0.81],
        'operating_margin_2024': [0.30, 0.43, 0.09, 0.38],
        'net_margin_2024': [0.28, 0.36, 0.07, 0.35],
        'roe_2024': [0.35, 0.41, 0.22, 0.32],
        'roic_2024': [0.20, 0.28, 0.10, 0.19],
    }
    return pd.DataFrame(data)

def plot_margin_trends():
    """Create Chart 3: Profitability trends."""
    print("Generating Chart 3: Profitability Trends...")

    df = create_margin_data()
    comp_df = create_competitor_margins()

    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

    # Chart 1: Margin trends over time
    ax1 = fig.add_subplot(gs[0, :])

    ax1.plot(df['year'], df['gross_margin'] * 100, marker='o', linewidth=2.5,
             color=COLORS['gross'], markersize=7, label='Gross Margin')
    ax1.plot(df['year'], df['operating_margin'] * 100, marker='s', linewidth=2.5,
             color=COLORS['operating'], markersize=7, label='Operating Margin')
    ax1.plot(df['year'], df['net_margin'] * 100, marker='^', linewidth=2.5,
             color=COLORS['net'], markersize=7, label='Net Profit Margin')

    # Shade AI investment era
    ax1.axvspan(2022, 2024, alpha=0.15, color='purple', label='AI Investment Era')

    # Add annotations for key events
    ax1.annotate('Cloud Profitability\nInflection',
                xy=(2023, 30), xytext=(2021.5, 40),
                arrowprops=dict(arrowstyle='->', color='green', lw=1.5),
                fontsize=9, ha='center', color='green', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='green', alpha=0.8))

    ax1.set_xlabel('Year', fontweight='bold')
    ax1.set_ylabel('Margin (%)', fontweight='bold')
    ax1.set_title('Alphabet Profitability Margins (2015-2024)', fontsize=14, fontweight='bold', pad=15)
    ax1.legend(loc='lower left', fontsize=10, framealpha=0.9)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(2014.5, 2024.5)
    ax1.set_ylim(15, 65)

    # Chart 2: ROE and ROIC trends
    ax2 = fig.add_subplot(gs[1, 0])

    x = np.arange(len(df))
    width = 0.35

    ax2.bar(x - width/2, df['roe'] * 100, width, label='ROE',
            color=COLORS['google'], alpha=0.8, edgecolor='black')
    ax2.bar(x + width/2, df['roic'] * 100, width, label='ROIC',
            color=COLORS['gross'], alpha=0.8, edgecolor='black')

    # Add value labels
    for i, (roe, roic) in enumerate(zip(df['roe'], df['roic'])):
        ax2.text(i - width/2, roe * 100 + 1, f'{roe*100:.0f}%',
                ha='center', va='bottom', fontsize=8, fontweight='bold')
        ax2.text(i + width/2, roic * 100 + 1, f'{roic*100:.0f}%',
                ha='center', va='bottom', fontsize=8, fontweight='bold')

    ax2.set_xlabel('Year', fontweight='bold')
    ax2.set_ylabel('Return (%)', fontweight='bold')
    ax2.set_title('Return on Equity (ROE) vs Return on Invested Capital (ROIC)',
                  fontsize=12, fontweight='bold', pad=10)
    ax2.set_xticks(x)
    ax2.set_xticklabels(df['year'])
    ax2.legend(fontsize=10, loc='upper left')
    ax2.grid(True, alpha=0.3, axis='y')

    # Chart 3: Competitor comparison - Gross Margins
    ax3 = fig.add_subplot(gs[1, 1])

    companies = comp_df['company']
    gross_margins = comp_df['gross_margin_2024'] * 100

    colors_comp = [COLORS['google'], COLORS['microsoft'], COLORS['amazon'], COLORS['meta']]
    bars = ax3.barh(companies, gross_margins, color=colors_comp, alpha=0.8, edgecolor='black')

    # Add value labels
    for i, (company, margin) in enumerate(zip(companies, gross_margins)):
        ax3.text(margin + 1, i, f'{margin:.1f}%',
                va='center', ha='left', fontsize=10, fontweight='bold')

    ax3.set_xlabel('Gross Margin (%)', fontweight='bold')
    ax3.set_title('2024 Gross Margin Comparison', fontsize=12, fontweight='bold', pad=10)
    ax3.grid(True, alpha=0.3, axis='x')
    ax3.set_xlim(0, 90)

    # Chart 4: Competitor comparison - Operating Margins
    ax4 = fig.add_subplot(gs[2, 0])

    operating_margins = comp_df['operating_margin_2024'] * 100
    bars = ax4.barh(companies, operating_margins, color=colors_comp, alpha=0.8, edgecolor='black')

    # Add value labels
    for i, (company, margin) in enumerate(zip(companies, operating_margins)):
        ax4.text(margin + 0.5, i, f'{margin:.1f}%',
                va='center', ha='left', fontsize=10, fontweight='bold')

    ax4.set_xlabel('Operating Margin (%)', fontweight='bold')
    ax4.set_title('2024 Operating Margin Comparison', fontsize=12, fontweight='bold', pad=10)
    ax4.grid(True, alpha=0.3, axis='x')
    ax4.set_xlim(0, 50)

    # Chart 5: Competitor comparison - ROE
    ax5 = fig.add_subplot(gs[2, 1])

    roe_values = comp_df['roe_2024'] * 100
    bars = ax5.barh(companies, roe_values, color=colors_comp, alpha=0.8, edgecolor='black')

    # Add value labels
    for i, (company, roe) in enumerate(zip(companies, roe_values)):
        ax5.text(roe + 0.5, i, f'{roe:.1f}%',
                va='center', ha='left', fontsize=10, fontweight='bold')

    ax5.set_xlabel('Return on Equity (%)', fontweight='bold')
    ax5.set_title('2024 ROE Comparison', fontsize=12, fontweight='bold', pad=10)
    ax5.grid(True, alpha=0.3, axis='x')
    ax5.set_xlim(0, 50)

    # Add overall title
    fig.suptitle('Alphabet Profitability Analysis & Peer Comparison',
                fontsize=16, fontweight='bold', y=0.995)

    # Save
    os.makedirs(CHARTS_DIR, exist_ok=True)
    output_file = os.path.join(CHARTS_DIR, 'profitability_trends.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.savefig(output_file.replace('.png', '.svg'), format='svg', bbox_inches='tight')
    print(f"Saved: {output_file}")
    plt.close()

def main():
    """Main execution."""
    print("\n" + "="*60)
    print("Generating Profitability Charts")
    print("="*60 + "\n")

    os.makedirs(CHARTS_DIR, exist_ok=True)

    plot_margin_trends()

    print("\n" + "="*60)
    print("Profitability charts generation complete!")
    print("="*60 + "\n")

if __name__ == '__main__':
    main()
