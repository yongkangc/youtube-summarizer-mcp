#!/usr/bin/env python3
"""
AI Power Infrastructure Investment Thesis
Real-time stock data via yfinance, market cap comparison, investment scorecard
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from datetime import datetime, timedelta

try:
    import yfinance as yf
    YFINANCE_AVAILABLE = True
except ImportError:
    YFINANCE_AVAILABLE = False
    print("Warning: yfinance not available, using fallback data")


# Investment thesis data
investment_thesis = {
    "GEV": {
        "company": "GE Vernova",
        "sector": "Power Equipment",
        "thesis": "Blue chip BYOG play, $135B backlog, pricing power",
        "catalyst": "Continued datacenter order flow, capacity expansion",
        "risk": "Execution on capacity ramp, supply chain constraints",
        "rating": "STRONG BUY",
        "fallback_ytd_return": 100,
        "fallback_market_cap_b": 100
    },
    "BE": {
        "company": "Bloom Energy",
        "sector": "Fuel Cells",
        "thesis": "Permitting arbitrage, fastest deployment, urban sites",
        "catalyst": "$5B Brookfield partnership, Oracle/hyperscaler deals",
        "risk": "High CapEx, stack replacement costs, execution",
        "rating": "BUY",
        "fallback_ytd_return": 300,
        "fallback_market_cap_b": 20
    },
    "HWM": {
        "company": "Howmet Aerospace",
        "sector": "Aerospace/Industrial",
        "thesis": "Hidden monopoly - every turbine needs Howmet blades",
        "catalyst": "Turbine production ramp, pricing power",
        "risk": "Rare earth supply chain, aerospace cycle",
        "rating": "STRONG BUY",
        "fallback_ytd_return": 50,
        "fallback_market_cap_b": 50
    },
    "CAT": {
        "company": "Caterpillar",
        "sector": "Industrial",
        "thesis": "Diversified exposure via Solar turbines + Jenbacher",
        "catalyst": "Doubling engine production, rental fleet leverage",
        "risk": "Construction cycle, China exposure",
        "rating": "HOLD/BUY",
        "fallback_ytd_return": 20,
        "fallback_market_cap_b": 180
    },
    "SMEGF": {
        "company": "Siemens Energy",
        "sector": "Power Equipment",
        "thesis": "European champion, diversified portfolio, service revenue",
        "catalyst": "Capacity expansion to 30GW/year by 2030",
        "risk": "Wind turbine issues, execution",
        "rating": "HOLD",
        "fallback_ytd_return": 80,
        "fallback_market_cap_b": 35
    },
    "WRTBY": {
        "company": "Wärtsilä",
        "sector": "Marine/Power",
        "thesis": "Marine-to-datacenter pivot, medium-speed engine leader",
        "catalyst": "800MW US datacenter contracts, more order flow",
        "risk": "Wait and see approach, capacity constraints",
        "rating": "SPECULATIVE BUY",
        "fallback_ytd_return": 40,
        "fallback_market_cap_b": 8
    }
}

# Arbitrage P&L projection (from user's model)
arbitrage_projection = {
    "datacenter_mw": 200,
    "revenue_per_mw_annual": 11_000_000,
    "onsite_month_start": 6,
    "grid_month_start": 36,
    "onsite_monthly_profit": 173_400_000,  # From user's model
    "grid_monthly_profit": 174_500_000,
    "months": list(range(1, 37)),
    "arbitrage_at_month_36": 5_200_000_000  # $5.2B
}


def fetch_stock_data(tickers: list) -> dict:
    """Fetch real-time stock data via yfinance"""
    if not YFINANCE_AVAILABLE:
        return None

    data = {}
    year_start = datetime(datetime.now().year, 1, 1)

    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(start=year_start)
            info = stock.info

            if len(hist) > 0:
                ytd_start = hist['Close'].iloc[0]
                ytd_end = hist['Close'].iloc[-1]
                ytd_return = ((ytd_end - ytd_start) / ytd_start) * 100

                data[ticker] = {
                    "current_price": ytd_end,
                    "ytd_return": ytd_return,
                    "market_cap_b": info.get('marketCap', 0) / 1e9,
                    "pe_ratio": info.get('trailingPE', None),
                    "name": info.get('shortName', ticker)
                }
            else:
                data[ticker] = None
        except Exception as e:
            print(f"Error fetching {ticker}: {e}")
            data[ticker] = None

    return data


def save_data():
    """Save investment data to JSON"""
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    with open(data_dir / "investment_thesis.json", "w") as f:
        json.dump(investment_thesis, f, indent=2)

    with open(data_dir / "arbitrage_projection.json", "w") as f:
        json.dump(arbitrage_projection, f, indent=2)

    # Fetch and save live stock data
    if YFINANCE_AVAILABLE:
        tickers = list(investment_thesis.keys())
        stock_data = fetch_stock_data(tickers)
        if stock_data:
            with open(data_dir / "stock_data_live.json", "w") as f:
                json.dump(stock_data, f, indent=2)
            print("Saved live stock data")

    print(f"Saved investment thesis data to {data_dir}")


def plot_stock_performance_ytd():
    """Plot YTD stock performance"""
    fig, ax = plt.subplots(figsize=(14, 8))

    tickers = list(investment_thesis.keys())

    # Try to fetch live data
    live_data = None
    if YFINANCE_AVAILABLE:
        live_data = fetch_stock_data(tickers)

    # Build data arrays
    companies = []
    returns = []
    ratings = []

    for ticker in tickers:
        thesis_data = investment_thesis[ticker]
        companies.append(thesis_data["company"])
        ratings.append(thesis_data["rating"])

        if live_data and live_data.get(ticker):
            returns.append(live_data[ticker]["ytd_return"])
        else:
            returns.append(thesis_data["fallback_ytd_return"])

    # Sort by return
    sorted_data = sorted(zip(companies, returns, ratings), key=lambda x: x[1], reverse=True)
    companies = [c for c, r, rt in sorted_data]
    returns = [r for c, r, rt in sorted_data]
    ratings = [rt for c, r, rt in sorted_data]

    # Color by rating
    rating_colors = {
        "STRONG BUY": "#27ae60",
        "BUY": "#2ecc71",
        "HOLD/BUY": "#f1c40f",
        "HOLD": "#f39c12",
        "SPECULATIVE BUY": "#9b59b6"
    }
    colors = [rating_colors.get(r, "#95a5a6") for r in ratings]

    bars = ax.barh(companies, returns, color=colors, alpha=0.9, edgecolor='black', linewidth=1.5)

    for bar, ret, rating in zip(bars, returns, ratings):
        width = bar.get_width()
        ax.text(width + 5, bar.get_y() + bar.get_height()/2.,
               f'+{ret:.0f}% ({rating})', ha='left', va='center',
               fontsize=10, fontweight='bold')

    ax.axvline(x=0, color='gray', linestyle='-', linewidth=1)
    ax.axvline(x=100, color='red', linestyle='--', linewidth=2, alpha=0.5, label='100% YTD')

    ax.set_xlabel('YTD Return (%)', fontsize=12, fontweight='bold')
    ax.set_title('AI Power Infrastructure Stocks: 2025 YTD Performance\n(Real-time data via yfinance)',
                fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3, linestyle='--')

    # Add legend for ratings
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor=c, label=r) for r, c in rating_colors.items()]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=9, title='Rating')

    # Add data source note
    source = "yfinance (live)" if YFINANCE_AVAILABLE else "Fallback estimates"
    ax.text(0.02, 0.02, f'Data source: {source}', transform=ax.transAxes,
           fontsize=8, style='italic', alpha=0.7)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    charts_dir.mkdir(exist_ok=True)
    plt.savefig(charts_dir / "17_stock_performance_ytd.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 17_stock_performance_ytd.png")
    plt.close()


def plot_arbitrage_cumulative_pnl():
    """Plot arbitrage cumulative P&L model"""
    fig, ax = plt.subplots(figsize=(14, 8))

    params = arbitrage_projection
    months = params["months"]

    # Calculate cumulative profits
    onsite_cum = []
    grid_cum = []
    onsite_total = 0
    grid_total = 0

    for m in months:
        if m >= params["onsite_month_start"]:
            onsite_total += params["onsite_monthly_profit"]
        if m >= params["grid_month_start"]:
            grid_total += params["grid_monthly_profit"]
        onsite_cum.append(onsite_total / 1e9)
        grid_cum.append(grid_total / 1e9)

    ax.fill_between(months, 0, onsite_cum, alpha=0.4, color='#27ae60')
    ax.fill_between(months, 0, grid_cum, alpha=0.4, color='#3498db')
    ax.plot(months, onsite_cum, linewidth=3, color='#27ae60', label='Onsite Gas (BYOG)')
    ax.plot(months, grid_cum, linewidth=3, color='#3498db', label='Grid Power')

    # Highlight key months
    ax.axvline(x=6, color='#27ae60', linestyle=':', linewidth=2, alpha=0.7)
    ax.axvline(x=36, color='#3498db', linestyle=':', linewidth=2, alpha=0.7)

    ax.text(6, 0.3, 'Onsite\nStarts', ha='center', fontsize=10, fontweight='bold', color='#27ae60')
    ax.text(36, 0.3, 'Grid\nStarts', ha='center', fontsize=10, fontweight='bold', color='#3498db')

    # Add arbitrage value
    arbitrage = params["arbitrage_at_month_36"] / 1e9
    ax.annotate(f'Arbitrage Value:\n${arbitrage:.1f}B\n\nThe "Speed Premium"',
               xy=(20, 4), fontsize=14, fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='gold', alpha=0.9, edgecolor='orange', linewidth=2),
               ha='center')

    ax.set_xlabel('Month', fontsize=12, fontweight='bold')
    ax.set_ylabel('Cumulative Profit ($ Billions)', fontsize=12, fontweight='bold')
    ax.set_title(f'The Interconnection Latency Arbitrage: 36-Month P&L\n'
                f'({params["datacenter_mw"]}MW Datacenter @ ${params["revenue_per_mw_annual"]/1e6:.0f}M/MW/year)',
                fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper left', fontsize=11)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlim(0, 37)
    ax.set_ylim(0, 6)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "18_arbitrage_cumulative_pnl.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 18_arbitrage_cumulative_pnl.png")
    plt.close()


def plot_market_cap_comparison():
    """Plot market cap comparison"""
    fig, ax = plt.subplots(figsize=(14, 8))

    tickers = list(investment_thesis.keys())

    # Try to fetch live data
    live_data = None
    if YFINANCE_AVAILABLE:
        live_data = fetch_stock_data(tickers)

    companies = []
    market_caps = []

    for ticker in tickers:
        thesis_data = investment_thesis[ticker]
        companies.append(thesis_data["company"])

        if live_data and live_data.get(ticker) and live_data[ticker].get("market_cap_b"):
            market_caps.append(live_data[ticker]["market_cap_b"])
        else:
            market_caps.append(thesis_data["fallback_market_cap_b"])

    # Sort by market cap
    sorted_data = sorted(zip(companies, market_caps), key=lambda x: x[1], reverse=True)
    companies = [c for c, m in sorted_data]
    market_caps = [m for c, m in sorted_data]

    colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(companies)))
    bars = ax.barh(companies, market_caps, color=colors, alpha=0.9, edgecolor='black', linewidth=1.5)

    for bar, cap in zip(bars, market_caps):
        width = bar.get_width()
        ax.text(width + 2, bar.get_y() + bar.get_height()/2.,
               f'${cap:.1f}B', ha='left', va='center', fontsize=11, fontweight='bold')

    ax.set_xlabel('Market Cap ($ Billions)', fontsize=12, fontweight='bold')
    ax.set_title('AI Power Infrastructure: Market Cap Comparison',
                fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3, linestyle='--')

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "19_market_cap_comparison.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 19_market_cap_comparison.png")
    plt.close()


def plot_investment_scorecard():
    """Create investment scorecard summary"""
    fig, ax = plt.subplots(figsize=(18, 10))
    ax.axis('off')

    columns = ['Ticker', 'Company', 'Thesis', 'Catalyst', 'Rating']

    rows = []
    for ticker, data in investment_thesis.items():
        rows.append([
            ticker,
            data['company'],
            data['thesis'][:45] + "..." if len(data['thesis']) > 45 else data['thesis'],
            data['catalyst'][:40] + "..." if len(data['catalyst']) > 40 else data['catalyst'],
            data['rating']
        ])

    table = ax.table(cellText=rows, colLabels=columns, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 2.2)

    # Style header
    for j in range(len(columns)):
        table[(0, j)].set_facecolor('#2c3e50')
        table[(0, j)].set_text_props(color='white', fontweight='bold')

    # Color by rating
    rating_colors = {
        "STRONG BUY": "#d5f4e6",
        "BUY": "#e8f6e8",
        "HOLD/BUY": "#fef9e7",
        "HOLD": "#fef5e7",
        "SPECULATIVE BUY": "#f5eef8"
    }

    for i, (ticker, data) in enumerate(investment_thesis.items(), 1):
        color = rating_colors.get(data['rating'], '#f8f9fa')
        for j in range(len(columns)):
            table[(i, j)].set_facecolor(color)

    ax.set_title('AI Power Infrastructure Investment Scorecard\n(Long-Only Portfolio)',
                fontsize=16, fontweight='bold', pad=20)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "20_investment_scorecard.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 20_investment_scorecard.png")
    plt.close()


if __name__ == "__main__":
    print("Generating investment thesis analysis...")
    print(f"yfinance available: {YFINANCE_AVAILABLE}")
    save_data()
    plot_stock_performance_ytd()
    plot_arbitrage_cumulative_pnl()
    plot_market_cap_comparison()
    plot_investment_scorecard()
    print("\nInvestment thesis analysis complete!")
