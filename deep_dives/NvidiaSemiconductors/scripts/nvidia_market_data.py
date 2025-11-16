#!/usr/bin/env python3
"""
Nvidia Market Data Collection Script
Fetches real-time market data for Nvidia and semiconductor competitors
"""

import yfinance as yf
import json
from datetime import datetime, timedelta

def get_market_data():
    """Fetch current market data for Nvidia and competitors"""

    tickers = {
        'NVDA': 'Nvidia',
        'AMD': 'AMD',
        'INTC': 'Intel',
        'TSM': 'TSMC',
        'AVGO': 'Broadcom',
        'QCOM': 'Qualcomm',
        'TXN': 'Texas Instruments',
        'MU': 'Micron'
    }

    data = {}

    for ticker, name in tickers.items():
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            hist = stock.history(period="5y")

            # Calculate 5-year return
            if len(hist) > 0:
                start_price = hist['Close'].iloc[0]
                current_price = hist['Close'].iloc[-1]
                five_year_return = ((current_price - start_price) / start_price) * 100
            else:
                five_year_return = None

            data[ticker] = {
                'name': name,
                'current_price': info.get('currentPrice', 'N/A'),
                'market_cap': info.get('marketCap', 'N/A'),
                'pe_ratio': info.get('forwardPE', info.get('trailingPE', 'N/A')),
                'revenue': info.get('totalRevenue', 'N/A'),
                'gross_margin': info.get('grossMargins', 'N/A'),
                'operating_margin': info.get('operatingMargins', 'N/A'),
                'five_year_return': round(five_year_return, 2) if five_year_return else 'N/A',
                'sector': info.get('sector', 'N/A'),
                'industry': info.get('industry', 'N/A')
            }

            print(f"✓ Fetched data for {name} ({ticker})")

        except Exception as e:
            print(f"✗ Error fetching {ticker}: {e}")
            data[ticker] = {'name': name, 'error': str(e)}

    return data

def get_nvidia_historical_revenue():
    """Fetch Nvidia's historical revenue data"""

    nvda = yf.Ticker('NVDA')

    # Get quarterly financials
    quarterly = nvda.quarterly_financials

    revenue_data = []

    if quarterly is not None and 'Total Revenue' in quarterly.index:
        revenues = quarterly.loc['Total Revenue']

        for date, revenue in revenues.items():
            revenue_data.append({
                'date': date.strftime('%Y-%m-%d'),
                'revenue': float(revenue),
                'revenue_billions': round(float(revenue) / 1e9, 2)
            })

    # Sort by date
    revenue_data.sort(key=lambda x: x['date'])

    return revenue_data

def get_nvidia_segments():
    """Historical segment data (manual entry based on Nvidia's reported data)"""

    # Data from Nvidia's FY reports
    segments = [
        {
            'fiscal_year': 2020,
            'gaming': 5.9,
            'data_center': 3.0,
            'professional_visualization': 1.2,
            'automotive': 0.7,
            'oem_other': 0.1,
            'total': 10.9
        },
        {
            'fiscal_year': 2021,
            'gaming': 7.8,
            'data_center': 6.7,
            'professional_visualization': 1.1,
            'automotive': 0.5,
            'oem_other': 0.6,
            'total': 16.7
        },
        {
            'fiscal_year': 2022,
            'gaming': 12.5,
            'data_center': 10.6,
            'professional_visualization': 2.1,
            'automotive': 0.6,
            'oem_other': 1.1,
            'total': 26.9
        },
        {
            'fiscal_year': 2023,
            'gaming': 9.1,
            'data_center': 15.0,
            'professional_visualization': 1.5,
            'automotive': 0.9,
            'oem_other': 0.4,
            'total': 26.9
        },
        {
            'fiscal_year': 2024,
            'gaming': 10.5,
            'data_center': 47.5,
            'professional_visualization': 1.5,
            'automotive': 1.1,
            'oem_other': 0.3,
            'total': 60.9
        }
    ]

    return segments

def main():
    print("Fetching Nvidia and Semiconductor Market Data...\n")

    # Get market data
    market_data = get_market_data()

    # Get Nvidia historical revenue
    print("\nFetching Nvidia historical revenue...")
    revenue_data = get_nvidia_historical_revenue()

    # Get segment data
    segment_data = get_nvidia_segments()

    # Combine all data
    output = {
        'generated_at': datetime.now().isoformat(),
        'market_data': market_data,
        'nvidia_quarterly_revenue': revenue_data,
        'nvidia_segment_revenue': segment_data
    }

    # Save to JSON
    output_file = 'deep_dives/NvidiaSemiconductors/data/market_data.json'
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\n✓ Data saved to {output_file}")

    # Print summary
    print("\n=== MARKET CAP COMPARISON ===")
    sorted_companies = sorted(
        [(k, v) for k, v in market_data.items() if 'market_cap' in v and v['market_cap'] != 'N/A'],
        key=lambda x: x[1]['market_cap'],
        reverse=True
    )

    for ticker, data in sorted_companies:
        market_cap_b = data['market_cap'] / 1e9
        print(f"{data['name']:20} ${market_cap_b:,.0f}B")

    print("\n=== NVIDIA SEGMENT GROWTH ===")
    for segment in segment_data[-3:]:  # Last 3 years
        dc_pct = (segment['data_center'] / segment['total']) * 100
        print(f"FY{segment['fiscal_year']}: Data Center = ${segment['data_center']}B ({dc_pct:.1f}% of total)")

if __name__ == '__main__':
    main()
