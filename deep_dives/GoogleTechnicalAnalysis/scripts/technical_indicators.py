#!/usr/bin/env python3
"""
Calculate technical indicators for Google stock:
- Moving Averages (SMA, EMA)
- RSI (Relative Strength Index)
- MACD (Moving Average Convergence Divergence)
- Bollinger Bands
- ATR (Average True Range)
"""

import yfinance as yf
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def calculate_rsi(prices, period=14):
    """Calculate RSI (Relative Strength Index)."""
    deltas = np.diff(prices)
    seed = deltas[:period+1]
    up = seed[seed >= 0].sum()/period
    down = -seed[seed < 0].sum()/period
    rs = up/down if down != 0 else 0
    rsi = np.zeros_like(prices)
    rsi[:period] = 100. - 100./(1. + rs)

    for i in range(period, len(prices)):
        delta = deltas[i - 1]
        if delta > 0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up * (period - 1) + upval) / period
        down = (down * (period - 1) + downval) / period
        rs = up/down if down != 0 else 0
        rsi[i] = 100. - 100./(1. + rs)

    return rsi

def calculate_macd(prices, fast=12, slow=26, signal=9):
    """Calculate MACD and signal line."""
    ema_fast = prices.ewm(span=fast, adjust=False).mean()
    ema_slow = prices.ewm(span=slow, adjust=False).mean()
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()
    histogram = macd_line - signal_line
    return macd_line, signal_line, histogram

def calculate_bollinger_bands(prices, period=20, num_std=2):
    """Calculate Bollinger Bands."""
    sma = prices.rolling(window=period).mean()
    std = prices.rolling(window=period).std()
    upper_band = sma + (std * num_std)
    lower_band = sma - (std * num_std)
    return upper_band, sma, lower_band

def calculate_atr(data, period=14):
    """Calculate Average True Range."""
    high = data['High']
    low = data['Low']
    close = data['Close']

    tr1 = high - low
    tr2 = abs(high - close.shift())
    tr3 = abs(low - close.shift())
    tr = np.maximum(tr1, np.maximum(tr2, tr3))
    atr = tr.rolling(window=period).mean()
    return atr

