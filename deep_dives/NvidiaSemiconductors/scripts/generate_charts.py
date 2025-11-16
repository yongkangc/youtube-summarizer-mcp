#!/usr/bin/env python3
"""
Generate Charts and Visualizations
Creates publication-ready charts for the Nvidia/Semiconductor analysis
"""

import json
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# Set style for professional-looking charts
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 7)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

def load_data():
    """Load all generated data files"""
    data_dir = Path('deep_dives/NvidiaSemiconductors/data')

    data = {}

    files = ['gpu_performance.json', 'tam_analysis.json', 'competitive_analysis.json']

    for file in files:
        file_path = data_dir / file
        if file_path.exists():
            with open(file_path, 'r') as f:
                key = file.replace('.json', '')
                data[key] = json.load(f)

    return data

def chart1_gpu_performance_evolution(data):
    """Chart 1: GPU Performance Evolution (Huang's Law)"""

    gpus = data['gpu_performance']['gpu_history']

    years = [gpu['year'] for gpu in gpus]
    tflops = [gpu.get('tflops', gpu.get('tflops_fp16', 0)) for gpu in gpus]

    fig, ax = plt.subplots(figsize=(14, 8))

    # Plot performance on log scale
    ax.semilogy(years, tflops, marker='o', linewidth=2.5, markersize=10, color='#76B900', label='GPU Performance')

    # Add annotations for key milestones
    annotations = [
        (1999, 0.00048, 'First "GPU"'),
        (2006, 0.518, 'CUDA Launch'),
        (2012, 4.58, 'AlexNet Era'),
        (2020, 312, 'A100\n(AI Boom)'),
        (2022, 1979, 'H100\n(LLM Era)')
    ]

    for year, tflop, label in annotations:
        ax.annotate(label, xy=(year, tflop), xytext=(10, 10),
                   textcoords='offset points', fontsize=9,
                   bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.3),
                   arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

    ax.set_xlabel('Year', fontweight='bold')
    ax.set_ylabel('Performance (TFLOPS, log scale)', fontweight='bold')
    ax.set_title("Huang's Law: GPU Performance Doubling Every ~1 Year\n(4 million times improvement in 25 years)",
                fontweight='bold', fontsize=15)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=12)

    plt.tight_layout()
    plt.savefig('deep_dives/NvidiaSemiconductors/charts/gpu_performance_evolution.png', dpi=300, bbox_inches='tight')
    print("✓ Generated: gpu_performance_evolution.png")
    plt.close()

def chart2_nvidia_revenue_segments(data):
    """Chart 2: Nvidia Revenue by Segment (2020-2024)"""

    segments = data['gpu_performance']['gpu_history']  # We'll use manual data

    # Manual data from Nvidia's reports
    years = [2020, 2021, 2022, 2023, 2024]
    gaming = [5.9, 7.8, 12.5, 9.1, 10.5]
    data_center = [3.0, 6.7, 10.6, 15.0, 47.5]
    pro_viz = [1.2, 1.1, 2.1, 1.5, 1.5]
    automotive = [0.7, 0.5, 0.6, 0.9, 1.1]

    fig, ax = plt.subplots(figsize=(14, 8))

    width = 0.6

    # Stacked bar chart
    p1 = ax.bar(years, data_center, width, label='Data Center', color='#76B900')
    p2 = ax.bar(years, gaming, width, bottom=data_center, label='Gaming', color='#00A3E0')
    p3 = ax.bar(years, pro_viz, width, bottom=np.array(data_center)+np.array(gaming),
               label='Professional Viz', color='#F26522')
    p4 = ax.bar(years, automotive, width,
               bottom=np.array(data_center)+np.array(gaming)+np.array(pro_viz),
               label='Automotive', color='#FFCE00')

    # Add total revenue labels on top
    totals = [a+b+c+d for a,b,c,d in zip(data_center, gaming, pro_viz, automotive)]
    for i, (year, total) in enumerate(zip(years, totals)):
        ax.text(year, total + 1.5, f'${total:.1f}B', ha='center', fontweight='bold', fontsize=11)

    # Add data center percentage labels
    for i, year in enumerate(years):
        dc_pct = (data_center[i] / totals[i]) * 100
        ax.text(year, data_center[i]/2, f'{dc_pct:.0f}%', ha='center',
               fontweight='bold', fontsize=10, color='white')

    ax.set_xlabel('Fiscal Year', fontweight='bold')
    ax.set_ylabel('Revenue (Billions USD)', fontweight='bold')
    ax.set_title('Nvidia Revenue Transformation: Gaming → AI Infrastructure\n(Data Center now 78% of revenue)',
                fontweight='bold', fontsize=15)
    ax.legend(loc='upper left', fontsize=11)
    ax.set_ylim(0, 70)
    ax.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    plt.savefig('deep_dives/NvidiaSemiconductors/charts/nvidia_revenue_segments.png', dpi=300, bbox_inches='tight')
    print("✓ Generated: nvidia_revenue_segments.png")
    plt.close()

