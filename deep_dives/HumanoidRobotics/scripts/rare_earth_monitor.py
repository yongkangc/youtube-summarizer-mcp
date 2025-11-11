#!/usr/bin/env python3
"""
Monitor rare earth elements (REE) pricing and supply chain data.
Critical for humanoid robotics manufacturing: motors, batteries, sensors.
"""

import json
from datetime import datetime
from pathlib import Path


# Rare Earth Elements Critical for Robotics
CRITICAL_REE = {
    "Neodymium (Nd)": {
        "use_case": "Permanent magnets for motors (servo motors, actuators)",
        "importance": "Critical - all humanoid joints use Nd-based motors",
        "china_production_share": "85%",
        "price_2023_avg": "$65-75/kg",
        "price_2024_est": "$60-70/kg",
        "supply_risk": "High - China dominance",
        "alternatives": "Ferrite magnets (lower performance)",
    },
    "Dysprosium (Dy)": {
        "use_case": "High-temperature permanent magnets (added to Nd magnets)",
        "importance": "Critical - improves motor efficiency at high temps",
        "china_production_share": "90%+",
        "price_2023_avg": "$350-450/kg",
        "price_2024_est": "$320-400/kg",
        "supply_risk": "Very High - most scarce heavy REE",
        "alternatives": "Limited - Terbium (also scarce)",
    },
    "Praseodymium (Pr)": {
        "use_case": "Permanent magnets (often mixed with Nd)",
        "importance": "High - cost-effective Nd substitute",
        "china_production_share": "85%",
        "price_2023_avg": "$60-70/kg",
        "price_2024_est": "$55-65/kg",
        "supply_risk": "High - similar to Nd",
        "alternatives": "Neodymium (interchangeable in many uses)",
    },
    "Samarium (Sm)": {
        "use_case": "SmCo magnets (high-temp applications)",
        "importance": "Medium - used in specialized actuators",
        "china_production_share": "75%",
        "price_2023_avg": "$8-12/kg",
        "price_2024_est": "$7-11/kg",
        "supply_risk": "Medium",
        "alternatives": "Nd-Fe-B magnets (more common)",
    },
    "Lanthanum (La)": {
        "use_case": "Batteries (NiMH), camera lenses, sensors",
        "importance": "Medium - less critical than Nd/Dy",
        "china_production_share": "80%",
        "price_2023_avg": "$2-3/kg",
        "price_2024_est": "$2-3/kg",
        "supply_risk": "Low-Medium - more abundant",
        "alternatives": "Lithium batteries (replacing NiMH)",
    },
}


# Global REE Production by Country (2024 estimates)
REE_PRODUCTION_BY_COUNTRY = {
    "China": {
        "production_tonnes": "210,000",
        "global_share": "70%",
        "reserves_tonnes": "44,000,000",
        "notes": "Dominant player, controls processing even for foreign-mined REE",
        "policy": "Export restrictions, domestic subsidies for manufacturing"
    },
    "USA": {
        "production_tonnes": "43,000",
        "global_share": "14%",
        "reserves_tonnes": "2,300,000",
        "notes": "Mountain Pass mine (MP Materials), but ships to China for processing",
        "policy": "Building domestic processing, IRA subsidies"
    },
    "Australia": {
        "production_tonnes": "24,000",
        "global_share": "8%",
        "reserves_tonnes": "4,200,000",
        "notes": "Lynas Rare Earths (processes in Malaysia)",
        "policy": "Strategic partnership with USA/Japan"
    },
    "Myanmar": {
        "production_tonnes": "26,000",
        "global_share": "8%",
        "reserves_tonnes": "1,000,000",
        "notes": "Exports primarily to China (illegal mining concerns)",
        "policy": "Unstable due to political situation"
    },
    "Other": {
        "production_tonnes": "~10,000",
        "global_share": "3%",
        "reserves_tonnes": "Various",
        "notes": "India, Brazil, Vietnam, Russia, etc.",
        "policy": "Various"
    }
}


# REE Cost Impact on Robotics
REE_COST_ANALYSIS = {
    "typical_humanoid_robot": {
        "total_motors": "30-40 servo motors",
        "nd_per_motor": "50-200g",
        "total_nd_per_robot": "2-6 kg",
        "nd_cost_per_robot": "$120-420 (at $60-70/kg)",
        "percentage_of_16k_robot": "0.75-2.6%",
        "notes": "Relatively small % of total cost, but supply risk is real"
    },
    "at_scale_production": {
        "units_per_year": "100,000 robots",
        "total_nd_needed": "200-600 tonnes/year",
        "percentage_of_global_nd_production": "~0.5-1.5%",
        "risk_assessment": "Manageable for single company, but if 10 companies scale simultaneously...",
        "china_dependency": "Critical bottleneck - 85% of Nd from China"
    }
}


