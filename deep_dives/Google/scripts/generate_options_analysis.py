#!/usr/bin/env python3
"""
Generate options market analysis for Alphabet (GOOGL)
Analyzes implied volatility, put/call ratios, and sentiment indicators
"""

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime, timedelta

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (16, 10)
plt.rcParams['font.size'] = 10

def fetch_options_data(ticker="GOOGL"):
    """Fetch options chain data"""
    stock = yf.Ticker(ticker)

    # Get available expiration dates
    expirations = stock.options

    if len(expirations) == 0:
        print("No options data available")
        return None, None, None

    # Get current stock price
    current_price = stock.history(period="1d")['Close'].iloc[-1]

    # Analyze multiple expirations
    options_data = []

    for exp_date in expirations[:8]:  # Analyze first 8 expirations
        try:
            # Get options chain
            opt = stock.option_chain(exp_date)
            calls = opt.calls
            puts = opt.puts

            # Calculate key metrics
            total_call_volume = calls['volume'].sum()
            total_put_volume = puts['volume'].sum()
            total_call_oi = calls['openInterest'].sum()
            total_put_oi = puts['openInterest'].sum()

            # Put/Call ratios
            pc_volume = total_put_volume / total_call_volume if total_call_volume > 0 else 0
            pc_oi = total_put_oi / total_call_oi if total_call_oi > 0 else 0

            # ATM options IV
            atm_strikes = (calls['strike'] - current_price).abs()
            atm_idx = atm_strikes.idxmin()
            atm_call_iv = calls.loc[atm_idx, 'impliedVolatility']

            atm_strikes_put = (puts['strike'] - current_price).abs()
            atm_idx_put = atm_strikes_put.idxmin()
            atm_put_iv = puts.loc[atm_idx_put, 'impliedVolatility']

            # Days to expiration
            exp_dt = datetime.strptime(exp_date, '%Y-%m-%d')
            dte = (exp_dt - datetime.now()).days

            options_data.append({
                'expiration': exp_date,
                'dte': dte,
                'call_volume': total_call_volume,
                'put_volume': total_put_volume,
                'call_oi': total_call_oi,
                'put_oi': total_put_oi,
                'pc_volume': pc_volume,
                'pc_oi': pc_oi,
                'atm_call_iv': atm_call_iv,
                'atm_put_iv': atm_put_iv,
                'iv_skew': atm_put_iv - atm_call_iv
            })
        except Exception as e:
            print(f"Error processing {exp_date}: {e}")
            continue

    return pd.DataFrame(options_data), stock, current_price

def calculate_iv_percentile(stock, current_iv):
    """Calculate IV percentile vs historical volatility"""
    # Get 1 year of historical data
    hist = stock.history(period="1y")

    # Calculate daily returns
    returns = hist['Close'].pct_change().dropna()

    # Calculate realized volatility (annualized)
    realized_vol = returns.std() * np.sqrt(252)

    # Calculate 30-day rolling realized vol
    rolling_vol = returns.rolling(30).std() * np.sqrt(252)

    # IV percentile (simplified - using realized vol as proxy)
    if len(rolling_vol) > 0:
        percentile = (rolling_vol < current_iv).sum() / len(rolling_vol) * 100
    else:
        percentile = 50

    return realized_vol, percentile