def analyze_indicators(data):
    """Calculate all technical indicators and generate analysis."""
    # Moving Averages
    ma20 = data['Close'].rolling(window=20).mean()
    ma50 = data['Close'].rolling(window=50).mean()
    ma100 = data['Close'].rolling(window=100).mean()
    ma200 = data['Close'].rolling(window=200).mean()
    ema12 = data['Close'].ewm(span=12, adjust=False).mean()
    ema26 = data['Close'].ewm(span=26, adjust=False).mean()

    # RSI
    rsi = calculate_rsi(data['Close'].values)

    # MACD
    macd_line, signal_line, histogram = calculate_macd(data['Close'])

    # Bollinger Bands
    bb_upper, bb_middle, bb_lower = calculate_bollinger_bands(data['Close'])

    # ATR
    atr = calculate_atr(data)

    # Current values
    current_price = data['Close'].iloc[-1]
    current_rsi = rsi[-1]
    current_macd = macd_line.iloc[-1]
    current_signal = signal_line.iloc[-1]
    current_bb_upper = bb_upper.iloc[-1]
    current_bb_lower = bb_lower.iloc[-1]
    current_atr = atr.iloc[-1]

    # Trend analysis
    trend_signals = {
        "price_vs_ma20": "bullish" if current_price > ma20.iloc[-1] else "bearish",
        "price_vs_ma50": "bullish" if current_price > ma50.iloc[-1] else "bearish",
        "price_vs_ma200": "bullish" if current_price > ma200.iloc[-1] else "bearish",
        "ma50_vs_ma200": "bullish" if ma50.iloc[-1] > ma200.iloc[-1] else "bearish",
        "rsi_signal": "oversold" if current_rsi < 30 else "overbought" if current_rsi > 70 else "neutral",
        "macd_signal": "bullish" if current_macd > current_signal else "bearish",
        "bb_position": "upper" if current_price > bb_middle.iloc[-1] else "lower"
    }

    indicators_summary = {
        "current_price": round(current_price, 2),
        "moving_averages": {
            "ma20": round(ma20.iloc[-1], 2),
            "ma50": round(ma50.iloc[-1], 2),
            "ma100": round(ma100.iloc[-1], 2),
            "ma200": round(ma200.iloc[-1], 2),
            "ema12": round(ema12.iloc[-1], 2),
            "ema26": round(ema26.iloc[-1], 2)
        },
        "rsi": {
            "current": round(current_rsi, 2),
            "signal": trend_signals["rsi_signal"]
        },
        "macd": {
            "macd_line": round(current_macd, 2),
            "signal_line": round(current_signal, 2),
            "histogram": round(histogram.iloc[-1], 2),
            "signal": trend_signals["macd_signal"]
        },
        "bollinger_bands": {
            "upper": round(current_bb_upper, 2),
            "middle": round(bb_middle.iloc[-1], 2),
            "lower": round(current_bb_lower, 2),
            "bandwidth_pct": round(((current_bb_upper - current_bb_lower) / bb_middle.iloc[-1]) * 100, 2)
        },
        "atr": {
            "current": round(current_atr, 2),
            "atr_pct_of_price": round((current_atr / current_price) * 100, 2)
        },
        "trend_signals": trend_signals
    }

    return indicators_summary, {
        'ma20': ma20, 'ma50': ma50, 'ma100': ma100, 'ma200': ma200,
        'rsi': rsi, 'macd_line': macd_line, 'signal_line': signal_line,
        'histogram': histogram, 'bb_upper': bb_upper, 'bb_middle': bb_middle,
        'bb_lower': bb_lower, 'atr': atr
    }

