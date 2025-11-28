#!/usr/bin/env python3
"""
Options analysis for selling puts on Google (GOOGL).
Analyzes:
- Implied Volatility (IV)
- Options chain data
- Recommended put strike prices based on support levels
- Expected premiums and return on risk
- Probability of profit
"""

import yfinance as yf
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from scipy.stats import norm

def fetch_options_data(ticker_symbol="GOOGL"):
    """Fetch current options chain data."""
    ticker = yf.Ticker(ticker_symbol)

    # Get available expiration dates
    expirations = ticker.options

    if not expirations:
        print("No options data available")
        return None

    # Get options data for multiple expirations (next 3 months)
    options_data = {}

    for exp_date in expirations[:6]:  # First 6 expiration dates
        try:
            opt = ticker.option_chain(exp_date)
            options_data[exp_date] = {
                'calls': opt.calls,
                'puts': opt.puts
            }
        except Exception as e:
            print(f"Error fetching options for {exp_date}: {e}")

    return options_data, ticker

def calculate_implied_volatility_stats(options_data):
    """Calculate IV statistics from options chain."""
    iv_data = []

    for exp_date, data in options_data.items():
        puts = data['puts']

        # Get ATM and near-the-money options
        if not puts.empty and 'impliedVolatility' in puts.columns:
            # Filter for liquid options (volume > 0 or openInterest > 10)
            liquid_puts = puts[
                ((puts['volume'] > 0) | (puts['openInterest'] > 10)) &
                (puts['impliedVolatility'].notna())
            ]

            if not liquid_puts.empty:
                avg_iv = liquid_puts['impliedVolatility'].mean()
                iv_data.append({
                    'expiration': exp_date,
                    'avg_iv': avg_iv,
                    'min_iv': liquid_puts['impliedVolatility'].min(),
                    'max_iv': liquid_puts['impliedVolatility'].max()
                })

    return iv_data

def recommend_put_strikes(current_price, support_levels, options_data, risk_tolerance='moderate'):
    """
    Recommend put strike prices for selling based on support levels.

    risk_tolerance:
    - 'conservative': Strikes well below support (lower premium, lower risk)
    - 'moderate': Strikes at or slightly below support
    - 'aggressive': Strikes at or above support (higher premium, higher risk)
    """
    recommendations = []

    # Define distance from support based on risk tolerance
    risk_params = {
        'conservative': {'support_buffer': 0.95, 'description': 'Strike 5% below support'},
        'moderate': {'support_buffer': 0.98, 'description': 'Strike at or 2% below support'},
        'aggressive': {'support_buffer': 1.00, 'description': 'Strike at support level'}
    }

    buffer = risk_params[risk_tolerance]['support_buffer']

    # For each major support level
    for support in support_levels[:3]:  # Top 3 support levels
        strike_price = round(support * buffer / 5) * 5  # Round to nearest $5

        # Find matching options across expirations
        for exp_date, data in options_data.items():
            puts = data['puts']

            # Find puts at this strike
            matching_puts = puts[puts['strike'] == strike_price]

            if not matching_puts.empty:
                put = matching_puts.iloc[0]

                # Calculate days to expiration
                exp_datetime = datetime.strptime(exp_date, '%Y-%m-%d')
                days_to_exp = (exp_datetime - datetime.now()).days

                # Skip if too close to expiration or too far out
                if days_to_exp < 7 or days_to_exp > 90:
                    continue

                # Get option metrics
                bid = put.get('bid', 0)
                ask = put.get('ask', 0)
                mid_price = (bid + ask) / 2 if bid > 0 and ask > 0 else 0
                iv = put.get('impliedVolatility', 0)
                delta = abs(put.get('delta', 0))  # Probability of being ITM
                volume = put.get('volume', 0)
                open_interest = put.get('openInterest', 0)

                if mid_price > 0:
                    # Calculate metrics
                    premium_pct = (mid_price / current_price) * 100
                    annualized_return = (premium_pct * 365 / days_to_exp)
                    distance_from_current = ((strike_price / current_price) - 1) * 100
                    distance_from_support = ((strike_price / support) - 1) * 100

                    recommendations.append({
                        'strike': strike_price,
                        'expiration': exp_date,
                        'days_to_expiration': days_to_exp,
                        'support_level': round(support, 2),
                        'current_price': round(current_price, 2),
                        'bid': round(bid, 2),
                        'ask': round(ask, 2),
                        'mid_price': round(mid_price, 2),
                        'implied_volatility': round(iv * 100, 2) if iv else 0,
                        'delta': round(delta, 3),
                        'probability_itm_pct': round(delta * 100, 2),
                        'probability_profit_pct': round((1 - delta) * 100, 2),
                        'premium_pct': round(premium_pct, 2),
                        'annualized_return_pct': round(annualized_return, 2),
                        'distance_from_current_pct': round(distance_from_current, 2),
                        'distance_from_support_pct': round(distance_from_support, 2),
                        'volume': int(volume) if pd.notna(volume) else 0,
                        'open_interest': int(open_interest) if pd.notna(open_interest) else 0,
                        'risk_level': risk_tolerance
                    })

    # Sort by annualized return (descending)
    recommendations.sort(key=lambda x: x['annualized_return_pct'], reverse=True)

    return recommendations

