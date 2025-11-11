#!/usr/bin/env python3
"""
Track humanoid robotics companies: funding, valuation, partnerships, production.
Data for: Unitree, Agility, UBTech, Tesla, Figure AI, Boston Dynamics,
Apptronik, 1X Technologies, Sanctuary AI, Fourier Intelligence.
"""

import json
from datetime import datetime
from pathlib import Path


# Humanoid Robotics Companies Database
COMPANIES = {
    "Unitree Robotics": {
        "ticker": "Private",
        "country": "China",
        "headquarters": "Hangzhou, China",
        "founded": 2016,
        "products": ["G1", "H1", "Go2 (quadruped)"],
        "key_product": "G1 ($16,000)",
        "status": "Pre-IPO (Q4 2025 expected)",
        "last_known_valuation": "~$1B (estimated)",
        "production_capacity": {
            "current_units_per_year": "TBD",
            "target_units_per_year": "100,000+ (2025 goal)",
            "actual_deployed": "Unknown"
        },
        "funding": {
            "total_raised": "$200M+ (estimated)",
            "latest_round": "Series B (2024)",
            "investors": ["Tencent", "Shunwei Capital", "Matrix Partners China"]
        },
        "partnerships": [
            "Various Chinese manufacturing partners",
            "Consumer robotics distribution channels"
        ],
        "technology": {
            "ai_integration": "Proprietary + potential OpenAI partnership",
            "key_differentiator": "Low-cost manufacturing, $16K price point"
        },
        "research_needed": [
            "IPO timeline confirmation",
            "Actual production numbers for 2025",
            "Latest funding round details"
        ]
    },

    "Agility Robotics": {
        "ticker": "Private",
        "country": "USA",
        "headquarters": "Corvallis, Oregon",
        "founded": 2015,
        "products": ["Digit"],
        "key_product": "Digit (bipedal warehouse robot)",
        "status": "Private, Series B",
        "last_known_valuation": "$1.5B+ (estimated)",
        "production_capacity": {
            "robofab_capacity": "10,000 units/year",
            "robofab_status": "Operational in Salem, OR",
            "actual_deployed": "100+ units (estimated, 2024)"
        },
        "funding": {
            "total_raised": "$350M+",
            "latest_round": "Series B ($150M, 2023)",
            "investors": ["Amazon Industrial Innovation Fund", "DCVC", "Playground Global", "SOMA Capital"]
        },
        "partnerships": [
            "Amazon (warehouse pilots)",
            "GXO Logistics",
            "Schaeffler (manufacturing)"
        ],
        "technology": {
            "ai_integration": "Proprietary AI + computer vision",
            "key_differentiator": "Purpose-built for logistics, RoboFab manufacturing scale"
        },
        "research_needed": [
            "Latest deployment numbers at Amazon",
            "RoboFab production ramp status",
            "2025 revenue projections"
        ]
    },

    "UBTech Robotics": {
        "ticker": "9888.HK",
        "country": "China",
        "headquarters": "Shenzhen, China",
        "founded": 2012,
        "products": ["Walker S1", "Walker S2", "Walker X"],
        "key_product": "Walker S (service humanoid)",
        "status": "Public (HKEX)",
        "last_known_valuation": "$2B+ (market cap)",
        "production_capacity": {
            "current_units_per_year": "TBD",
            "target_units_per_year": "50,000+",
            "actual_deployed": "Unknown"
        },
        "funding": {
            "total_raised": "$820M (pre-IPO)",
            "ipo_date": "December 2023",
            "investors": ["Tencent", "CDH Investments", "Qiming Venture Partners"]
        },
        "partnerships": [
            "China Mobile (5G robotics)",
            "Various Chinese municipalities (smart city projects)"
        ],
        "technology": {
            "ai_integration": "Proprietary + Tencent AI",
            "key_differentiator": "First humanoid robotics IPO, Chinese government backing"
        },
        "research_needed": [
            "Current market cap and stock performance",
            "Post-IPO production numbers",
            "Government subsidy details"
        ]
    },

    "Tesla (Optimus)": {
        "ticker": "TSLA",
        "country": "USA",
        "headquarters": "Austin, Texas",
        "founded": 2003,
        "products": ["Optimus Gen 2", "Optimus Gen 3 (announced)"],
        "key_product": "Optimus humanoid robot",
        "status": "Public",
        "optimus_status": "Internal development, limited external deployment",
        "production_capacity": {
            "current_units_per_year": "~1,000 (estimated, internal use)",
            "target_units_per_year": "Millions (Musk target)",
            "actual_deployed": "~50-100 in Tesla factories (estimated)"
        },
        "funding": {
            "total_raised": "Public company (TSLA market cap ~$800B)",
            "robotics_investment": "$5B+ estimated R&D",
            "investors": "Public shareholders"
        },
        "partnerships": [
            "Internal Tesla factories",
            "No announced external partnerships yet"
        ],
        "technology": {
            "ai_integration": "Tesla FSD AI + Dojo training",
            "key_differentiator": "Vertical integration, AI expertise from autonomous driving"
        },
        "research_needed": [
            "Gen 3 specifications and timeline",
            "Actual deployment numbers in factories",
            "External sales timeline (if any)"
        ]
    },

    "Figure AI": {
        "ticker": "Private",
        "country": "USA",
        "headquarters": "Sunnyvale, California",
        "founded": 2022,
        "products": ["Figure 01", "Figure 02", "Figure 03 (development)"],
        "key_product": "Figure 02 (general-purpose humanoid)",
        "status": "Private, Series B",
        "last_known_valuation": "$2.6B (Feb 2024)",
        "production_capacity": {
            "current_units_per_year": "TBD",
            "target_units_per_year": "TBD",
            "actual_deployed": "Pilots at BMW"
        },
        "funding": {
            "total_raised": "$754M",
            "latest_round": "Series B ($675M, Feb 2024)",
            "investors": [
                "OpenAI", "Microsoft", "Nvidia", "Jeff Bezos", "Intel Capital",
                "ARK Invest", "Parkway Venture Capital", "Aliya Capital"
            ]
        },
        "partnerships": [
            "OpenAI (AI integration)",
            "BMW (manufacturing pilot)",
            "Potential additional enterprise pilots"
        ],
        "technology": {
            "ai_integration": "OpenAI partnership (vision + language models)",
            "key_differentiator": "Star-studded investor base, OpenAI AI integration"
        },
        "research_needed": [
            "BMW pilot results and scale",
            "Figure 03 development status",
            "Commercial deployment timeline"
        ]
    },

    "Boston Dynamics": {
        "ticker": "Private (Hyundai)",
        "country": "USA",
        "headquarters": "Waltham, Massachusetts",
        "founded": 1992,
        "products": ["Atlas (electric)", "Spot (quadruped)", "Stretch (logistics)"],
        "key_product": "Electric Atlas (latest humanoid)",
        "status": "Private, owned by Hyundai Motor Group",
        "last_known_valuation": "$1.1B (Hyundai acquisition, 2020)",
        "production_capacity": {
            "current_units_per_year": "Limited (R&D focus)",
            "target_units_per_year": "TBD",
            "actual_deployed": "Spot: 1,000+, Atlas: <10 (research)"
        },
        "funding": {
            "total_raised": "Acquired by Hyundai for $1.1B",
            "previous_owners": "Google, SoftBank",
            "investors": "Hyundai Motor Group"
        },
        "partnerships": [
            "Hyundai (integration into manufacturing)",
            "Various research institutions",
            "Industrial customers for Spot"
        ],
        "technology": {
            "ai_integration": "Proprietary AI + Hyundai integration",
            "key_differentiator": "Advanced mobility and dynamics, industry-leading R&D"
        },
        "research_needed": [
            "Electric Atlas commercial timeline",
            "Hyundai factory integration status",
            "Production plans for humanoid Atlas"
        ]
    },

    "Apptronik": {
        "ticker": "Private",
        "country": "USA",
        "headquarters": "Austin, Texas",
        "founded": 2016,
        "products": ["Apollo"],
        "key_product": "Apollo (warehouse & logistics humanoid)",
        "status": "Private, Series A",
        "last_known_valuation": "$500M+ (estimated)",
        "production_capacity": {
            "current_units_per_year": "TBD",
            "target_units_per_year": "TBD",
            "actual_deployed": "Pilots (Mercedes, Walmart)"
        },
        "funding": {
            "total_raised": "$100M+",
            "latest_round": "Series A ($50M, 2023)",
            "investors": ["Calibrate Ventures", "Mercury Fund", "ACME Capital", "Plus Capital"]
        },
        "partnerships": [
            "Mercedes-Benz (manufacturing pilot)",
            "NASA (technology development)",
            "GXO Logistics (warehouse pilots)"
        ],
        "technology": {
            "ai_integration": "Proprietary AI for logistics",
            "key_differentiator": "NASA heritage, modular design, logistics focus"
        },
        "research_needed": [
            "Mercedes pilot scale and results",
            "Walmart deployment status",
            "Production timeline"
        ]
    },

    "1X Technologies": {
        "ticker": "Private",
        "country": "Norway/USA",
        "headquarters": "Moss, Norway / San Francisco, CA",
        "founded": 2014,
        "products": ["Neo (consumer)", "EVE (industrial)"],
        "key_product": "Neo (home assistant humanoid)",
        "status": "Private, Series B",
        "last_known_valuation": "$600M+ (estimated)",
        "production_capacity": {
            "current_units_per_year": "TBD",
            "target_units_per_year": "Consumer scale (TBD)",
            "actual_deployed": "Limited pilots"
        },
        "funding": {
            "total_raised": "$125M+",
            "latest_round": "Series B ($100M, 2024)",
            "investors": ["OpenAI", "Tiger Global", "EQT Ventures"]
        },
        "partnerships": [
            "OpenAI (AI integration + investment)",
            "ADT (security services pilot)"
        ],
        "technology": {
            "ai_integration": "OpenAI partnership (similar to Figure)",
            "key_differentiator": "Consumer focus, wheeled base for stability/cost"
        },
        "research_needed": [
            "Neo consumer launch timeline",
            "ADT pilot results",
            "Manufacturing location and scale"
        ]
    },

    "Sanctuary AI": {
        "ticker": "Private",
        "country": "Canada",
        "headquarters": "Vancouver, British Columbia",
        "founded": 2018,
        "products": ["Phoenix (Gen 7)"],
        "key_product": "Phoenix humanoid robot",
        "status": "Private, Series A",
        "last_known_valuation": "$500M+ (estimated)",
        "production_capacity": {
            "current_units_per_year": "TBD",
            "target_units_per_year": "TBD",
            "actual_deployed": "Pilots in retail/logistics"
        },
        "funding": {
            "total_raised": "$100M+",
            "latest_round": "Series A ($60M, 2023)",
            "investors": ["BDC Capital", "Accenture Ventures", "Bell", "Magna", "Verizon Ventures"]
        },
        "partnerships": [
            "Canadian Tire (retail pilot)",
            "Accenture (enterprise deployment)",
            "Various logistics partners"
        ],
        "technology": {
            "ai_integration": "Carbon AI platform (proprietary)",
            "key_differentiator": "Advanced hand dexterity, enterprise SaaS model"
        },
        "research_needed": [
            "Canadian Tire pilot results",
            "Production timeline",
            "Commercial traction metrics"
        ]
    },

    "Fourier Intelligence": {
        "ticker": "Private",
        "country": "China/Singapore",
        "headquarters": "Shanghai, China / Singapore",
        "founded": 2015,
        "products": ["GR-1", "GR-2", "Medical rehabilitation robots"],
        "key_product": "GR-1 (healthcare humanoid)",
        "status": "Private",
        "last_known_valuation": "$500M+ (estimated)",
        "production_capacity": {
            "current_units_per_year": "TBD",
            "target_units_per_year": "Healthcare market focus",
            "actual_deployed": "Hospitals in China and Singapore"
        },
        "funding": {
            "total_raised": "$100M+",
            "latest_round": "Series C (2023)",
            "investors": ["Saudi Aramco Entrepreneurship Ventures", "CICC Capital", "IDG Capital"]
        },
        "partnerships": [
            "Healthcare providers in China",
            "Singapore hospitals",
            "Saudi healthcare initiative"
        ],
        "technology": {
            "ai_integration": "Healthcare-specific AI",
            "key_differentiator": "Medical/rehab focus, Asian market penetration"
        },
        "research_needed": [
            "Healthcare adoption rates",
            "GR-2 specifications and timeline",
            "Middle East expansion status"
        ]
    }
}