def chart3_market_share_ai_chips(data):
    """Chart 3: AI Chip Market Share (2024 vs 2027 Projected)"""

    competitors = data['competitive_analysis']['competitor_analysis']

    # Current market share (2024)
    companies_2024 = ['Nvidia', 'AMD', 'Google TPU', 'Amazon', 'Intel', 'Others']
    shares_2024 = [92, 3, 3, 1, 1, 0]

    # Projected 2027
    companies_2027 = ['Nvidia', 'AMD', 'Google TPU', 'Amazon', 'Intel', 'Others']
    shares_2027 = [75, 8, 3, 2, 2, 10]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    colors = ['#76B900', '#ED1C24', '#4285F4', '#FF9900', '#0071C5', '#CCCCCC']

    # 2024 pie chart
    wedges1, texts1, autotexts1 = ax1.pie(shares_2024, labels=companies_2024, autopct='%1.0f%%',
                                           colors=colors, startangle=90, textprops={'fontsize': 11})
    ax1.set_title('AI Training Chip Market Share\n2024', fontweight='bold', fontsize=14)

    # Make Nvidia slice explode slightly
    wedges1[0].set_edgecolor('white')
    wedges1[0].set_linewidth(2)

    # 2027 pie chart
    wedges2, texts2, autotexts2 = ax2.pie(shares_2027, labels=companies_2027, autopct='%1.0f%%',
                                           colors=colors, startangle=90, textprops={'fontsize': 11})
    ax2.set_title('AI Training Chip Market Share\n2027 (Projected)', fontweight='bold', fontsize=14)

    wedges2[0].set_edgecolor('white')
    wedges2[0].set_linewidth(2)

    plt.suptitle('Nvidia Maintains Dominant Position Despite Rising Competition',
                fontweight='bold', fontsize=16, y=1.00)

    plt.tight_layout()
    plt.savefig('deep_dives/NvidiaSemiconductors/charts/market_share_ai_chips.png', dpi=300, bbox_inches='tight')
    print("✓ Generated: market_share_ai_chips.png")
    plt.close()

def chart4_tam_growth_projection(data):
    """Chart 4: TAM Growth and Nvidia's Opportunity"""

    tam_data = data['tam_analysis']['nvidia_tam_analysis']

    # Get top 5 segments by 2030 potential
    segments = sorted(tam_data['segments'], key=lambda x: x['nvidia_revenue_potential_2030'], reverse=True)[:6]

    segment_names = [s['segment'] for s in segments]
    tam_2024 = [s['current_tam_2024'] for s in segments]
    tam_2030 = [s['tam_2030'] for s in segments]
    nvidia_potential = [s['nvidia_revenue_potential_2030'] for s in segments]

    fig, ax = plt.subplots(figsize=(14, 9))

    x = np.arange(len(segment_names))
    width = 0.25

    # Grouped bar chart
    bars1 = ax.bar(x - width, tam_2024, width, label='TAM 2024', color='#B0BEC5', alpha=0.7)
    bars2 = ax.bar(x, tam_2030, width, label='TAM 2030', color='#546E7A', alpha=0.8)
    bars3 = ax.bar(x + width, nvidia_potential, width, label="Nvidia's Share (2030)", color='#76B900')

    # Add value labels on bars
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                ax.text(bar.get_x() + bar.get_width()/2., height + 2,
                       f'${height:.0f}B', ha='center', va='bottom', fontsize=9)

    ax.set_xlabel('Market Segment', fontweight='bold')
    ax.set_ylabel('Revenue (Billions USD)', fontweight='bold')
    ax.set_title("Nvidia's $350B+ Revenue Opportunity Across Market Segments (2030)\nCurrent Revenue: $60.9B | Potential: $354B",
                fontweight='bold', fontsize=15)
    ax.set_xticks(x)
    ax.set_xticklabels(segment_names, rotation=25, ha='right')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3, axis='y')
    ax.set_ylim(0, 280)

    plt.tight_layout()
    plt.savefig('deep_dives/NvidiaSemiconductors/charts/tam_growth_projection.png', dpi=300, bbox_inches='tight')
    print("✓ Generated: tam_growth_projection.png")
    plt.close()

