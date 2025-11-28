#!/usr/bin/env python3
"""
Identify support and resistance levels for Google stock using multiple methods:
1. Pivot Points (Standard, Fibonacci, Camarilla)
2. Historical price levels (swing highs/lows)
3. Volume Profile (price levels with high trading volume)
4. Fibonacci Retracement
5. Psychological levels (round numbers)
"""

import yfinance as yf
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from scipy.signal import argrelextrema

def calculate_pivot_points(data):
    """Calculate various pivot point levels."""
    # Use recent high, low, close for pivot calculation
    high = data['High'].iloc[-1]
    low = data['Low'].iloc[-1]
    close = data['Close'].iloc[-1]

    # Standard Pivot Points
    pivot = (high + low + close) / 3
    r1 = 2 * pivot - low
    r2 = pivot + (high - low)
    r3 = high + 2 * (pivot - low)
    s1 = 2 * pivot - high
    s2 = pivot - (high - low)
    s3 = low - 2 * (high - pivot)

    # Fibonacci Pivot Points
    fib_r1 = pivot + 0.382 * (high - low)
    fib_r2 = pivot + 0.618 * (high - low)
    fib_r3 = pivot + 1.000 * (high - low)
    fib_s1 = pivot - 0.382 * (high - low)
    fib_s2 = pivot - 0.618 * (high - low)
    fib_s3 = pivot - 1.000 * (high - low)

    # Camarilla Pivot Points
    cam_r1 = close + (high - low) * 1.1 / 12
    cam_r2 = close + (high - low) * 1.1 / 6
    cam_r3 = close + (high - low) * 1.1 / 4
    cam_r4 = close + (high - low) * 1.1 / 2
    cam_s1 = close - (high - low) * 1.1 / 12
    cam_s2 = close - (high - low) * 1.1 / 6
    cam_s3 = close - (high - low) * 1.1 / 4
    cam_s4 = close - (high - low) * 1.1 / 2

    return {
        "standard": {
            "pivot": round(pivot, 2),
            "r1": round(r1, 2), "r2": round(r2, 2), "r3": round(r3, 2),
            "s1": round(s1, 2), "s2": round(s2, 2), "s3": round(s3, 2)
        },
        "fibonacci": {
            "pivot": round(pivot, 2),
            "r1": round(fib_r1, 2), "r2": round(fib_r2, 2), "r3": round(fib_r3, 2),
            "s1": round(fib_s1, 2), "s2": round(fib_s2, 2), "s3": round(fib_s3, 2)
        },
        "camarilla": {
            "r1": round(cam_r1, 2), "r2": round(cam_r2, 2),
            "r3": round(cam_r3, 2), "r4": round(cam_r4, 2),
            "s1": round(cam_s1, 2), "s2": round(cam_s2, 2),
            "s3": round(cam_s3, 2), "s4": round(cam_s4, 2)
        }
    }

def find_swing_points(data, order=5):
    """Find swing highs and lows using local extrema."""
    # Find local maxima and minima
    high_indices = argrelextrema(data['High'].values, np.greater, order=order)[0]
    low_indices = argrelextrema(data['Low'].values, np.less, order=order)[0]

    swing_highs = []
    swing_lows = []

    # Get recent swing highs (last 6 months)
    recent_days = 126
    for idx in high_indices:
        if idx >= len(data) - recent_days:
            swing_highs.append({
                "date": data.index[idx].strftime("%Y-%m-%d"),
                "price": round(data['High'].iloc[idx], 2),
                "index": int(idx)
            })

    # Get recent swing lows (last 6 months)
    for idx in low_indices:
        if idx >= len(data) - recent_days:
            swing_lows.append({
                "date": data.index[idx].strftime("%Y-%m-%d"),
                "price": round(data['Low'].iloc[idx], 2),
                "index": int(idx)
            })

    return swing_highs, swing_lows

def calculate_fibonacci_retracement(data, lookback=252):
    """Calculate Fibonacci retracement levels from recent high/low."""
    recent_data = data.iloc[-lookback:]
    swing_high = recent_data['High'].max()
    swing_low = recent_data['Low'].min()
    diff = swing_high - swing_low

    fib_levels = {
        "swing_high": round(swing_high, 2),
        "fib_0.236": round(swing_high - 0.236 * diff, 2),
        "fib_0.382": round(swing_high - 0.382 * diff, 2),
        "fib_0.500": round(swing_high - 0.500 * diff, 2),
        "fib_0.618": round(swing_high - 0.618 * diff, 2),
        "fib_0.786": round(swing_high - 0.786 * diff, 2),
        "swing_low": round(swing_low, 2)
    }

    return fib_levels