def analyze_put_selling_strategy(current_price, historical_data, support_levels, options_data):
    """Comprehensive put selling strategy analysis."""

    # Calculate historical volatility
    returns = historical_data['Close'].pct_change()
    hist_vol_30d = returns.iloc[-30:].std() * np.sqrt(252) * 100  # Annualized
    hist_vol_60d = returns.iloc[-60:].std() * np.sqrt(252) * 100
    hist_vol_252d = returns.iloc[-252:].std() * np.sqrt(252) * 100

    # Get IV stats
    iv_stats = calculate_implied_volatility_stats(options_data)

    # Get recommendations for different risk levels
    conservative_recs = recommend_put_strikes(current_price, support_levels,
                                               options_data, 'conservative')
    moderate_recs = recommend_put_strikes(current_price, support_levels,
                                           options_data, 'moderate')
    aggressive_recs = recommend_put_strikes(current_price, support_levels,
                                             options_data, 'aggressive')

    all_recommendations = conservative_recs + moderate_recs + aggressive_recs

    # Filter for best opportunities (high return, decent liquidity)
    quality_recs = [r for r in all_recommendations
                    if r['open_interest'] > 10 and r['mid_price'] > 0.5]

    # Get top recommendations
    top_conservative = conservative_recs[:3] if conservative_recs else []
    top_moderate = moderate_recs[:3] if moderate_recs else []
    top_aggressive = aggressive_recs[:3] if aggressive_recs else []

    strategy_analysis = {
        "current_price": round(current_price, 2),
        "market_conditions": {
            "historical_volatility_30d": round(hist_vol_30d, 2),
            "historical_volatility_60d": round(hist_vol_60d, 2),
            "historical_volatility_252d": round(hist_vol_252d, 2),
            "implied_volatility_stats": iv_stats
        },
        "support_levels_used": [round(s, 2) for s in support_levels[:3]],
        "recommendations": {
            "conservative": top_conservative,
            "moderate": top_moderate,
            "aggressive": top_aggressive
        },
        "all_quality_recommendations": quality_recs[:20],  # Top 20 overall
        "strategy_notes": {
            "conservative": "Lower premium, lower risk. Strike 5% below support.",
            "moderate": "Balanced risk/reward. Strike at or 2% below support.",
            "aggressive": "Higher premium, higher risk. Strike at support level."
        }
    }

    return strategy_analysis

