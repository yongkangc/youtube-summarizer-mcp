#!/usr/bin/env python3
"""
Fetch current market data for Nvidia and related companies.
Uses yfinance for stock data.
"""

import json
import os
from datetime import datetime

try:
    import yfinance as yf
except ImportError:
    print("yfinance not installed. Run: uv add yfinance")
    exit(1)

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(DATA_DIR, exist_ok=True)


def fetch_nvidia_data():
    """Fetch Nvidia stock and financial data."""
    print("Fetching Nvidia (NVDA) data...")
    nvda = yf.Ticker("NVDA")

    info = nvda.info

    data = {
        "symbol": "NVDA",
        "name": info.get("longName", "NVIDIA Corporation"),
        "fetched_at": datetime.now().isoformat(),
        "market_data": {
            "market_cap": info.get("marketCap"),
            "current_price": info.get("currentPrice"),
            "52_week_high": info.get("fiftyTwoWeekHigh"),
            "52_week_low": info.get("fiftyTwoWeekLow"),
            "pe_ratio": info.get("trailingPE"),
            "forward_pe": info.get("forwardPE"),
            "price_to_book": info.get("priceToBook"),
            "ev_to_revenue": info.get("enterpriseToRevenue"),
            "ev_to_ebitda": info.get("enterpriseToEbitda"),
        },
        "financials": {
            "revenue_ttm": info.get("totalRevenue"),
            "gross_margins": info.get("grossMargins"),
            "operating_margins": info.get("operatingMargins"),
            "profit_margins": info.get("profitMargins"),
            "free_cash_flow": info.get("freeCashflow"),
        },
        "growth": {
            "revenue_growth": info.get("revenueGrowth"),
            "earnings_growth": info.get("earningsGrowth"),
        },
        "data_center_context": {
            "note": "Data center revenue was $47.5B in FY2024, representing 78% of total revenue",
            "yoy_growth_fy2024": 2.17,
            "market_share_training": 0.92,
        }
    }

    return data


def fetch_amd_data():
    """Fetch AMD stock data for comparison."""
    print("Fetching AMD data...")
    amd = yf.Ticker("AMD")

    info = amd.info

    data = {
        "symbol": "AMD",
        "name": info.get("longName", "Advanced Micro Devices"),
        "fetched_at": datetime.now().isoformat(),
        "market_data": {
            "market_cap": info.get("marketCap"),
            "current_price": info.get("currentPrice"),
            "pe_ratio": info.get("trailingPE"),
            "forward_pe": info.get("forwardPE"),
        },
        "financials": {
            "revenue_ttm": info.get("totalRevenue"),
            "gross_margins": info.get("grossMargins"),
            "operating_margins": info.get("operatingMargins"),
        },
        "data_center_context": {
            "note": "Data center GPU revenue was $5B+ in 2024",
            "mi300x_price_usd": [10000, 15000],
        }
    }

    return data


def fetch_semiconductor_etf():
    """Fetch semiconductor ETF for sector context."""
    print("Fetching SMH (VanEck Semiconductor ETF) data...")
    smh = yf.Ticker("SMH")

    info = smh.info

    data = {
        "symbol": "SMH",
        "name": "VanEck Semiconductor ETF",
        "fetched_at": datetime.now().isoformat(),
        "market_data": {
            "current_price": info.get("previousClose"),
            "52_week_high": info.get("fiftyTwoWeekHigh"),
            "52_week_low": info.get("fiftyTwoWeekLow"),
            "ytd_return": info.get("ytdReturn"),
        }
    }

    return data


def main():
    """Fetch all market data and save to JSON."""
    print("\n" + "="*60)
    print("Fetching Market Data for Nvidia-Groq Analysis")
    print("="*60 + "\n")

    all_data = {
        "nvidia": fetch_nvidia_data(),
        "amd": fetch_amd_data(),
        "semiconductor_sector": fetch_semiconductor_etf(),
    }

    # Save combined data
    output_file = os.path.join(DATA_DIR, 'market_data.json')
    with open(output_file, 'w') as f:
        json.dump(all_data, f, indent=2, default=str)

    print(f"\nSaved market data to: {output_file}")

    # Print summary
    print("\n" + "="*60)
    print("Summary")
    print("="*60)
    nvda = all_data["nvidia"]["market_data"]
    print(f"Nvidia Market Cap: ${nvda['market_cap']:,.0f}" if nvda['market_cap'] else "N/A")
    print(f"Nvidia P/E: {nvda['pe_ratio']:.2f}" if nvda['pe_ratio'] else "N/A")
    print(f"Nvidia Price: ${nvda['current_price']:.2f}" if nvda['current_price'] else "N/A")


if __name__ == '__main__':
    main()
