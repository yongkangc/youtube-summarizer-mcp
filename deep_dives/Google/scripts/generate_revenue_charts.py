#!/usr/bin/env python3
"""
Generate revenue growth and breakdown charts for Google (Alphabet).
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
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

# Google brand colors
COLORS = {
    'google_blue': '#4285F4',
    'google_red': '#EA4335',
    'google_yellow': '#FBBC04',
    'google_green': '#34A853',
    'search': '#4285F4',
    'youtube': '#FF0000',
    'cloud': '#34A853',
    'network': '#FBBC04',
    'other': '#EA4335',
}

DATA_DIR = '../data'
CHARTS_DIR = '../charts'

def load_data():
    """Load financial data."""
    quarterly_file = os.path.join(DATA_DIR, 'quarterly_financials.csv')

    if not os.path.exists(quarterly_file):
        print(f"Error: {quarterly_file} not found. Run fetch_financials.py first.")
        return None

    df = pd.read_csv(quarterly_file)
    df['quarter'] = pd.to_datetime(df['quarter'])
    return df

def create_segment_data():
    """
    Create segment revenue data based on actual Google reporting.
    Note: This uses approximate percentages based on recent reports.
    """
    # Approximate segment breakdown for Google (2024 data)
    segments = {
        'year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
        'total_revenue': [74.5, 90.3, 110.9, 136.8, 161.9, 182.5, 257.6, 282.8, 307.4, 350.0],  # Billions
        # Approximate percentages
        'search_pct': [0.68, 0.66, 0.64, 0.62, 0.60, 0.59, 0.58, 0.58, 0.57, 0.57],
        'youtube_pct': [0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.11, 0.10, 0.10, 0.10],
        'cloud_pct': [0.02, 0.03, 0.04, 0.05, 0.06, 0.06, 0.07, 0.09, 0.10, 0.11],
        'network_pct': [0.15, 0.15, 0.15, 0.14, 0.13, 0.13, 0.12, 0.11, 0.11, 0.10],
        'other_pct': [0.09, 0.09, 0.09, 0.10, 0.11, 0.11, 0.12, 0.12, 0.12, 0.12],
    }

    df = pd.DataFrame(segments)

    # Calculate actual revenues
    df['search'] = df['total_revenue'] * df['search_pct']
    df['youtube'] = df['total_revenue'] * df['youtube_pct']
    df['cloud'] = df['total_revenue'] * df['cloud_pct']
    df['network'] = df['total_revenue'] * df['network_pct']
    df['other'] = df['total_revenue'] * df['other_pct']

    return df

def plot_revenue_growth():
    """Create Chart 1: Revenue growth over 10 years."""
    print("Generating Chart 1: Revenue Growth (10 years)...")

    df = create_segment_data()

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

    # Top chart: Revenue trajectory
    ax1.plot(df['year'], df['total_revenue'], marker='o', linewidth=3,
             color=COLORS['google_blue'], markersize=8, label='Total Revenue')

    # Fill area under curve
    ax1.fill_between(df['year'], 0, df['total_revenue'], alpha=0.2, color=COLORS['google_blue'])

    # Add value labels
    for idx, row in df.iterrows():
        ax1.annotate(f'${row["total_revenue"]:.1f}B',
                    xy=(row['year'], row['total_revenue']),
                    xytext=(0, 10), textcoords='offset points',
                    ha='center', fontsize=9, fontweight='bold')

    # Annotations for key events
    events = [
        (2022, 280, 'ChatGPT Launch\n(Nov 2022)', 'red'),
        (2023, 310, 'Gemini Announced\n(May 2023)', 'green'),
        (2020, 185, 'COVID-19\nPandemic', 'orange'),
    ]

    for year, revenue, text, color in events:
        ax1.annotate(text, xy=(year, revenue), xytext=(year, revenue + 30),
                    arrowprops=dict(arrowstyle='->', color=color, lw=2),
                    fontsize=9, ha='center', color=color, fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=color, alpha=0.8))

    ax1.set_xlabel('Year', fontweight='bold')
    ax1.set_ylabel('Revenue (Billions USD)', fontweight='bold')
    ax1.set_title('Alphabet Total Revenue Growth (2015-2024)', fontsize=16, fontweight='bold', pad=20)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(2014.5, 2024.5)

    # Bottom chart: Year-over-year growth rates
    df['yoy_growth'] = df['total_revenue'].pct_change() * 100

    colors_growth = [COLORS['google_green'] if x > 0 else COLORS['google_red'] for x in df['yoy_growth'][1:]]
    ax2.bar(df['year'][1:], df['yoy_growth'][1:], color=colors_growth, alpha=0.7, edgecolor='black')

    # Add value labels on bars
    for idx, (year, growth) in enumerate(zip(df['year'][1:], df['yoy_growth'][1:])):
        ax2.text(year, growth + 1 if growth > 0 else growth - 1,
                f'{growth:.1f}%', ha='center', va='bottom' if growth > 0 else 'top',
                fontweight='bold', fontsize=9)

    # Add average line
    avg_growth = df['yoy_growth'][1:].mean()
    ax2.axhline(y=avg_growth, color='navy', linestyle='--', linewidth=2,
                label=f'Avg Growth: {avg_growth:.1f}%', alpha=0.7)

    ax2.set_xlabel('Year', fontweight='bold')
    ax2.set_ylabel('YoY Growth Rate (%)', fontweight='bold')
    ax2.set_title('Year-over-Year Revenue Growth Rate', fontsize=14, fontweight='bold', pad=15)
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.legend(loc='upper right', fontsize=10)
    ax2.set_xlim(2015.5, 2024.5)

    plt.tight_layout()

    # Save
    os.makedirs(CHARTS_DIR, exist_ok=True)
    output_file = os.path.join(CHARTS_DIR, 'revenue_growth_10yr.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.savefig(output_file.replace('.png', '.svg'), format='svg', bbox_inches='tight')
    print(f"Saved: {output_file}")
    plt.close()

def plot_segment_breakdown():
    """Create Chart 2: Revenue breakdown by segment."""
    print("Generating Chart 2: Revenue Breakdown by Segment...")

    df = create_segment_data()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    # Left chart: Stacked area chart
    ax1.stackplot(df['year'],
                  df['search'], df['youtube'], df['cloud'], df['network'], df['other'],
                  labels=['Google Search & Other', 'YouTube Ads', 'Google Cloud',
                          'Google Network', 'Other Bets & Services'],
                  colors=[COLORS['search'], COLORS['youtube'], COLORS['cloud'],
                          COLORS['network'], COLORS['other']],
                  alpha=0.8)

    ax1.set_xlabel('Year', fontweight='bold')
    ax1.set_ylabel('Revenue (Billions USD)', fontweight='bold')
    ax1.set_title('Revenue by Segment (2015-2024)', fontsize=14, fontweight='bold', pad=15)
    ax1.legend(loc='upper left', fontsize=9, framealpha=0.9)
    ax1.grid(True, alpha=0.3, axis='y')
    ax1.set_xlim(2015, 2024)

    # Right chart: Pie chart for 2024
    latest = df.iloc[-1]
    segments_2024 = [latest['search'], latest['youtube'], latest['cloud'],
                     latest['network'], latest['other']]
    labels_2024 = ['Google Search\n& Other\n57%', 'YouTube Ads\n10%',
                   'Google Cloud\n11%', 'Google Network\n10%',
                   'Other Bets\n& Services\n12%']
    colors_2024 = [COLORS['search'], COLORS['youtube'], COLORS['cloud'],
                   COLORS['network'], COLORS['other']]

    wedges, texts, autotexts = ax2.pie(segments_2024, labels=labels_2024, colors=colors_2024,
                                        autopct='$%1.0fB', startangle=90,
                                        pctdistance=0.85, textprops={'fontsize': 10, 'fontweight': 'bold'})

    # Make percentage text white and bold
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(11)

    ax2.set_title(f'2024 Revenue Breakdown\n(Total: ${latest["total_revenue"]:.1f}B)',
                  fontsize=14, fontweight='bold', pad=15)

    plt.tight_layout()

    # Save
    output_file = os.path.join(CHARTS_DIR, 'revenue_breakdown_segments.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.savefig(output_file.replace('.png', '.svg'), format='svg', bbox_inches='tight')
    print(f"Saved: {output_file}")
    plt.close()

def main():
    """Main execution."""
    print("\n" + "="*60)
    print("Generating Revenue Charts for Google (Alphabet)")
    print("="*60 + "\n")

    os.makedirs(CHARTS_DIR, exist_ok=True)

    plot_revenue_growth()
    plot_segment_breakdown()

    print("\n" + "="*60)
    print("Revenue charts generation complete!")
    print("="*60 + "\n")

if __name__ == '__main__':
    main()