def find_volume_clusters(data, num_bins=50):
    """Find price levels with high volume concentration."""
    # Create price bins and sum volume
    price_min = data['Low'].min()
    price_max = data['High'].max()
    bins = np.linspace(price_min, price_max, num_bins)

    volume_profile = []
    for i in range(len(bins) - 1):
        mask = (data['Close'] >= bins[i]) & (data['Close'] < bins[i + 1])
        total_volume = data.loc[mask, 'Volume'].sum()
        volume_profile.append({
            "price_level": round((bins[i] + bins[i + 1]) / 2, 2),
            "volume": int(total_volume)
        })

    # Sort by volume and get top levels
    volume_profile.sort(key=lambda x: x['volume'], reverse=True)
    return volume_profile[:10]  # Top 10 volume clusters

def find_psychological_levels(current_price, range_pct=20):
    """Find psychological round number levels near current price."""
    # Round to nearest $10, $5, etc.
    levels = []

    # $10 increments
    base_10 = int(current_price / 10) * 10
    for i in range(-3, 4):
        level = base_10 + (i * 10)
        if level > 0:
            levels.append(level)

    # $5 increments between $10 levels
    base_5 = int(current_price / 5) * 5
    for i in range(-6, 7):
        level = base_5 + (i * 5)
        if level > 0 and level not in levels:
            levels.append(level)

    # Filter to within range
    min_price = current_price * (1 - range_pct / 100)
    max_price = current_price * (1 + range_pct / 100)
    levels = [l for l in levels if min_price <= l <= max_price]
    levels.sort()

    return levels

def identify_key_support_resistance(data):
    """Comprehensive support and resistance identification."""
    current_price = data['Close'].iloc[-1]

    # 1. Pivot Points
    pivots = calculate_pivot_points(data)

    # 2. Swing Points
    swing_highs, swing_lows = find_swing_points(data)

    # 3. Fibonacci Retracement
    fib_levels = calculate_fibonacci_retracement(data)

    # 4. Volume Clusters
    volume_clusters = find_volume_clusters(data)

    # 5. Psychological Levels
    psych_levels = find_psychological_levels(current_price)

    # Aggregate all resistance and support levels
    resistance_levels = []
    support_levels = []

    # From pivots
    for method in ['standard', 'fibonacci']:
        if pivots[method]['r1'] > current_price:
            resistance_levels.append(pivots[method]['r1'])
        if pivots[method]['s1'] < current_price:
            support_levels.append(pivots[method]['s1'])

    # From swing points
    for swing in swing_highs:
        if swing['price'] > current_price:
            resistance_levels.append(swing['price'])
    for swing in swing_lows:
        if swing['price'] < current_price:
            support_levels.append(swing['price'])

    # From fibonacci
    for key, level in fib_levels.items():
        if 'fib' in key:
            if level > current_price:
                resistance_levels.append(level)
            elif level < current_price:
                support_levels.append(level)

    # From volume clusters
    for cluster in volume_clusters:
        if cluster['price_level'] > current_price:
            resistance_levels.append(cluster['price_level'])
        elif cluster['price_level'] < current_price:
            support_levels.append(cluster['price_level'])

    # Cluster similar levels (within 1% of each other)
    def cluster_levels(levels):
        if not levels:
            return []
        levels = sorted(levels)
        clustered = []
        current_cluster = [levels[0]]

        for level in levels[1:]:
            if abs(level - current_cluster[-1]) / current_cluster[-1] < 0.01:
                current_cluster.append(level)
            else:
                clustered.append(round(np.mean(current_cluster), 2))
                current_cluster = [level]
        clustered.append(round(np.mean(current_cluster), 2))
        return clustered

    resistance_levels = cluster_levels(resistance_levels)
    support_levels = cluster_levels(support_levels)

    # Get nearest levels
    nearest_resistance = [r for r in resistance_levels if r > current_price][:3]
    nearest_support = [s for s in support_levels if s < current_price][-3:]

    return {
        "current_price": round(current_price, 2),
        "nearest_resistance": nearest_resistance,
        "nearest_support": nearest_support,
        "all_resistance": resistance_levels,
        "all_support": support_levels,
        "pivot_points": pivots,
        "fibonacci_retracement": fib_levels,
        "swing_highs": swing_highs[:5],  # Top 5 most recent
        "swing_lows": swing_lows[:5],
        "volume_clusters": volume_clusters,
        "psychological_levels": psych_levels
    }

