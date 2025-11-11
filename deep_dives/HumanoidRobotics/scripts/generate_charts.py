#!/usr/bin/env python3
"""
Generate visualizations for humanoid robotics investment thesis.
Charts: market cap comparison, funding timeline, production ramps, unit economics, etc.
"""

import json
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from datetime import datetime


# Chart styling
plt.style.use('seaborn-v0_8-darkgrid')
COLORS = {
    'primary': '#1f77b4',
    'secondary': '#ff7f0e',
    'success': '#2ca02c',
    'danger': '#d62728',
    'info': '#9467bd',
    'warning': '#8c564b',
    'china': '#d62728',
    'usa': '#1f77b4',
    'humanoid': '#2ca02c',
    'other': '#7f7f7f'
}


def load_data():
    """Load all JSON data files."""
    data_dir = Path(__file__).parent.parent / "data"

    data = {}
    for file_name in ["market_caps.json", "companies.json", "rare_earth_data.json", "competitive_analysis.json"]:
        file_path = data_dir / file_name
        if file_path.exists():
            with open(file_path) as f:
                key = file_name.replace(".json", "")
                data[key] = json.load(f)

    return data


def chart_market_cap_comparison(data, output_dir):
    """Chart: Market Cap Comparison - Humanoid Robotics vs Other Sectors."""
    fig, ax = plt.subplots(figsize=(12, 8))

    sectors = []
    market_caps = []
    colors_list = []

    # Get sector data from market_caps.json
    if 'market_caps' in data and 'sectors' in data['market_caps']:
        sectors_data = data['market_caps']['sectors']

        for sector, info in sectors_data.items():
            sectors.append(sector)
            market_caps.append(info['total_market_cap_trillions'])
            colors_list.append(COLORS['primary'])

    # Add Crypto
    if 'market_caps' in data and 'crypto' in data['market_caps']:
        sectors.append('Crypto')
        market_caps.append(data['market_caps']['crypto']['total_crypto_trillions'])
        colors_list.append(COLORS['warning'])

    # Add Humanoid Robotics (estimated)
    sectors.append('Humanoid Robotics')
    market_caps.append(0.01)  # $10B estimated (private companies)
    colors_list.append(COLORS['humanoid'])

    # Create bar chart
    y_pos = np.arange(len(sectors))
    ax.barh(y_pos, market_caps, color=colors_list, alpha=0.8, edgecolor='black')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(sectors, fontsize=12, fontweight='bold')
    ax.set_xlabel('Market Capitalization (Trillions USD)', fontsize=14, fontweight='bold')
    ax.set_title('Market Cap Comparison: Humanoid Robotics vs Other Tech Sectors', fontsize=16, fontweight='bold', pad=20)

    # Add value labels
    for i, v in enumerate(market_caps):
        if v >= 1:
            ax.text(v + 0.2, i, f'${v:.1f}T', va='center', fontsize=11, fontweight='bold')
        else:
            ax.text(v + 0.01, i, f'${v*1000:.0f}B', va='center', fontsize=11, fontweight='bold', color=COLORS['danger'])

    plt.tight_layout()
    plt.savefig(output_dir / "01_market_cap_comparison.png", dpi=300, bbox_inches='tight')
    plt.close()

    print("✅ Generated: 01_market_cap_comparison.png")