def plot_options_dashboard(options_df, stock, current_price, output_dir='charts'):
    """Create comprehensive options analysis dashboard"""

    if options_df is None or len(options_df) == 0:
        print("No options data to plot")
        return

    # Create figure with subplots
    fig = plt.figure(figsize=(18, 12))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

    # 1. Implied Volatility Term Structure
    ax1 = fig.add_subplot(gs[0, :2])
    ax1.plot(options_df['dte'], options_df['atm_call_iv'] * 100,
             marker='o', linewidth=2, markersize=8, label='Call IV', color='#34a853')
    ax1.plot(options_df['dte'], options_df['atm_put_iv'] * 100,
             marker='s', linewidth=2, markersize=8, label='Put IV', color='#ea4335')
    ax1.set_xlabel('Days to Expiration', fontsize=12)
    ax1.set_ylabel('Implied Volatility (%)', fontsize=12)
    ax1.set_title('IV Term Structure', fontsize=14, fontweight='bold')
    ax1.legend(loc='best')
    ax1.grid(True, alpha=0.3)

    # 2. IV Skew
    ax2 = fig.add_subplot(gs[0, 2])
    colors = ['#34a853' if x < 0 else '#ea4335' for x in options_df['iv_skew']]
    ax2.barh(options_df['dte'], options_df['iv_skew'] * 100, color=colors, alpha=0.7)
    ax2.axvline(0, color='black', linestyle='--', linewidth=1)
    ax2.set_xlabel('IV Skew (%)', fontsize=12)
    ax2.set_ylabel('DTE', fontsize=12)
    ax2.set_title('Put-Call IV Skew', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='x')

    # 3. Put/Call Ratio (Volume)
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.bar(range(len(options_df)), options_df['pc_volume'], color='#1a73e8', alpha=0.7)
    ax3.axhline(1.0, color='#ea4335', linestyle='--', linewidth=2, label='Neutral (1.0)')
    ax3.axhline(0.7, color='#34a853', linestyle=':', linewidth=1.5, label='Bullish (<0.7)')
    ax3.set_xlabel('Expiration (by DTE)', fontsize=12)
    ax3.set_ylabel('Put/Call Volume Ratio', fontsize=12)
    ax3.set_title('P/C Ratio (Volume)', fontsize=14, fontweight='bold')
    ax3.set_xticks(range(len(options_df)))
    ax3.set_xticklabels([f"{int(dte)}d" for dte in options_df['dte']], rotation=45)
    ax3.legend()
    ax3.grid(True, alpha=0.3, axis='y')

    # 4. Put/Call Ratio (Open Interest)
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.bar(range(len(options_df)), options_df['pc_oi'], color='#fbbc04', alpha=0.7)
    ax4.axhline(1.0, color='#ea4335', linestyle='--', linewidth=2, label='Neutral (1.0)')
    ax4.axhline(0.7, color='#34a853', linestyle=':', linewidth=1.5, label='Bullish (<0.7)')
    ax4.set_xlabel('Expiration (by DTE)', fontsize=12)
    ax4.set_ylabel('Put/Call OI Ratio', fontsize=12)
    ax4.set_title('P/C Ratio (Open Interest)', fontsize=14, fontweight='bold')
    ax4.set_xticks(range(len(options_df)))
    ax4.set_xticklabels([f"{int(dte)}d" for dte in options_df['dte']], rotation=45)
    ax4.legend()
    ax4.grid(True, alpha=0.3, axis='y')

    # 5. Options Volume Distribution
    ax5 = fig.add_subplot(gs[1, 2])
    call_volume_sum = options_df['call_volume'].sum()
    put_volume_sum = options_df['put_volume'].sum()
    ax5.pie([call_volume_sum, put_volume_sum],
            labels=['Calls', 'Puts'],
            colors=['#34a853', '#ea4335'],
            autopct='%1.1f%%',
            startangle=90)
    ax5.set_title('Total Volume Distribution', fontsize=14, fontweight='bold')

    # 6. Historical Price with Volume Context
    ax6 = fig.add_subplot(gs[2, :])
    hist_30d = stock.history(period="30d")
    ax6.plot(hist_30d.index, hist_30d['Close'], linewidth=2, color='#1a73e8', label='Stock Price')
    ax6.axhline(current_price, color='#ea4335', linestyle='--', linewidth=2,
                label=f'Current: ${current_price:.2f}')
    ax6.fill_between(hist_30d.index, hist_30d['Close'], alpha=0.1, color='#1a73e8')
    ax6.set_xlabel('Date', fontsize=12)
    ax6.set_ylabel('Stock Price ($)', fontsize=12)
    ax6.set_title('30-Day Price Action', fontsize=14, fontweight='bold')
    ax6.legend()
    ax6.grid(True, alpha=0.3)

    # Add summary statistics text box
    avg_pc_volume = options_df['pc_volume'].mean()
    avg_pc_oi = options_df['pc_oi'].mean()
    avg_iv = (options_df['atm_call_iv'].mean() + options_df['atm_put_iv'].mean()) / 2

    # Determine sentiment
    if avg_pc_volume < 0.7:
        sentiment = "BULLISH"
        sentiment_color = '#34a853'
    elif avg_pc_volume > 1.2:
        sentiment = "BEARISH"
        sentiment_color = '#ea4335'
    else:
        sentiment = "NEUTRAL"
        sentiment_color = '#1a73e8'

    stats_text = f"""Options Market Summary:

    • Current Price: ${current_price:.2f}
    • Avg IV (ATM): {avg_iv*100:.1f}%
    • P/C Ratio (Vol): {avg_pc_volume:.2f}
    • P/C Ratio (OI): {avg_pc_oi:.2f}
    • Sentiment: {sentiment}

    Interpretation:
    • P/C < 0.7 = Bullish
    • P/C 0.7-1.2 = Neutral
    • P/C > 1.2 = Bearish"""

    fig.text(0.02, 0.98, stats_text, transform=fig.transFigure,
             verticalalignment='top', fontsize=10, family='monospace',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    # Main title
    fig.suptitle(f'Alphabet (GOOGL) - Options Market Analysis\nGenerated: {datetime.now().strftime("%Y-%m-%d %H:%M")}',
                 fontsize=16, fontweight='bold', y=0.995)

    plt.savefig(f'{output_dir}/options_analysis.png', dpi=300, bbox_inches='tight')
    plt.savefig(f'{output_dir}/options_analysis.svg', format='svg', bbox_inches='tight')
    print(f"✓ Saved: {output_dir}/options_analysis.png")
    print(f"✓ Saved: {output_dir}/options_analysis.svg")

    return sentiment, avg_pc_volume, avg_iv

def main():
    print("Generating Options Market Analysis...")
    print("-" * 50)

    # Fetch options data
    options_df, stock, current_price = fetch_options_data("GOOGL")

    if options_df is None:
        print("Failed to fetch options data")
        return

    print(f"✓ Fetched options data for {len(options_df)} expirations")
    print(f"  Current price: ${current_price:.2f}")

    # Calculate IV metrics
    current_iv = options_df['atm_call_iv'].iloc[0] if len(options_df) > 0 else 0
    realized_vol, iv_percentile = calculate_iv_percentile(stock, current_iv)

    # Generate dashboard
    sentiment, avg_pc, avg_iv = plot_options_dashboard(options_df, stock, current_price)

    # Print summary
    print("\n" + "=" * 50)
    print("OPTIONS MARKET ANALYSIS SUMMARY")
    print("=" * 50)
    print(f"Current Stock Price: ${current_price:.2f}")
    print(f"Average IV (ATM): {avg_iv*100:.1f}%")
    print(f"Realized Vol (30d): {realized_vol*100:.1f}%")
    print(f"IV Percentile: {iv_percentile:.0f}th")
    print(f"\nP/C Ratio (Volume): {avg_pc:.2f}")
    print(f"Market Sentiment: {sentiment}")
    print("\nInterpretation:")
    if sentiment == "BULLISH":
        print("  • More call buying than put buying")
        print("  • Market expects upside")
    elif sentiment == "BEARISH":
        print("  • More put buying than call buying")
        print("  • Market pricing in downside risk")
    else:
        print("  • Balanced options activity")
        print("  • No strong directional bias")

    print("\nIV Analysis:")
    if current_iv > realized_vol:
        premium = ((current_iv - realized_vol) / realized_vol) * 100
        print(f"  • IV {premium:.1f}% above realized volatility")
        print("  • Options may be expensive (premium sellers favored)")
    else:
        discount = ((realized_vol - current_iv) / realized_vol) * 100
        print(f"  • IV {discount:.1f}% below realized volatility")
        print("  • Options may be cheap (premium buyers favored)")

    print("=" * 50)

if __name__ == "__main__":
    main()