def chart5_cuda_ecosystem_growth(data):
    """Chart 5: CUDA Ecosystem Growth Over Time"""

    cuda_milestones = data['gpu_performance']['cuda_ecosystem']

    years = [m['year'] for m in cuda_milestones]
    developers = [m['developers'] for m in cuda_milestones]
    applications = [m['applications'] for m in cuda_milestones]

    fig, ax1 = plt.subplots(figsize=(14, 8))

    color1 = '#76B900'
    ax1.set_xlabel('Year', fontweight='bold')
    ax1.set_ylabel('CUDA Developers (Millions)', color=color1, fontweight='bold')
    line1 = ax1.plot(years, [d/1e6 for d in developers], marker='o', linewidth=3,
                    markersize=10, color=color1, label='Developers')
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.set_ylim(0, 5)

    # Add developer count labels
    for year, dev in zip(years, developers):
        ax1.annotate(f'{dev/1e6:.1f}M', xy=(year, dev/1e6), xytext=(0, 8),
                    textcoords='offset points', ha='center', fontsize=10, fontweight='bold')

    # Second y-axis for applications
    ax2 = ax1.twinx()
    color2 = '#00A3E0'
    ax2.set_ylabel('GPU-Accelerated Applications', color=color2, fontweight='bold')
    line2 = ax2.plot(years, applications, marker='s', linewidth=3, markersize=9,
                    color=color2, linestyle='--', label='Applications')
    ax2.tick_params(axis='y', labelcolor=color2)
    ax2.set_ylim(0, 4500)

    # Add application count labels
    for year, app in zip(years, applications):
        ax2.annotate(f'{app:,}', xy=(year, app), xytext=(0, -20),
                    textcoords='offset points', ha='center', fontsize=9, color=color2)

    # Title and grid
    ax1.set_title("CUDA Ecosystem: 18 Years of Compound Growth\n(4M developers = massive switching cost)",
                 fontweight='bold', fontsize=15)
    ax1.grid(True, alpha=0.3)

    # Combined legend
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left', fontsize=12)

    plt.tight_layout()
    plt.savefig('deep_dives/NvidiaSemiconductors/charts/cuda_ecosystem_growth.png', dpi=300, bbox_inches='tight')
    print("✓ Generated: cuda_ecosystem_growth.png")
    plt.close()

def chart6_scenario_analysis(data):
    """Chart 6: Bull/Base/Bear Case Scenario Analysis"""

    scenarios = data['tam_analysis']['scenario_analysis']

    cases = ['Bear Case\n(Competition\nErodes Moat)', 'Base Case\n(Gradual Share\nLoss)',
             'Bull Case\n(AI Dominance\nContinues)']
    revenue_2030 = [scenarios['bear_case']['revenue_2030'],
                    scenarios['base_case']['revenue_2030'],
                    scenarios['bull_case']['revenue_2030']]
    stock_cagr = [scenarios['bear_case']['implied_stock_cagr'],
                  scenarios['base_case']['implied_stock_cagr'],
                  scenarios['bull_case']['implied_stock_cagr']]
    probabilities = [scenarios['bear_case']['probability'],
                     scenarios['base_case']['probability'],
                     scenarios['bull_case']['probability']]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    colors = ['#ED1C24', '#FFCE00', '#76B900']

    # Revenue chart
    bars1 = ax1.bar(cases, revenue_2030, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax1.axhline(y=60.9, color='gray', linestyle='--', linewidth=2, label='Current Revenue (FY2024)')

    for bar, rev, prob in zip(bars1, revenue_2030, probabilities):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 5,
                f'${rev}B\n({prob}% prob)', ha='center', va='bottom', fontsize=11, fontweight='bold')

    ax1.set_ylabel('2030 Revenue (Billions USD)', fontweight='bold')
    ax1.set_title('Revenue Scenarios (2030)', fontweight='bold', fontsize=14)
    ax1.set_ylim(0, 250)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3, axis='y')

    # Stock CAGR chart
    bars2 = ax2.bar(cases, stock_cagr, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)

    for bar, cagr in zip(bars2, stock_cagr):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{cagr}%', ha='center', va='bottom', fontsize=11, fontweight='bold')

    ax2.set_ylabel('Expected Stock CAGR (2024-2030)', fontweight='bold')
    ax2.set_title('Expected Returns', fontweight='bold', fontsize=14)
    ax2.set_ylim(0, 22)
    ax2.grid(True, alpha=0.3, axis='y')

    plt.suptitle('Nvidia Investment Scenarios: Risk vs Return Analysis',
                fontweight='bold', fontsize=16, y=1.00)

    plt.tight_layout()
    plt.savefig('deep_dives/NvidiaSemiconductors/charts/scenario_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Generated: scenario_analysis.png")
    plt.close()

def main():
    print("Generating Charts and Visualizations...\n")

    # Load data
    data = load_data()

    # Generate all charts
    chart1_gpu_performance_evolution(data)
    chart2_nvidia_revenue_segments(data)
    chart3_market_share_ai_chips(data)
    chart4_tam_growth_projection(data)
    chart5_cuda_ecosystem_growth(data)
    chart6_scenario_analysis(data)

    print("\n✓ All charts generated successfully!")
    print("Charts saved to: deep_dives/NvidiaSemiconductors/charts/")

if __name__ == '__main__':
    main()
