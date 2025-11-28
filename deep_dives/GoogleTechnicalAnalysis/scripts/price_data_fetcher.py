#!/usr/bin/env python3
"""
Fetch historical price data for Google (GOOGL) stock.
Saves data to JSON for analysis and generates initial price chart.
"""

import yfinance as yf
import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def fetch_google_data(period="2y"):
    """
    Fetch Google stock data using yfinance.

    Args:
        period: Time period to fetch (default: 2 years for good technical analysis)

    Returns:
        DataFrame with OHLCV data
    """
    ticker = yf.Ticker("GOOGL")
    data = ticker.history(period=period)
    return data

def save_price_data(data, filepath="../data/google_price_data.json"):
    """Save price data to JSON format."""
    # Convert to JSON-serializable format
    data_dict = {
        "ticker": "GOOGL",
        "fetch_date": datetime.now().isoformat(),
        "period": "2y",
        "data": []
    }

    for date, row in data.iterrows():
        data_dict["data"].append({
            "date": date.strftime("%Y-%m-%d"),
            "open": round(row["Open"], 2),
            "high": round(row["High"], 2),
            "low": round(row["Low"], 2),
            "close": round(row["Close"], 2),
            "volume": int(row["Volume"])
        })

    with open(filepath, 'w') as f:
        json.dump(data_dict, f, indent=2)

    print(f"Price data saved to {filepath}")
    print(f"Total trading days: {len(data_dict['data'])}")
    print(f"Date range: {data_dict['data'][0]['date']} to {data_dict['data'][-1]['date']}")
    print(f"Current price: ${data_dict['data'][-1]['close']}")
    print(f"52-week high: ${max(d['high'] for d in data_dict['data'][-252:])}")
    print(f"52-week low: ${min(d['low'] for d in data_dict['data'][-252:])}")

def plot_price_chart(data, filepath="../charts/google_price_chart.png"):
    """Generate candlestick-style price chart."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10),
                                     gridspec_kw={'height_ratios': [3, 1]})

    # Price chart
    dates = data.index
    ax1.plot(dates, data['Close'], label='Close Price', color='#1a73e8', linewidth=2)
    ax1.fill_between(dates, data['Low'], data['High'], alpha=0.2, color='#1a73e8')

    # 50 and 200 day moving averages
    ma50 = data['Close'].rolling(window=50).mean()
    ma200 = data['Close'].rolling(window=200).mean()
    ax1.plot(dates, ma50, label='50-day MA', color='orange', linewidth=1.5, linestyle='--')
    ax1.plot(dates, ma200, label='200-day MA', color='red', linewidth=1.5, linestyle='--')

    ax1.set_title('GOOGL - 2 Year Price History', fontsize=16, fontweight='bold', pad=20)
    ax1.set_ylabel('Price ($)', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper left', framealpha=0.9)
    ax1.grid(True, alpha=0.3)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    # Volume chart
    colors = ['green' if data['Close'].iloc[i] >= data['Open'].iloc[i] else 'red'
              for i in range(len(data))]
    ax2.bar(dates, data['Volume'], color=colors, alpha=0.6, width=1)
    ax2.set_ylabel('Volume', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    plt.tight_layout()
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f"Price chart saved to {filepath}")
    plt.close()

def get_current_stats(data):
    """Calculate and return current key statistics."""
    current_price = data['Close'].iloc[-1]

    # Recent performance
    day_change = ((data['Close'].iloc[-1] / data['Close'].iloc[-2]) - 1) * 100
    week_change = ((data['Close'].iloc[-1] / data['Close'].iloc[-5]) - 1) * 100
    month_change = ((data['Close'].iloc[-1] / data['Close'].iloc[-21]) - 1) * 100
    ytd_start = data[data.index >= f"{datetime.now().year}-01-01"]['Close'].iloc[0]
    ytd_change = ((data['Close'].iloc[-1] / ytd_start) - 1) * 100

    # 52-week stats
    week_52_high = data['High'].iloc[-252:].max()
    week_52_low = data['Low'].iloc[-252:].min()

    # Volatility (30-day)
    returns = data['Close'].pct_change()
    volatility_30d = returns.iloc[-30:].std() * (252 ** 0.5) * 100  # Annualized

    stats = {
        "current_price": round(current_price, 2),
        "day_change_pct": round(day_change, 2),
        "week_change_pct": round(week_change, 2),
        "month_change_pct": round(month_change, 2),
        "ytd_change_pct": round(ytd_change, 2),
        "52_week_high": round(week_52_high, 2),
        "52_week_low": round(week_52_low, 2),
        "distance_from_52w_high_pct": round(((current_price / week_52_high) - 1) * 100, 2),
        "distance_from_52w_low_pct": round(((current_price / week_52_low) - 1) * 100, 2),
        "volatility_30d_annualized": round(volatility_30d, 2)
    }

    return stats

if __name__ == "__main__":
    print("Fetching Google (GOOGL) price data...")
    data = fetch_google_data(period="2y")

    print("\nCurrent Statistics:")
    stats = get_current_stats(data)
    for key, value in stats.items():
        print(f"  {key}: {value}")

    # Save to JSON
    save_price_data(data)

    # Save stats
    with open("../data/google_current_stats.json", 'w') as f:
        json.dump(stats, f, indent=2)

    # Generate chart
    plot_price_chart(data)

    print("\n✓ Price data fetch complete!")