def plot_technical_indicators(data, indicators, filepath="../charts/technical_indicators.png"):
    """Generate comprehensive technical indicators chart."""
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(4, 1, height_ratios=[2, 1, 1, 1], hspace=0.3)

    dates = data.index

    # 1. Price with Moving Averages and Bollinger Bands
    ax1 = fig.add_subplot(gs[0])
    ax1.plot(dates, data['Close'], label='Close Price', color='#1a73e8', linewidth=2)
    ax1.plot(dates, indicators['ma20'], label='MA20', color='orange', linewidth=1.5, alpha=0.8)
    ax1.plot(dates, indicators['ma50'], label='MA50', color='red', linewidth=1.5, alpha=0.8)
    ax1.plot(dates, indicators['ma200'], label='MA200', color='purple', linewidth=1.5, alpha=0.8)

    # Bollinger Bands
    ax1.plot(dates, indicators['bb_upper'], 'g--', label='BB Upper', alpha=0.5, linewidth=1)
    ax1.plot(dates, indicators['bb_lower'], 'g--', label='BB Lower', alpha=0.5, linewidth=1)
    ax1.fill_between(dates, indicators['bb_upper'], indicators['bb_lower'], alpha=0.1, color='green')

    ax1.set_title('GOOGL - Technical Analysis Dashboard', fontsize=16, fontweight='bold', pad=20)
    ax1.set_ylabel('Price ($)', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper left', ncol=3, framealpha=0.9, fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    # 2. RSI
    ax2 = fig.add_subplot(gs[1], sharex=ax1)
    ax2.plot(dates, indicators['rsi'], label='RSI', color='purple', linewidth=1.5)
    ax2.axhline(y=70, color='r', linestyle='--', alpha=0.5, label='Overbought (70)')
    ax2.axhline(y=30, color='g', linestyle='--', alpha=0.5, label='Oversold (30)')
    ax2.fill_between(dates, 70, 100, alpha=0.1, color='red')
    ax2.fill_between(dates, 0, 30, alpha=0.1, color='green')
    ax2.set_ylabel('RSI', fontsize=12, fontweight='bold')
    ax2.set_ylim(0, 100)
    ax2.legend(loc='upper left', framealpha=0.9, fontsize=9)
    ax2.grid(True, alpha=0.3)

    # 3. MACD
    ax3 = fig.add_subplot(gs[2], sharex=ax1)
    ax3.plot(dates, indicators['macd_line'], label='MACD', color='blue', linewidth=1.5)
    ax3.plot(dates, indicators['signal_line'], label='Signal', color='red', linewidth=1.5)
    colors = ['green' if val >= 0 else 'red' for val in indicators['histogram']]
    ax3.bar(dates, indicators['histogram'], label='Histogram', color=colors, alpha=0.5, width=1)
    ax3.axhline(y=0, color='black', linestyle='-', alpha=0.3, linewidth=0.8)
    ax3.set_ylabel('MACD', fontsize=12, fontweight='bold')
    ax3.legend(loc='upper left', framealpha=0.9, fontsize=9)
    ax3.grid(True, alpha=0.3)

    # 4. Volume with ATR
    ax4 = fig.add_subplot(gs[3], sharex=ax1)
    colors = ['green' if data['Close'].iloc[i] >= data['Open'].iloc[i] else 'red'
              for i in range(len(data))]
    ax4.bar(dates, data['Volume'], color=colors, alpha=0.6, width=1)
    ax4.set_ylabel('Volume', fontsize=12, fontweight='bold')
    ax4.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax4.grid(True, alpha=0.3, axis='y')
    ax4.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    # Add ATR on secondary axis
    ax4_twin = ax4.twinx()
    ax4_twin.plot(dates, indicators['atr'], color='orange', linewidth=2, alpha=0.7, label='ATR')
    ax4_twin.set_ylabel('ATR ($)', fontsize=12, fontweight='bold', color='orange')
    ax4_twin.tick_params(axis='y', labelcolor='orange')
    ax4_twin.legend(loc='upper left', framealpha=0.9, fontsize=9)

    plt.tight_layout()
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f"Technical indicators chart saved to {filepath}")
    plt.close()

if __name__ == "__main__":
    print("Calculating technical indicators for GOOGL...")

    # Fetch data
    ticker = yf.Ticker("GOOGL")
    data = ticker.history(period="2y")

    # Calculate indicators
    summary, indicators = analyze_indicators(data)

    # Print summary
    print("\n=== TECHNICAL INDICATORS SUMMARY ===")
    print(f"Current Price: ${summary['current_price']}")
    print("\nMoving Averages:")
    for ma, value in summary['moving_averages'].items():
        trend = "↑" if summary['current_price'] > value else "↓"
        print(f"  {ma.upper()}: ${value} {trend}")

    print(f"\nRSI: {summary['rsi']['current']} ({summary['rsi']['signal']})")
    print(f"MACD: {summary['macd']['macd_line']} (Signal: {summary['macd']['signal_line']}) - {summary['macd']['signal']}")
    print(f"\nBollinger Bands: ${summary['bollinger_bands']['lower']} - ${summary['bollinger_bands']['upper']}")
    print(f"BB Bandwidth: {summary['bollinger_bands']['bandwidth_pct']}%")
    print(f"\nATR: ${summary['atr']['current']} ({summary['atr']['atr_pct_of_price']}% of price)")

    print("\n=== TREND SIGNALS ===")
    for signal, value in summary['trend_signals'].items():
        print(f"  {signal}: {value}")

    # Save to JSON
    with open("../data/technical_indicators.json", 'w') as f:
        json.dump(summary, f, indent=2)
    print("\nIndicators saved to ../data/technical_indicators.json")

    # Generate chart
    plot_technical_indicators(data, indicators)

    print("\n✓ Technical indicators analysis complete!")