def plot_support_resistance(data, levels, filepath="../charts/support_resistance_levels.png"):
    """Visualize support and resistance levels on price chart."""
    fig, ax = plt.subplots(figsize=(16, 10))

    dates = data.index[-126:]  # Last 6 months
    prices = data['Close'].iloc[-126:]

    # Plot price
    ax.plot(dates, prices, label='Close Price', color='#1a73e8', linewidth=2, zorder=3)

    # Plot resistance levels
    for level in levels['nearest_resistance']:
        ax.axhline(y=level, color='red', linestyle='--', linewidth=1.5, alpha=0.7, zorder=2)
        ax.text(dates[-1], level, f' R: ${level}', verticalalignment='center',
                color='red', fontweight='bold', fontsize=10)

    # Plot support levels
    for level in levels['nearest_support']:
        ax.axhline(y=level, color='green', linestyle='--', linewidth=1.5, alpha=0.7, zorder=2)
        ax.text(dates[-1], level, f' S: ${level}', verticalalignment='center',
                color='green', fontweight='bold', fontsize=10)

    # Mark swing highs and lows
    for swing in levels['swing_highs']:
        if swing['index'] >= len(data) - 126:
            idx = swing['index'] - (len(data) - 126)
            if 0 <= idx < len(dates):
                ax.plot(dates[idx], swing['price'], 'rv', markersize=8, zorder=4)

    for swing in levels['swing_lows']:
        if swing['index'] >= len(data) - 126:
            idx = swing['index'] - (len(data) - 126)
            if 0 <= idx < len(dates):
                ax.plot(dates[idx], swing['price'], 'g^', markersize=8, zorder=4)

    # Current price line
    ax.axhline(y=levels['current_price'], color='blue', linestyle='-',
               linewidth=2, alpha=0.5, label=f"Current: ${levels['current_price']}")

    ax.set_title('GOOGL - Support & Resistance Levels (6 Month View)',
                 fontsize=16, fontweight='bold', pad=20)
    ax.set_ylabel('Price ($)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax.legend(loc='upper left', framealpha=0.9)
    ax.grid(True, alpha=0.3)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    # Add shaded zones for support/resistance
    if levels['nearest_resistance']:
        ax.axhspan(levels['current_price'], levels['nearest_resistance'][0],
                   alpha=0.1, color='red', label='Resistance Zone')
    if levels['nearest_support']:
        ax.axhspan(levels['nearest_support'][-1], levels['current_price'],
                   alpha=0.1, color='green', label='Support Zone')

    plt.tight_layout()
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f"Support/Resistance chart saved to {filepath}")
    plt.close()

if __name__ == "__main__":
    print("Identifying support and resistance levels for GOOGL...")

    # Fetch data
    ticker = yf.Ticker("GOOGL")
    data = ticker.history(period="2y")

    # Identify levels
    levels = identify_key_support_resistance(data)

    # Print analysis
    print(f"\n=== SUPPORT & RESISTANCE ANALYSIS ===")
    print(f"Current Price: ${levels['current_price']}")

    print(f"\nNearest Resistance Levels:")
    for i, r in enumerate(levels['nearest_resistance'], 1):
        distance = ((r / levels['current_price']) - 1) * 100
        print(f"  R{i}: ${r} (+{distance:.2f}%)")

    print(f"\nNearest Support Levels:")
    for i, s in enumerate(reversed(levels['nearest_support']), 1):
        distance = ((s / levels['current_price']) - 1) * 100
        print(f"  S{i}: ${s} ({distance:.2f}%)")

    print(f"\n=== PIVOT POINTS ===")
    print("Standard Pivot Points:")
    for key, value in levels['pivot_points']['standard'].items():
        print(f"  {key}: ${value}")

    print("\n=== FIBONACCI RETRACEMENT ===")
    for key, value in levels['fibonacci_retracement'].items():
        print(f"  {key}: ${value}")

    print(f"\n=== TOP VOLUME CLUSTERS ===")
    for i, cluster in enumerate(levels['volume_clusters'][:5], 1):
        print(f"  {i}. ${cluster['price_level']} (Volume: {cluster['volume']:,})")

    # Save to JSON
    # Convert numpy types to native Python types for JSON serialization
    def convert_to_native(obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, dict):
            return {key: convert_to_native(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [convert_to_native(item) for item in obj]
        return obj

    levels_json = convert_to_native(levels)

    with open("../data/support_resistance_levels.json", 'w') as f:
        json.dump(levels_json, f, indent=2)
    print("\nLevels saved to ../data/support_resistance_levels.json")

    # Generate chart
    plot_support_resistance(data, levels)

    print("\n✓ Support/Resistance analysis complete!")
