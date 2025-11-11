#!/usr/bin/env python3
"""
Fetch market capitalization data for tech sectors and major companies.
Validates sector market caps: AI, Semiconductors, Biotech, Crypto.
"""

import json
import yfinance as yf
from datetime import datetime
from pathlib import Path


# Major companies representing each sector
SECTOR_COMPANIES = {
    "AI": {
        "companies": ["MSFT", "GOOGL", "META", "NVDA", "AMZN", "TSLA"],
        "description": "AI/Tech Giants"
    },
    "Semiconductors": {
        "companies": ["NVDA", "TSM", "ASML", "AMD", "INTC", "QCOM", "AVGO", "TXN"],
        "description": "Semiconductor Industry"
    },
    "Biotech": {
        "companies": ["JNJ", "LLY", "NVO", "UNH", "ABBV", "MRK", "TMO", "ABT", "PFE"],
        "description": "Biotech/Healthcare"
    }
}

# ETFs for broader market data
SECTOR_ETFS = {
    "AI": "BOTZ",  # Global Robotics and AI ETF
    "Semiconductors": "SOXX",  # Semiconductor ETF
    "Biotech": "XBI",  # Biotech ETF
    "Crypto": "BITO",  # Bitcoin Strategy ETF (proxy)
}

# Robotics/humanoid companies (publicly traded)
ROBOTICS_COMPANIES = {
    "TSLA": "Tesla (Optimus)",
    "1211.HK": "BYD (robotics division)",
    "9888.HK": "UBTech Robotics",
    "IRBT": "iRobot",
    "ISRG": "Intuitive Surgical",
}


def get_market_cap(ticker):
    """Fetch current market cap for a ticker."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        market_cap = info.get('marketCap', 0)
        return market_cap
    except Exception as e:
        print(f"Error fetching {ticker}: {e}")
        return 0


def get_sector_market_caps():
    """Calculate total market cap for each sector."""
    results = {}

    for sector, data in SECTOR_COMPANIES.items():
        print(f"\n📊 Fetching {sector} sector...")
        companies = data["companies"]
        total_market_cap = 0
        company_details = {}

        for ticker in companies:
            market_cap = get_market_cap(ticker)
            total_market_cap += market_cap
            company_details[ticker] = {
                "market_cap": market_cap,
                "market_cap_billions": round(market_cap / 1e9, 2)
            }
            print(f"  {ticker}: ${market_cap/1e9:.2f}B")

        results[sector] = {
            "total_market_cap": total_market_cap,
            "total_market_cap_trillions": round(total_market_cap / 1e12, 2),
            "companies": company_details,
            "description": data["description"]
        }
        print(f"  Total {sector}: ${total_market_cap/1e12:.2f}T")

    return results


def get_robotics_market_caps():
    """Fetch market caps for publicly traded robotics companies."""
    print("\n🤖 Fetching Robotics companies...")
    results = {}
    total = 0

    for ticker, name in ROBOTICS_COMPANIES.items():
        market_cap = get_market_cap(ticker)
        results[ticker] = {
            "name": name,
            "market_cap": market_cap,
            "market_cap_billions": round(market_cap / 1e9, 2)
        }
        total += market_cap
        print(f"  {ticker} ({name}): ${market_cap/1e9:.2f}B")

    results["_total"] = {
        "total_market_cap": total,
        "total_market_cap_billions": round(total / 1e9, 2)
    }
    print(f"  Total Robotics (public): ${total/1e9:.2f}B")

    return results


def get_crypto_market_cap():
    """Get crypto market cap estimate using Bitcoin as proxy."""
    print("\n₿ Fetching Crypto market data...")
    # Bitcoin dominance is ~50%, so 2x BTC market cap = rough total crypto
    btc_cap = get_market_cap("BTC-USD")

    # Also check Ethereum
    eth_cap = get_market_cap("ETH-USD")

    # Rough estimate: BTC + ETH + 2x for all other crypto
    total_crypto_estimate = (btc_cap + eth_cap) * 2

    return {
        "BTC_market_cap": btc_cap,
        "BTC_market_cap_billions": round(btc_cap / 1e9, 2),
        "ETH_market_cap": eth_cap,
        "ETH_market_cap_billions": round(eth_cap / 1e9, 2),
        "total_crypto_estimate": total_crypto_estimate,
        "total_crypto_trillions": round(total_crypto_estimate / 1e12, 2),
        "note": "Rough estimate: (BTC + ETH) * 2"
    }


def main():
    """Main execution."""
    print("=" * 60)
    print("Market Cap Data Collection")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 60)

    # Collect all data
    data = {
        "timestamp": datetime.now().isoformat(),
        "sectors": get_sector_market_caps(),
        "crypto": get_crypto_market_cap(),
        "robotics": get_robotics_market_caps(),
    }

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"AI Sector: ${data['sectors']['AI']['total_market_cap_trillions']:.2f}T")
    print(f"Semiconductors: ${data['sectors']['Semiconductors']['total_market_cap_trillions']:.2f}T")
    print(f"Biotech: ${data['sectors']['Biotech']['total_market_cap_trillions']:.2f}T")
    print(f"Crypto (est): ${data['crypto']['total_crypto_trillions']:.2f}T")
    print(f"Robotics (public only): ${data['robotics']['_total']['total_market_cap_billions']:.2f}B")

    # Save to file
    output_path = Path(__file__).parent.parent / "data" / "market_caps.json"
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\n✅ Data saved to: {output_path}")

    return data


if __name__ == "__main__":
    main()