# Geopolitical Risks
GEOPOLITICAL_RISKS = {
    "US_China_Decoupling": {
        "risk_level": "High",
        "scenario": "US restricts Chinese robotics imports, China restricts REE exports",
        "impact": "US robotics companies face 2-3x REE costs, potential supply disruption",
        "mitigation": "MP Materials domestic processing, recycling, alternative magnet research",
        "probability": "30-40% in next 3 years"
    },
    "China_Export_Controls": {
        "risk_level": "Medium-High",
        "scenario": "China imposes export quotas on processed REE (already done for Ga, Ge)",
        "impact": "Global REE prices spike 50-100%, favors Chinese manufacturers",
        "mitigation": "Limited - takes 5-10 years to build alternative supply chain",
        "probability": "40-50% in next 2 years",
        "precedent": "Gallium/Germanium export controls (2023), Magnet export restrictions (2024)"
    },
    "US_Subsidies_Advantage": {
        "risk_level": "Opportunity",
        "scenario": "IRA + CHIPS Act subsidies accelerate US REE processing",
        "impact": "US robotics companies get domestic supply by 2026-2027",
        "mitigation": "N/A - positive for US companies",
        "probability": "60% partial success",
        "funding": "$500M+ in grants (MP Materials, others)"
    }
}


# Alternative Technologies
ALTERNATIVES_RESEARCH = {
    "Rare_Earth_Free_Magnets": {
        "technology": "Iron Nitride (FeN), Manganese-based magnets",
        "status": "Research phase (TRL 3-4)",
        "timeline": "5-10 years to commercialization",
        "performance": "Potentially competitive with Nd-Fe-B",
        "companies": "Niron Magnetics, Toshiba, others",
        "risk": "Unproven at scale, manufacturing challenges"
    },
    "Magnet_Recycling": {
        "technology": "Urban mining (recycle REE from e-waste, old motors)",
        "status": "Commercial but small scale",
        "timeline": "Current - scaling now",
        "performance": "Same as virgin REE",
        "companies": "Apple (recycling bots), Cyclic Materials, others",
        "potential": "Could supply 10-20% of demand by 2030"
    },
    "Ferrite_Magnets": {
        "technology": "No REE, lower performance",
        "status": "Mature technology",
        "timeline": "Available now",
        "performance": "50-70% weaker than Nd-Fe-B",
        "use_case": "Low-cost applications, but not suitable for humanoid joints (need high torque-to-weight)",
        "risk": "Performance penalty too high for premium robots"
    }
}


def main():
    """Main execution."""
    print("=" * 80)
    print("Rare Earth Elements (REE) Supply Chain Monitor")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 80)

    # Display critical REE
    print("\n⚗️  Critical REE for Humanoid Robotics:\n")
    for element, data in CRITICAL_REE.items():
        print(f"{element}")
        print(f"  Use: {data['use_case']}")
        print(f"  Importance: {data['importance']}")
        print(f"  China Share: {data['china_production_share']}")
        print(f"  Price (2024): {data['price_2024_est']}")
        print(f"  Risk: {data['supply_risk']}\n")

    # Production by country
    print("\n🌍 Global REE Production:\n")
    for country, data in REE_PRODUCTION_BY_COUNTRY.items():
        print(f"{country}: {data['global_share']} ({data['production_tonnes']} tonnes/year)")
        print(f"  {data['notes']}\n")

    # Cost analysis
    print("\n💰 REE Cost Impact:\n")
    print(f"Typical humanoid robot:")
    print(f"  Motors: {REE_COST_ANALYSIS['typical_humanoid_robot']['total_motors']}")
    print(f"  Nd per robot: {REE_COST_ANALYSIS['typical_humanoid_robot']['total_nd_per_robot']}")
    print(f"  Nd cost: {REE_COST_ANALYSIS['typical_humanoid_robot']['nd_cost_per_robot']}")
    print(f"  % of $16K robot: {REE_COST_ANALYSIS['typical_humanoid_robot']['percentage_of_16k_robot']}\n")

    print(f"At 100K units/year scale:")
    print(f"  Total Nd needed: {REE_COST_ANALYSIS['at_scale_production']['total_nd_needed']}")
    print(f"  % of global production: {REE_COST_ANALYSIS['at_scale_production']['percentage_of_global_nd_production']}")
    print(f"  Risk: {REE_COST_ANALYSIS['at_scale_production']['risk_assessment']}\n")

    # Geopolitical risks
    print("\n⚠️  Geopolitical Risks:\n")
    for risk, data in GEOPOLITICAL_RISKS.items():
        print(f"{risk.replace('_', ' ')}")
        print(f"  Level: {data['risk_level']}")
        print(f"  Scenario: {data['scenario']}")
        print(f"  Probability: {data['probability']}\n")

    # Save data
    output_data = {
        "timestamp": datetime.now().isoformat(),
        "critical_ree": CRITICAL_REE,
        "production_by_country": REE_PRODUCTION_BY_COUNTRY,
        "cost_analysis": REE_COST_ANALYSIS,
        "geopolitical_risks": GEOPOLITICAL_RISKS,
        "alternatives": ALTERNATIVES_RESEARCH
    }

    output_path = Path(__file__).parent.parent / "data" / "rare_earth_data.json"
    with open(output_path, 'w') as f:
        json.dump(output_data, f, indent=2)

    print(f"✅ Data saved to: {output_path}")

    # Key insights
    print("\n🔑 Key Insights:")
    print("1. China controls 70% of REE production, 85-90% of Nd/Dy processing")
    print("2. REE cost is small (~1-2% of robot cost), but supply risk is HIGH")
    print("3. At 100K robots/year, single company needs 0.5-1.5% of global Nd production")
    print("4. If 10 companies scale simultaneously, REE becomes a bottleneck")
    print("5. US-China decoupling could spike REE costs 50-100% for Western companies")
    print("6. China-based companies (Unitree, UBTech, Fourier) have structural advantage")

    return output_data


if __name__ == "__main__":
    main()
