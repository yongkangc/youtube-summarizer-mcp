#!/usr/bin/env python3
"""
Generate valuation multiples comparison chart
Compares Google's valuation vs FANG+ peers across multiple metrics
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (16, 10)
plt.rcParams['font.size'] = 10

# Valuation data for FANG+ companies (November 2024)
valuation_data = {
    'Company': ['Alphabet', 'Microsoft', 'Amazon', 'Meta', 'Apple', 'Netflix', 'NVIDIA'],
    'Market_Cap_T': [3.37, 3.12, 2.10, 1.45, 3.50, 0.38, 3.45],
    'PE_Ratio': [27.5, 35.2, 45.8, 28.5, 32.1, 38.7, 52.3],
    'PEG_Ratio': [1.81, 3.20, 3.82, 1.58, 5.35, 2.58, 1.95],
    'EV_EBITDA': [23.3, 28.5, 32.1, 24.2, 28.9, 35.4, 48.2],
    'EV_Sales': [8.9, 12.3, 3.2, 9.1, 8.5, 7.2, 28.5],
    'Revenue_Growth': [14, 10, 12, 18, 6, 15, 95],
    'ROE': [35.5, 41.0, 22.0, 32.0, 147.0, 28.0, 95.0],
    'Op_Margin': [30, 43, 9, 38, 30, 22, 62]
}

df = pd.DataFrame(valuation_data)

def plot_valuation_comparison(output_dir='charts'):
    """Create comprehensive valuation comparison dashboard"""

    fig = plt.figure(figsize=(18, 12))
    gs = fig.add_gridspec(3, 3, hspace=0.35, wspace=0.3)

    # Color scheme
    google_color = '#1a73e8'
    peer_color = '#ea4335'
    colors = [google_color if company == 'Alphabet' else '#cccccc' for company in df['Company']]
    edge_colors = [google_color if company == 'Alphabet' else peer_color for company in df['Company']]

    # 1. P/E Ratio Comparison
    ax1 = fig.add_subplot(gs[0, 0])
    bars1 = ax1.barh(df['Company'], df['PE_Ratio'], color=colors, edgecolor=edge_colors, linewidth=2)
    ax1.axvline(df['PE_Ratio'].mean(), color='red', linestyle='--', linewidth=2, label=f'Avg: {df["PE_Ratio"].mean():.1f}x')
    ax1.set_xlabel('P/E Ratio', fontsize=11, fontweight='bold')
    ax1.set_title('P/E Ratio Comparison', fontsize=12, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3, axis='x')

    # Highlight Google
    google_idx = df[df['Company'] == 'Alphabet'].index[0]
    ax1.text(df.loc[google_idx, 'PE_Ratio'] + 1, google_idx,
             f"{df.loc[google_idx, 'PE_Ratio']:.1f}x",
             va='center', fontweight='bold', fontsize=10, color=google_color)

    # 2. PEG Ratio Comparison
    ax2 = fig.add_subplot(gs[0, 1])
    bars2 = ax2.barh(df['Company'], df['PEG_Ratio'], color=colors, edgecolor=edge_colors, linewidth=2)
    ax2.axvline(2.0, color='green', linestyle='--', linewidth=2, label='Attractive (<2.0)')
    ax2.axvline(df['PEG_Ratio'].mean(), color='red', linestyle=':', linewidth=1.5, label=f'Avg: {df["PEG_Ratio"].mean():.2f}')
    ax2.set_xlabel('PEG Ratio', fontsize=11, fontweight='bold')
    ax2.set_title('PEG Ratio (P/E to Growth)', fontsize=12, fontweight='bold')
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3, axis='x')

    # 3. EV/EBITDA Comparison
    ax3 = fig.add_subplot(gs[0, 2])
    bars3 = ax3.barh(df['Company'], df['EV_EBITDA'], color=colors, edgecolor=edge_colors, linewidth=2)
    ax3.axvline(df['EV_EBITDA'].mean(), color='red', linestyle='--', linewidth=2, label=f'Avg: {df["EV_EBITDA"].mean():.1f}x')
    ax3.set_xlabel('EV/EBITDA', fontsize=11, fontweight='bold')
    ax3.set_title('EV/EBITDA Comparison', fontsize=12, fontweight='bold')
    ax3.legend()
    ax3.grid(True, alpha=0.3, axis='x')

    # 4. ROE vs P/E Scatter
    ax4 = fig.add_subplot(gs[1, :2])
    for idx, row in df.iterrows():
        if row['Company'] == 'Alphabet':
            ax4.scatter(row['ROE'], row['PE_Ratio'], s=500, color=google_color,
                       edgecolor='black', linewidth=2, zorder=10, label='Alphabet')
            ax4.annotate('GOOGL', (row['ROE'], row['PE_Ratio']),
                        xytext=(10, 10), textcoords='offset points',
                        fontweight='bold', fontsize=11, color=google_color)
        else:
            ax4.scatter(row['ROE'], row['PE_Ratio'], s=300, color='lightcoral',
                       edgecolor=peer_color, linewidth=1.5, alpha=0.7)
            ax4.annotate(row['Company'], (row['ROE'], row['PE_Ratio']),
                        xytext=(5, 5), textcoords='offset points',
                        fontsize=9, alpha=0.8)

    ax4.set_xlabel('Return on Equity (%)', fontsize=12, fontweight='bold')
    ax4.set_ylabel('P/E Ratio', fontsize=12, fontweight='bold')
    ax4.set_title('Valuation vs Quality: ROE vs P/E Ratio', fontsize=14, fontweight='bold')
    ax4.grid(True, alpha=0.3)
    ax4.legend(loc='upper left')

    # Add diagonal lines for constant PEG
    x_range = np.array([df['ROE'].min()-10, df['ROE'].max()+10])
    for peg in [2.0, 3.0, 4.0]:
        # Simplified: assuming growth correlates with ROE
        y_range = x_range * peg / 5  # rough approximation
        ax4.plot(x_range, y_range, linestyle=':', alpha=0.3, color='gray', linewidth=1)

    # 5. Growth vs Valuation
    ax5 = fig.add_subplot(gs[1, 2])
    for idx, row in df.iterrows():
        if row['Company'] == 'Alphabet':
            ax5.scatter(row['Revenue_Growth'], row['PE_Ratio'], s=500, color=google_color,
                       edgecolor='black', linewidth=2, zorder=10)
            ax5.annotate('GOOGL', (row['Revenue_Growth'], row['PE_Ratio']),
                        xytext=(10, 10), textcoords='offset points',
                        fontweight='bold', fontsize=11, color=google_color)
        else:
            ax5.scatter(row['Revenue_Growth'], row['PE_Ratio'], s=300, color='lightblue',
                       edgecolor='steelblue', linewidth=1.5, alpha=0.7)
            ax5.annotate(row['Company'], (row['Revenue_Growth'], row['PE_Ratio']),
                        xytext=(5, 5), textcoords='offset points',
                        fontsize=9, alpha=0.8)

    ax5.set_xlabel('Revenue Growth (%)', fontsize=12, fontweight='bold')
    ax5.set_ylabel('P/E Ratio', fontsize=12, fontweight='bold')
    ax5.set_title('Growth vs Valuation', fontsize=14, fontweight='bold')
    ax5.grid(True, alpha=0.3)

    # 6. Valuation Summary Table
    ax6 = fig.add_subplot(gs[2, :])
    ax6.axis('off')

    # Create comparison table
    table_data = []
    for idx, row in df.iterrows():
        if row['Company'] in ['Alphabet', 'Microsoft', 'Amazon', 'Meta']:
            table_data.append([
                row['Company'],
                f"{row['PE_Ratio']:.1f}x",
                f"{row['PEG_Ratio']:.2f}",
                f"{row['Revenue_Growth']:.0f}%",
                f"{row['ROE']:.1f}%",
                f"{row['Op_Margin']:.0f}%"
            ])

    table = ax6.table(cellText=table_data,
                      colLabels=['Company', 'P/E', 'PEG', 'Rev Growth', 'ROE', 'Op Margin'],
                      cellLoc='center',
                      loc='center',
                      bbox=[0.1, 0.2, 0.8, 0.6])

    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2)

    # Style header
    for i in range(6):
        table[(0, i)].set_facecolor('#4285F4')
        table[(0, i)].set_text_props(weight='bold', color='white')

    # Highlight Google row
    for i in range(6):
        table[(1, i)].set_facecolor('#E8F0FE')
        table[(1, i)].set_text_props(weight='bold', color=google_color)

    ax6.text(0.5, 0.9, 'Key Metrics Comparison (Top 4 Companies)',
             ha='center', va='top', transform=ax6.transAxes,
             fontsize=14, fontweight='bold')

    # Add insights box
    insights_text = """Key Insights:
    • Alphabet trades at 27.5x P/E vs peer avg 38.5x (-29% discount)
    • PEG ratio 1.81 (attractive vs Meta 1.58, MSFT 3.20)
    • ROE of 35.5% comparable to Microsoft (41%)
    • Valuation dislocation: Similar quality, lower multiple"""

    ax6.text(0.5, 0.05, insights_text,
             ha='center', va='bottom', transform=ax6.transAxes,
             fontsize=10, family='monospace',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    # Main title
    fig.suptitle('Alphabet Valuation vs FANG+ Peers\nComprehensive Multiples Analysis',
                 fontsize=16, fontweight='bold', y=0.98)

    plt.savefig(f'{output_dir}/valuation_comparison.png', dpi=300, bbox_inches='tight')
    plt.savefig(f'{output_dir}/valuation_comparison.svg', format='svg', bbox_inches='tight')
    print(f"✓ Saved: {output_dir}/valuation_comparison.png")
    print(f"✓ Saved: {output_dir}/valuation_comparison.svg")

    return df

def main():
    print("Generating Valuation Comparison Analysis...")
    print("-" * 50)

    # Generate chart
    df = plot_valuation_comparison()

    # Calculate statistics
    google_pe = df[df['Company'] == 'Alphabet']['PE_Ratio'].values[0]
    avg_pe = df[df['Company'] != 'Alphabet']['PE_Ratio'].mean()
    discount = ((avg_pe - google_pe) / avg_pe) * 100

    # Print summary
    print("\n" + "=" * 50)
    print("VALUATION COMPARISON SUMMARY")
    print("=" * 50)

    print(f"\n📊 Alphabet (GOOGL):")
    print(f"  P/E Ratio: {google_pe:.1f}x")
    print(f"  Peer Average: {avg_pe:.1f}x")
    print(f"  Discount: {discount:.1f}%")

    print(f"\n💰 Valuation Metrics:")
    google_row = df[df['Company'] == 'Alphabet'].iloc[0]
    print(f"  PEG Ratio: {google_row['PEG_Ratio']:.2f} (attractive if <2.0)")
    print(f"  EV/EBITDA: {google_row['EV_EBITDA']:.1f}x vs peer avg {df[df['Company'] != 'Alphabet']['EV_EBITDA'].mean():.1f}x")

    print(f"\n📈 Fundamentals:")
    print(f"  Revenue Growth: {google_row['Revenue_Growth']:.0f}%")
    print(f"  ROE: {google_row['ROE']:.1f}%")
    print(f"  Operating Margin: {google_row['Op_Margin']:.0f}%")

    print(f"\n💡 Key Finding:")
    if discount > 20:
        print(f"  ✓ Alphabet trading at significant {discount:.0f}% discount despite:")
    print(f"    - Strong fundamentals (35.5% ROE, 30% op margin)")
    print(f"    - Solid growth (14% revenue CAGR)")
    print(f"    - Multiple growth drivers (Search, Cloud, AI)")
    print(f"\n  Conclusion: UNDERVALUED relative to peers")

    print("=" * 50)

if __name__ == "__main__":
    main()