def generate_summary_stats():
    """Generate summary statistics across all companies."""
    total_companies = len(COMPANIES)

    # Count by country
    countries = {}
    for company, data in COMPANIES.items():
        country = data.get("country", "Unknown")
        countries[country] = countries.get(country, 0) + 1

    # Estimate total funding
    total_funding_min = 0
    for company, data in COMPANIES.items():
        funding_str = data.get("funding", {}).get("total_raised", "0")
        # Extract numeric value (rough estimate)
        if "$" in funding_str:
            amount_str = funding_str.replace("$", "").replace("M", "").replace("B", "000").replace("+", "").replace("(estimated)", "").strip()
            if "(" in amount_str:
                amount_str = amount_str.split("(")[0].strip()
            try:
                if "B" in funding_str:
                    total_funding_min += float(amount_str)
                else:
                    total_funding_min += float(amount_str.split()[0]) if amount_str else 0
            except:
                pass

    return {
        "total_companies": total_companies,
        "by_country": countries,
        "estimated_total_funding_millions": round(total_funding_min),
        "private_companies": sum(1 for c in COMPANIES.values() if c["ticker"] == "Private" or "Private" in c["ticker"]),
        "public_companies": sum(1 for c in COMPANIES.values() if c["ticker"] not in ["Private"] and "Private" not in c["ticker"]),
    }