def plot_put_selling_strategy(historical_data, support_levels, recommendations,
                                filepath="../charts/put_selling_strategy.png"):
    """Visualize put selling strategy with strike prices and support levels."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 12),
                                     gridspec_kw={'height_ratios': [2, 1]})

    # Last 6 months of data
    dates = historical_data.index[-126:]
    prices = historical_data['Close'].iloc[-126:]
    current_price = prices.iloc[-1]

    # Plot price
    ax1.plot(dates, prices, label='Close Price', color='#1a73e8', linewidth=2, zorder=3)

    # Plot support levels
    colors_support = ['green', 'darkgreen', 'lime']
    for i, support in enumerate(support_levels[:3]):
        color = colors_support[i] if i < len(colors_support) else 'green'
        ax1.axhline(y=support, color=color, linestyle='--', linewidth=2,
                    alpha=0.7, label=f'Support ${support:.0f}', zorder=2)

    # Plot recommended strike prices
    strike_colors = {'conservative': 'blue', 'moderate': 'orange', 'aggressive': 'red'}

    plotted_strikes = set()
    for rec in recommendations[:9]:  # Top 9 recommendations
        strike = rec['strike']
        if strike not in plotted_strikes:
            color = strike_colors.get(rec['risk_level'], 'gray')
            ax1.axhline(y=strike, color=color, linestyle=':', linewidth=1.5,
                        alpha=0.6, zorder=1)
            plotted_strikes.add(strike)

    # Current price
    ax1.axhline(y=current_price, color='black', linestyle='-',
                linewidth=2, label=f'Current ${current_price:.0f}')

    ax1.set_title('GOOGL - Put Selling Strategy: Support Levels & Recommended Strikes',
                  fontsize=16, fontweight='bold', pad=20)
    ax1.set_ylabel('Price ($)', fontsize=12, fontweight='bold')
    ax1.legend(loc='upper left', framealpha=0.9, fontsize=9)
    ax1.grid(True, alpha=0.3)

    # Bottom panel: Strike recommendations table visualization
    ax2.axis('off')

    # Create table data
    table_data = []
    headers = ['Strike', 'Exp', 'DTE', 'Premium', 'Ann. Ret.%', 'Prob. Profit%',
               'Dist. Support%', 'Risk']

    for rec in recommendations[:8]:  # Top 8
        row = [
            f"${rec['strike']}",
            rec['expiration'][5:],  # MM-DD
            f"{rec['days_to_expiration']}d",
            f"${rec['mid_price']:.2f}",
            f"{rec['annualized_return_pct']:.1f}%",
            f"{rec['probability_profit_pct']:.0f}%",
            f"{rec['distance_from_support_pct']:.1f}%",
            rec['risk_level'][0].upper()  # C/M/A
        ]
        table_data.append(row)

    # Create table
    table = ax2.table(cellText=table_data, colLabels=headers,
                      cellLoc='center', loc='center',
                      bbox=[0, 0, 1, 1])

    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2)

    # Color code by risk level
    for i, rec in enumerate(recommendations[:8], 1):
        risk_color = {'conservative': '#90EE90', 'moderate': '#FFD580', 'aggressive': '#FFB6C6'}
        color = risk_color.get(rec['risk_level'], 'white')
        for j in range(len(headers)):
            table[(i, j)].set_facecolor(color)

    # Header formatting
    for j in range(len(headers)):
        table[(0, j)].set_facecolor('#1a73e8')
        table[(0, j)].set_text_props(weight='bold', color='white')

    ax2.set_title('Top Put Selling Opportunities (Ranked by Annualized Return)',
                  fontsize=12, fontweight='bold', pad=10)

    plt.tight_layout()
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f"Put selling strategy chart saved to {filepath}")
    plt.close()

def plot_risk_return_scatter(recommendations, filepath="../charts/put_risk_return.png"):
    """Scatter plot of risk vs return for put recommendations."""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Separate by risk level
    conservative = [r for r in recommendations if r['risk_level'] == 'conservative']
    moderate = [r for r in recommendations if r['risk_level'] == 'moderate']
    aggressive = [r for r in recommendations if r['risk_level'] == 'aggressive']

    # Plot scatter points
    for recs, color, label in [(conservative, 'blue', 'Conservative'),
                                (moderate, 'orange', 'Moderate'),
                                (aggressive, 'red', 'Aggressive')]:
        if recs:
            x = [r['probability_profit_pct'] for r in recs]
            y = [r['annualized_return_pct'] for r in recs]
            sizes = [r['days_to_expiration'] * 2 for r in recs]
            ax.scatter(x, y, s=sizes, alpha=0.6, c=color, label=label, edgecolors='black')

    ax.set_xlabel('Probability of Profit (%)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Annualized Return (%)', fontsize=12, fontweight='bold')
    ax.set_title('GOOGL Put Selling: Risk vs Return Analysis\n(Size = Days to Expiration)',
                 fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper left', framealpha=0.9)
    ax.grid(True, alpha=0.3)

    # Add quadrant lines
    ax.axvline(x=70, color='gray', linestyle='--', alpha=0.5)
    ax.axhline(y=15, color='gray', linestyle='--', alpha=0.5)

    # Annotate best opportunities
    top_recs = sorted(recommendations, key=lambda x: x['annualized_return_pct'], reverse=True)[:3]
    for rec in top_recs:
        ax.annotate(f"${rec['strike']}\n{rec['expiration'][5:]}",
                    xy=(rec['probability_profit_pct'], rec['annualized_return_pct']),
                    xytext=(10, 10), textcoords='offset points',
                    fontsize=8, alpha=0.7,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.3))

    plt.tight_layout()
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f"Risk/return scatter plot saved to {filepath}")
    plt.close()

if __name__ == "__main__":
    print("Analyzing put selling opportunities for GOOGL...")

    # Fetch historical data
    ticker = yf.Ticker("GOOGL")
    historical_data = ticker.history(period="2y")
    current_price = historical_data['Close'].iloc[-1]

    # Load support levels from previous analysis
    try:
        with open("../data/support_resistance_levels.json", 'r') as f:
            sr_data = json.load(f)
            support_levels = sr_data['nearest_support']
    except FileNotFoundError:
        print("Warning: Support/resistance data not found. Using default levels.")
        support_levels = [current_price * 0.95, current_price * 0.90, current_price * 0.85]

    # Fetch options data
    print("\nFetching options chain data...")
    result = fetch_options_data("GOOGL")
    if result:
        options_data, ticker_obj = result

        # Analyze strategy
        analysis = analyze_put_selling_strategy(current_price, historical_data,
                                                 support_levels, options_data)

        # Print results
        print(f"\n=== PUT SELLING STRATEGY ANALYSIS ===")
        print(f"Current Price: ${analysis['current_price']}")
        print(f"\nHistorical Volatility:")
        print(f"  30-day: {analysis['market_conditions']['historical_volatility_30d']:.2f}%")
        print(f"  60-day: {analysis['market_conditions']['historical_volatility_60d']:.2f}%")
        print(f"  1-year: {analysis['market_conditions']['historical_volatility_252d']:.2f}%")

        print(f"\nSupport Levels Used: {analysis['support_levels_used']}")

        print("\n=== TOP RECOMMENDATIONS ===")

        for risk_level in ['conservative', 'moderate', 'aggressive']:
            recs = analysis['recommendations'][risk_level]
            if recs:
                print(f"\n{risk_level.upper()}:")
                print(f"  {analysis['strategy_notes'][risk_level]}")
                for i, rec in enumerate(recs[:3], 1):
                    print(f"\n  {i}. Strike ${rec['strike']} exp {rec['expiration']}")
                    print(f"     Premium: ${rec['mid_price']} ({rec['premium_pct']:.2f}% of stock price)")
                    print(f"     Annualized Return: {rec['annualized_return_pct']:.1f}%")
                    print(f"     Probability of Profit: {rec['probability_profit_pct']:.0f}%")
                    print(f"     Days to Expiration: {rec['days_to_expiration']}")
                    print(f"     Distance from Support: {rec['distance_from_support_pct']:.1f}%")
                    print(f"     Open Interest: {rec['open_interest']}")

        # Save to JSON
        with open("../data/put_selling_analysis.json", 'w') as f:
            json.dump(analysis, f, indent=2, default=str)
        print("\n\nAnalysis saved to ../data/put_selling_analysis.json")

        # Generate visualizations
        if analysis['all_quality_recommendations']:
            plot_put_selling_strategy(historical_data, support_levels,
                                       analysis['all_quality_recommendations'])
            plot_risk_return_scatter(analysis['all_quality_recommendations'])

        print("\n✓ Options analysis complete!")
    else:
        print("Unable to fetch options data")