def chart_company_funding_timeline(data, output_dir):
    """Chart: Company Funding Timeline (last 24 months)."""
    fig, ax = plt.subplots(figsize=(14, 10))

    # Extract company funding data
    companies_data = data.get('companies', {}).get('companies', {})

    companies = []
    funding_amounts = []
    colors_list = []

    for company, info in companies_data.items():
        companies.append(company)

        # Extract funding amount (rough estimate)
        funding_str = info.get('funding', {}).get('total_raised', '0')
        amount = 0
        if '$' in funding_str:
            amount_str = funding_str.replace('$', '').replace('M', '').replace('B', '000').replace('+', '').replace('(estimated)', '').strip()
            if '(' in amount_str:
                amount_str = amount_str.split('(')[0].strip()
            try:
                if 'B' in funding_str:
                    amount = float(amount_str) * 1000
                else:
                    amount = float(amount_str.split()[0]) if amount_str else 0
            except:
                amount = 0

        funding_amounts.append(amount)

        # Color by country
        if info.get('country') == 'China':
            colors_list.append(COLORS['china'])
        elif info.get('country') == 'USA':
            colors_list.append(COLORS['usa'])
        else:
            colors_list.append(COLORS['other'])

    # Sort by funding amount
    sorted_indices = np.argsort(funding_amounts)[::-1][:10]  # Top 10
    companies = [companies[i] for i in sorted_indices]
    funding_amounts = [funding_amounts[i] for i in sorted_indices]
    colors_list = [colors_list[i] for i in sorted_indices]

    # Create horizontal bar chart
    y_pos = np.arange(len(companies))
    ax.barh(y_pos, funding_amounts, color=colors_list, alpha=0.8, edgecolor='black')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(companies, fontsize=11)
    ax.set_xlabel('Total Funding (Millions USD)', fontsize=13, fontweight='bold')
    ax.set_title('Humanoid Robotics Companies - Total Funding Raised', fontsize=15, fontweight='bold', pad=20)

    # Add value labels
    for i, v in enumerate(funding_amounts):
        ax.text(v + 10, i, f'${v:.0f}M', va='center', fontsize=10)

    # Legend
    usa_patch = mpatches.Patch(color=COLORS['usa'], label='USA')
    china_patch = mpatches.Patch(color=COLORS['china'], label='China')
    other_patch = mpatches.Patch(color=COLORS['other'], label='Other')
    ax.legend(handles=[usa_patch, china_patch, other_patch], loc='lower right', fontsize=10)

    plt.tight_layout()
    plt.savefig(output_dir / "02_company_funding.png", dpi=300, bbox_inches='tight')
    plt.close()

    print("✅ Generated: 02_company_funding.png")


def chart_unit_economics(data, output_dir):
    """Chart: Unit Economics - Robot vs Human Labor (5-year TCO)."""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Assumptions
    robot_cost = 50000  # $50K (mid-range estimate)
    robot_maintenance_annual = 5000  # $5K/year
    robot_lifespan_years = 5

    human_annual_cost = 60000  # $60K/year (salary + benefits)

    years = np.arange(0, 6)  # 0-5 years

    # Calculate cumulative costs
    robot_cumulative = [robot_cost + (robot_maintenance_annual * y) for y in years]
    human_cumulative = [human_annual_cost * y for y in years]

    ax.plot(years, robot_cumulative, marker='o', linewidth=3, markersize=8, label='Humanoid Robot', color=COLORS['success'])
    ax.plot(years, human_cumulative, marker='s', linewidth=3, markersize=8, label='Human Worker', color=COLORS['primary'])

    ax.set_xlabel('Years', fontsize=13, fontweight='bold')
    ax.set_ylabel('Cumulative Cost (USD)', fontsize=13, fontweight='bold')
    ax.set_title('5-Year Total Cost of Ownership: Robot vs Human Labor', fontsize=15, fontweight='bold', pad=20)

    # Format y-axis as currency
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

    # Add breakeven annotation
    breakeven_year = 2.5  # Approximate
    ax.axvline(x=breakeven_year, color=COLORS['danger'], linestyle='--', linewidth=2, alpha=0.7)
    ax.text(breakeven_year + 0.1, 150000, 'Breakeven\n(~2.5 years)', fontsize=11, color=COLORS['danger'], fontweight='bold')

    ax.legend(fontsize=12, loc='upper left')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_dir / "03_unit_economics_tco.png", dpi=300, bbox_inches='tight')
    plt.close()

    print("✅ Generated: 03_unit_economics_tco.png")