def main():
    """Main execution."""
    print("=" * 80)
    print("Humanoid Robotics Company Tracker")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 80)

    # Display summary
    summary = generate_summary_stats()
    print(f"\n📊 Summary Statistics:")
    print(f"  Total Companies: {summary['total_companies']}")
    print(f"  Public Companies: {summary['public_companies']}")
    print(f"  Private Companies: {summary['private_companies']}")
    print(f"  By Country: {summary['by_country']}")
    print(f"  Estimated Total Funding: ${summary['estimated_total_funding_millions']}M+")

    # List companies
    print(f"\n🤖 Companies:\n")
    for i, (company, data) in enumerate(COMPANIES.items(), 1):
        print(f"{i}. {company} ({data['country']})")
        print(f"   Product: {data['key_product']}")
        print(f"   Status: {data['status']}")
        print(f"   Funding: {data['funding']['total_raised']}")
        if data.get('last_known_valuation'):
            print(f"   Valuation: {data['last_known_valuation']}")
        print()

    # Save data
    output_data = {
        "timestamp": datetime.now().isoformat(),
        "summary": summary,
        "companies": COMPANIES
    }

    output_path = Path(__file__).parent.parent / "data" / "companies.json"
    with open(output_path, 'w') as f:
        json.dump(output_data, f, indent=2)

    print(f"✅ Data saved to: {output_path}")

    # Research priorities
    print("\n🔍 Research Priorities (validate these manually):")
    for company, data in COMPANIES.items():
        if data.get("research_needed"):
            print(f"\n{company}:")
            for item in data["research_needed"]:
                print(f"  - {item}")

    return output_data


if __name__ == "__main__":
    main()
