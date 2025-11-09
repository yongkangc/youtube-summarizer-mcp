#!/usr/bin/env python3
"""
Fetch financial data for Google (Alphabet) and competitors from Yahoo Finance.
Outputs cleaned CSV files for analysis.
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

# Configuration
TICKERS = {
    'GOOGL': 'Alphabet (Google)',
    'MSFT': 'Microsoft',
    'AMZN': 'Amazon',
    'META': 'Meta',
}

DATA_DIR = '../data'
YEARS_HISTORY = 10

def fetch_stock_data(ticker, years=10):
    """Fetch historical stock data and financials."""
    print(f"Fetching data for {ticker}...")

    stock = yf.Ticker(ticker)

    # Get historical price data
    end_date = datetime.now()
    start_date = end_date - timedelta(days=years*365)
    hist = stock.history(start=start_date, end=end_date)

    # Get financial statements
    financials = stock.financials
    quarterly_financials = stock.quarterly_financials
    balance_sheet = stock.balance_sheet
    cashflow = stock.cashflow
    quarterly_cashflow = stock.quarterly_cashflow

    return {
        'history': hist,
        'financials': financials,
        'quarterly_financials': quarterly_financials,
        'balance_sheet': balance_sheet,
        'cashflow': cashflow,
        'quarterly_cashflow': quarterly_cashflow,
        'info': stock.info
    }

def extract_key_metrics(data_dict, ticker):
    """Extract key financial metrics into a clean dataframe."""
    info = data_dict['info']

    metrics = {
        'ticker': ticker,
        'company_name': info.get('longName', ''),
        'market_cap': info.get('marketCap', None),
        'enterprise_value': info.get('enterpriseValue', None),
        'trailing_pe': info.get('trailingPE', None),
        'forward_pe': info.get('forwardPE', None),
        'peg_ratio': info.get('pegRatio', None),
        'price_to_sales': info.get('priceToSalesTrailing12Months', None),
        'price_to_book': info.get('priceToBook', None),
        'ev_to_revenue': info.get('enterpriseToRevenue', None),
        'ev_to_ebitda': info.get('enterpriseToEbitda', None),
        'profit_margin': info.get('profitMargins', None),
        'operating_margin': info.get('operatingMargins', None),
        'roe': info.get('returnOnEquity', None),
        'roa': info.get('returnOnAssets', None),
        'revenue_growth': info.get('revenueGrowth', None),
        'earnings_growth': info.get('earningsGrowth', None),
        'current_price': info.get('currentPrice', None),
        'total_revenue': info.get('totalRevenue', None),
        'revenue_per_share': info.get('revenuePerShare', None),
        'total_cash': info.get('totalCash', None),
        'total_debt': info.get('totalDebt', None),
        'free_cashflow': info.get('freeCashflow', None),
        'operating_cashflow': info.get('operatingCashflow', None),
    }

    return pd.Series(metrics)

def create_annual_summary(data_dict, ticker):
    """Create annual summary from quarterly data."""
    try:
        qf = data_dict['quarterly_financials']
        qc = data_dict['quarterly_cashflow']

        if qf is None or qf.empty:
            print(f"Warning: No quarterly financials for {ticker}")
            return pd.DataFrame()

        # Convert column names to datetime and extract year
        annual_data = []

        # Group by year and sum
        for col in qf.columns:
            year = pd.to_datetime(col).year

            revenue = qf.loc['Total Revenue', col] if 'Total Revenue' in qf.index else None
            gross_profit = qf.loc['Gross Profit', col] if 'Gross Profit' in qf.index else None
            operating_income = qf.loc['Operating Income', col] if 'Operating Income' in qf.index else None
            net_income = qf.loc['Net Income', col] if 'Net Income' in qf.index else None

            # Try to get CapEx from cashflow
            capex = None
            if qc is not None and not qc.empty and col in qc.columns:
                if 'Capital Expenditure' in qc.index:
                    capex = abs(qc.loc['Capital Expenditure', col])
                elif 'Capital Expenditures' in qc.index:
                    capex = abs(qc.loc['Capital Expenditures', col])

            annual_data.append({
                'ticker': ticker,
                'year': year,
                'quarter': pd.to_datetime(col),
                'revenue': revenue,
                'gross_profit': gross_profit,
                'operating_income': operating_income,
                'net_income': net_income,
                'capex': capex,
            })

        df = pd.DataFrame(annual_data)

        # Calculate margins
        if not df.empty:
            df['gross_margin'] = df['gross_profit'] / df['revenue']
            df['operating_margin'] = df['operating_income'] / df['revenue']
            df['net_margin'] = df['net_income'] / df['revenue']

        return df

    except Exception as e:
        print(f"Error creating annual summary for {ticker}: {e}")
        return pd.DataFrame()

def main():
    """Main execution function."""
    # Create data directory if it doesn't exist
    os.makedirs(DATA_DIR, exist_ok=True)

    # Fetch data for all tickers
    all_data = {}
    for ticker, name in TICKERS.items():
        print(f"\n{'='*60}")
        print(f"Processing {name} ({ticker})")
        print('='*60)

        try:
            data = fetch_stock_data(ticker, YEARS_HISTORY)
            all_data[ticker] = data
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            continue

    # Extract current metrics
    print("\n" + "="*60)
    print("Extracting current metrics...")
    print("="*60)

    current_metrics = []
    for ticker, data in all_data.items():
        try:
            metrics = extract_key_metrics(data, ticker)
            current_metrics.append(metrics)
        except Exception as e:
            print(f"Error extracting metrics for {ticker}: {e}")

    if current_metrics:
        current_df = pd.DataFrame(current_metrics)
        output_file = os.path.join(DATA_DIR, 'current_metrics.csv')
        current_df.to_csv(output_file, index=False)
        print(f"\nSaved current metrics to {output_file}")
        print(current_df[['ticker', 'company_name', 'market_cap', 'trailing_pe', 'revenue_growth']])

    # Create annual summaries
    print("\n" + "="*60)
    print("Creating annual summaries...")
    print("="*60)

    all_annual = []
    for ticker, data in all_data.items():
        try:
            annual = create_annual_summary(data, ticker)
            if not annual.empty:
                all_annual.append(annual)
        except Exception as e:
            print(f"Error creating annual summary for {ticker}: {e}")

    if all_annual:
        annual_df = pd.concat(all_annual, ignore_index=True)
        annual_df = annual_df.sort_values(['ticker', 'quarter'])
        output_file = os.path.join(DATA_DIR, 'quarterly_financials.csv')
        annual_df.to_csv(output_file, index=False)
        print(f"\nSaved quarterly financials to {output_file}")
        print(f"Total quarters: {len(annual_df)}")

    # Save historical prices
    print("\n" + "="*60)
    print("Saving historical prices...")
    print("="*60)

    for ticker, data in all_data.items():
        try:
            hist = data['history']
            output_file = os.path.join(DATA_DIR, f'{ticker}_price_history.csv')
            hist.to_csv(output_file)
            print(f"Saved {ticker} price history: {len(hist)} days")
        except Exception as e:
            print(f"Error saving price history for {ticker}: {e}")

    print("\n" + "="*60)
    print("Data fetching complete!")
    print("="*60)

if __name__ == '__main__':
    main()