def chart_ree_supply_chain(data, output_dir):
    """Chart: REE Production by Country (pie chart)."""
    fig, ax = plt.subplots(figsize=(10, 8))

    # Get REE data
    ree_data = data.get('rare_earth_data', {}).get('production_by_country', {})

    countries = []
    shares = []
    colors_list = []

    for country, info in ree_data.items():
        countries.append(country)
        share_str = info['global_share'].replace('%', '')
        shares.append(float(share_str))

        if country == 'China':
            colors_list.append(COLORS['china'])
        elif country == 'USA':
            colors_list.append(COLORS['usa'])
        else:
            colors_list.append(COLORS['other'])

    # Create pie chart
    wedges, texts, autotexts = ax.pie(shares, labels=countries, autopct='%1.1f%%',
                                        colors=colors_list, startangle=90,
                                        textprops={'fontsize': 12, 'fontweight': 'bold'},
                                        explode=[0.1 if c == 'China' else 0 for c in countries])

    ax.set_title('Global Rare Earth Elements Production Share (2024)', fontsize=15, fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig(output_dir / "04_ree_production_share.png", dpi=300, bbox_inches='tight')
    plt.close()

    print("✅ Generated: 04_ree_production_share.png")


def chart_market_segments_tam(data, output_dir):
    """Chart: Market Segments TAM (2025 vs 2030)."""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Get competitive analysis data
    segments_data = data.get('competitive_analysis', {}).get('market_segments', {})

    segments = []
    tam_2025 = []
    tam_2030 = []

    for segment, info in segments_data.items():
        segments.append(segment.replace('_', ' '))

        # Extract 2025 TAM
        tam_2025_str = info['market_size_2025'].replace('$', '').replace('B', '').replace('M', '').replace('(nascent)', '').replace('<', '').strip()
        tam_2025_val = float(tam_2025_str) if tam_2025_str else 0
        tam_2025.append(tam_2025_val)

        # Extract 2030 TAM
        tam_2030_str = info['market_size_2030'].replace('$', '').replace('B (projected)', '').replace('B (speculative)', '').replace('B', '').strip()
        tam_2030_val = float(tam_2030_str) if tam_2030_str else 0
        tam_2030.append(tam_2030_val)

    # Create grouped bar chart
    x = np.arange(len(segments))
    width = 0.35

    ax.bar(x - width/2, tam_2025, width, label='2025', color=COLORS['primary'], alpha=0.8, edgecolor='black')
    ax.bar(x + width/2, tam_2030, width, label='2030 (Projected)', color=COLORS['success'], alpha=0.8, edgecolor='black')

    ax.set_ylabel('Total Addressable Market (Billions USD)', fontsize=13, fontweight='bold')
    ax.set_title('Humanoid Robotics Market Segments - TAM Growth (2025 vs 2030)', fontsize=15, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(segments, rotation=15, ha='right', fontsize=10)
    ax.legend(fontsize=12)

    # Add value labels
    for i, v in enumerate(tam_2025):
        ax.text(i - width/2, v + 1, f'${v:.1f}B', ha='center', va='bottom', fontsize=9)
    for i, v in enumerate(tam_2030):
        ax.text(i + width/2, v + 1, f'${v:.0f}B', ha='center', va='bottom', fontsize=9, fontweight='bold')

    plt.tight_layout()
    plt.savefig(output_dir / "05_market_segments_tam.png", dpi=300, bbox_inches='tight')
    plt.close()

    print("✅ Generated: 05_market_segments_tam.png")


def main():
    """Main execution."""
    print("=" * 80)
    print("Generate Charts for Humanoid Robotics Investment Thesis")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 80)

    # Output directory
    output_dir = Path(__file__).parent.parent / "charts"
    output_dir.mkdir(exist_ok=True)

    # Load data
    print("\n📊 Loading data...")
    data = load_data()

    # Generate charts
    print("\n🎨 Generating charts...\n")

    if 'market_caps' in data:
        chart_market_cap_comparison(data, output_dir)

    if 'companies' in data:
        chart_company_funding_timeline(data, output_dir)

    chart_unit_economics(data, output_dir)

    if 'rare_earth_data' in data:
        chart_ree_supply_chain(data, output_dir)

    if 'competitive_analysis' in data:
        chart_market_segments_tam(data, output_dir)

    print(f"\n✅ All charts saved to: {output_dir}")
    print("\nCharts generated:")
    print("  1. Market cap comparison (Humanoid vs AI/Semiconductors/etc.)")
    print("  2. Company funding comparison")
    print("  3. Unit economics (Robot vs Human labor 5-year TCO)")
    print("  4. REE production by country")
    print("  5. Market segments TAM growth (2025 vs 2030)")


if __name__ == "__main__":
    main()
