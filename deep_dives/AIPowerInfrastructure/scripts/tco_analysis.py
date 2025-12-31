#!/usr/bin/env python3
"""
AI Power Infrastructure TCO (Total Cost of Ownership) Analysis
Compares onsite gas vs grid economics, redundancy costs, fuel sensitivity
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# TCO components by technology ($/MWh all-in)
tco_by_technology = {
    "Aeroderivative": {
        "capex_amortized_mwh": 25,  # $1850/kW over 15 years, 85% capacity factor
        "fuel_cost_mwh": 27,        # Heat rate 9500 BTU/kWh @ $3/MMBtu
        "om_cost_mwh": 8,
        "redundancy_overhead_pct": 15,  # N+1 overbuild
        "total_tco_mwh": 69,
        "grid_equivalent_mwh": 60
    },
    "IGT": {
        "capex_amortized_mwh": 22,
        "fuel_cost_mwh": 30,        # Heat rate 10000 BTU/kWh
        "om_cost_mwh": 6,
        "redundancy_overhead_pct": 12,
        "total_tco_mwh": 65,
        "grid_equivalent_mwh": 60
    },
    "RICE": {
        "capex_amortized_mwh": 26,
        "fuel_cost_mwh": 25.5,      # Heat rate 8500 BTU/kWh
        "om_cost_mwh": 10,          # Higher O&M (more moving parts)
        "redundancy_overhead_pct": 10,  # Easier redundancy with small units
        "total_tco_mwh": 68,
        "grid_equivalent_mwh": 60
    },
    "Fuel Cell (SOFC)": {
        "capex_amortized_mwh": 50,  # $3500/kW, 5-6 year stack replacement
        "fuel_cost_mwh": 19.5,      # Heat rate 6500 BTU/kWh
        "om_cost_mwh": 15,          # Stack replacements
        "redundancy_overhead_pct": 8,
        "total_tco_mwh": 91,
        "grid_equivalent_mwh": 60
    },
    "CCGT (H-Class)": {
        "capex_amortized_mwh": 12,  # $1000/kW, most efficient
        "fuel_cost_mwh": 18,        # Heat rate 6000 BTU/kWh
        "om_cost_mwh": 4,
        "redundancy_overhead_pct": 30,  # Massive overbuild for large units
        "total_tco_mwh": 44,
        "grid_equivalent_mwh": 60
    }
}

# Arbitrage model parameters
arbitrage_model = {
    "datacenter_capacity_mw": 200,
    "revenue_per_mw_annual": 11_000_000,
    "onsite_deployment_month": 6,
    "grid_deployment_month": 36,
    "onsite_capex_per_kw": 1850,
    "onsite_om_mwh": 20,
    "heat_rate_btu_kwh": 9000,
    "gas_price_mmbtu": 3.00,
    "grid_power_cost_mwh": 60,
    "hours_per_month": 730,
    "amortization_years": 10
}

# Redundancy configurations
redundancy_configs = {
    "N+1 (Aeros)": {
        "overbuild_ratio": 1.15,
        "tech": "Aeroderivative",
        "example": "10x 34MW LM2500 for 300MW load"
    },
    "N+1+1 (RICE)": {
        "overbuild_ratio": 1.25,
        "tech": "RICE",
        "example": "50x 4.5MW Jenbacher for 180MW load"
    },
    "2x CCGT + Aero backup": {
        "overbuild_ratio": 1.40,
        "tech": "CCGT",
        "example": "2x 400MW CCGT + 4x LM2500 for 600MW load"
    },
    "VoltaGrid Style": {
        "overbuild_ratio": 1.64,
        "tech": "RICE",
        "example": "2.3GW generation for 1.4GW datacenter (Vantage)"
    }
}

# Fuel price sensitivity
fuel_sensitivity = {
    "gas_prices_mmbtu": [2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 7.0, 10.0],
    "grid_breakeven_mwh": 60  # Constant grid price
}


def save_data():
    """Save TCO data to JSON"""
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    with open(data_dir / "tco_by_technology.json", "w") as f:
        json.dump(tco_by_technology, f, indent=2)

    with open(data_dir / "arbitrage_model.json", "w") as f:
        json.dump(arbitrage_model, f, indent=2)

    with open(data_dir / "redundancy_configs.json", "w") as f:
        json.dump(redundancy_configs, f, indent=2)

    with open(data_dir / "fuel_sensitivity.json", "w") as f:
        json.dump(fuel_sensitivity, f, indent=2)

    print(f"Saved TCO data to {data_dir}")


def plot_tco_by_technology():
    """Plot stacked TCO breakdown by technology"""
    fig, ax = plt.subplots(figsize=(14, 8))

    techs = list(tco_by_technology.keys())
    capex = [tco_by_technology[t]["capex_amortized_mwh"] for t in techs]
    fuel = [tco_by_technology[t]["fuel_cost_mwh"] for t in techs]
    om = [tco_by_technology[t]["om_cost_mwh"] for t in techs]
    overhead = [tco_by_technology[t]["capex_amortized_mwh"] * tco_by_technology[t]["redundancy_overhead_pct"] / 100 for t in techs]

    x = np.arange(len(techs))
    width = 0.6

    ax.bar(x, capex, width, label='CapEx (amortized)', color='#3498db', alpha=0.9)
    ax.bar(x, fuel, width, bottom=capex, label='Fuel', color='#e74c3c', alpha=0.9)
    ax.bar(x, om, width, bottom=[c+f for c, f in zip(capex, fuel)], label='O&M', color='#2ecc71', alpha=0.9)
    ax.bar(x, overhead, width, bottom=[c+f+o for c, f, o in zip(capex, fuel, om)],
           label='Redundancy Overhead', color='#9b59b6', alpha=0.9)

    # Add total labels
    totals = [tco_by_technology[t]["total_tco_mwh"] for t in techs]
    for i, (total, grid) in enumerate(zip(totals, [tco_by_technology[t]["grid_equivalent_mwh"] for t in techs])):
        ax.text(i, total + 2, f'${total}/MWh', ha='center', fontsize=10, fontweight='bold')

    # Add grid reference line
    ax.axhline(y=60, color='orange', linestyle='--', linewidth=2, label='Grid Power ($60/MWh)')

    ax.set_xlabel('Technology', fontsize=12, fontweight='bold')
    ax.set_ylabel('Total Cost of Ownership ($/MWh)', fontsize=12, fontweight='bold')
    ax.set_title('Onsite Gas TCO by Technology\n(Includes redundancy overhead)',
                fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(techs, rotation=15, ha='right')
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    charts_dir.mkdir(exist_ok=True)
    plt.savefig(charts_dir / "13_tco_by_technology.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 13_tco_by_technology.png")
    plt.close()


def plot_arbitrage_model():
    """Plot 36-month onsite vs grid arbitrage P&L"""
    fig, ax = plt.subplots(figsize=(14, 8))

    params = arbitrage_model
    months = np.arange(1, 37)

    # Calculate monthly revenue and costs
    monthly_revenue = (params["revenue_per_mw_annual"] * params["datacenter_capacity_mw"]) / 12

    # Onsite costs
    onsite_capex_total = params["onsite_capex_per_kw"] * params["datacenter_capacity_mw"] * 1000
    monthly_capex_amortized = onsite_capex_total / (params["amortization_years"] * 12)
    fuel_cost_mwh = (params["heat_rate_btu_kwh"] * params["gas_price_mmbtu"]) / 1000
    onsite_opex_per_mwh = fuel_cost_mwh + params["onsite_om_mwh"]
    onsite_monthly_opex = onsite_opex_per_mwh * params["datacenter_capacity_mw"] * params["hours_per_month"]

    # Grid costs
    grid_monthly_opex = params["grid_power_cost_mwh"] * params["datacenter_capacity_mw"] * params["hours_per_month"]

    # Calculate cumulative profits
    onsite_cum_profit = []
    grid_cum_profit = []
    onsite_running = 0
    grid_running = 0

    for m in months:
        if m >= params["onsite_deployment_month"]:
            onsite_profit = monthly_revenue - onsite_monthly_opex - monthly_capex_amortized
            onsite_running += onsite_profit
        onsite_cum_profit.append(onsite_running)

        if m >= params["grid_deployment_month"]:
            grid_profit = monthly_revenue - grid_monthly_opex
            grid_running += grid_profit
        grid_cum_profit.append(grid_running)

    # Convert to billions
    onsite_cum_profit = [p / 1e9 for p in onsite_cum_profit]
    grid_cum_profit = [p / 1e9 for p in grid_cum_profit]

    ax.fill_between(months, 0, onsite_cum_profit, alpha=0.3, color='#27ae60', label='Onsite Gas (BYOG)')
    ax.fill_between(months, 0, grid_cum_profit, alpha=0.3, color='#3498db', label='Grid Power')
    ax.plot(months, onsite_cum_profit, linewidth=3, color='#27ae60', marker='o', markersize=4)
    ax.plot(months, grid_cum_profit, linewidth=3, color='#3498db', marker='s', markersize=4)

    # Add annotations
    final_onsite = onsite_cum_profit[-1]
    final_grid = grid_cum_profit[-1]
    arbitrage = final_onsite - final_grid

    ax.annotate(f'Onsite: ${final_onsite:.2f}B',
               xy=(36, final_onsite), xytext=(30, final_onsite + 0.5),
               fontsize=11, fontweight='bold', color='#27ae60',
               arrowprops=dict(arrowstyle='->', color='#27ae60'))

    ax.annotate(f'Grid: ${final_grid:.2f}B\n(Starts Month 36)',
               xy=(36, final_grid), xytext=(25, final_grid + 0.3),
               fontsize=11, fontweight='bold', color='#3498db',
               arrowprops=dict(arrowstyle='->', color='#3498db'))

    # Add arbitrage callout
    ax.text(20, 4.5, f'36-Month Arbitrage:\n${arbitrage:.2f}B\n(Speed Premium)',
           fontsize=14, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9, edgecolor='gold', linewidth=2))

    ax.set_xlabel('Month', fontsize=12, fontweight='bold')
    ax.set_ylabel('Cumulative Profit ($ Billions)', fontsize=12, fontweight='bold')
    ax.set_title(f'The Speed Premium: Onsite vs Grid P&L ({params["datacenter_capacity_mw"]}MW Datacenter)\n'
                f'Revenue: ${params["revenue_per_mw_annual"]/1e6:.0f}M/MW/year | Onsite: Month {params["onsite_deployment_month"]} | Grid: Month {params["grid_deployment_month"]}',
                fontsize=13, fontweight='bold', pad=20)
    ax.legend(loc='upper left', fontsize=11)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlim(0, 37)
    ax.set_ylim(0, 6)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "14_onsite_vs_grid_arbitrage.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 14_onsite_vs_grid_arbitrage.png")
    plt.close()


def plot_redundancy_costs():
    """Plot redundancy overbuild factors"""
    fig, ax = plt.subplots(figsize=(12, 8))

    configs = list(redundancy_configs.keys())
    ratios = [redundancy_configs[c]["overbuild_ratio"] for c in configs]
    techs = [redundancy_configs[c]["tech"] for c in configs]

    colors = {'Aeroderivative': '#3498db', 'RICE': '#e74c3c', 'CCGT': '#2ecc71'}
    bar_colors = [colors[t] for t in techs]

    bars = ax.barh(configs, ratios, color=bar_colors, alpha=0.9, edgecolor='black', linewidth=1.5)

    for bar, ratio in zip(bars, ratios):
        width = bar.get_width()
        ax.text(width + 0.02, bar.get_y() + bar.get_height()/2.,
               f'{ratio:.2f}x', ha='left', va='center', fontsize=11, fontweight='bold')

    ax.axvline(x=1.0, color='gray', linestyle='--', linewidth=2, label='No Overbuild (1.0x)')

    ax.set_xlabel('Overbuild Ratio (Generation / IT Load)', fontsize=12, fontweight='bold')
    ax.set_title('Redundancy Configurations: Overbuild Factor\n(Higher = More Expensive but Reliable)',
                fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.set_xlim(0.9, 1.8)

    # Add legend for tech colors
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor=colors[t], label=t) for t in colors]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=10)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "15_redundancy_costs.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 15_redundancy_costs.png")
    plt.close()


def plot_fuel_sensitivity():
    """Plot TCO sensitivity to natural gas prices"""
    fig, ax = plt.subplots(figsize=(14, 8))

    gas_prices = fuel_sensitivity["gas_prices_mmbtu"]
    grid_price = fuel_sensitivity["grid_breakeven_mwh"]

    # Calculate TCO at each gas price for aeroderivative (heat rate 9500)
    heat_rate = 9500
    base_capex_om = 25 + 8  # CapEx + O&M without fuel

    tco_at_price = []
    for price in gas_prices:
        fuel_cost = (heat_rate * price) / 1000
        total = base_capex_om + fuel_cost + (base_capex_om * 0.15)  # 15% redundancy overhead
        tco_at_price.append(total)

    ax.plot(gas_prices, tco_at_price, marker='o', linewidth=3, markersize=10,
           color='#e74c3c', label='Onsite Gas (Aeroderivative)')
    ax.axhline(y=grid_price, color='#3498db', linestyle='--', linewidth=2, label=f'Grid Power (${grid_price}/MWh)')

    # Fill regions
    ax.fill_between(gas_prices, tco_at_price, grid_price,
                   where=[t < grid_price for t in tco_at_price],
                   alpha=0.3, color='green', label='Onsite Cheaper')
    ax.fill_between(gas_prices, tco_at_price, grid_price,
                   where=[t >= grid_price for t in tco_at_price],
                   alpha=0.3, color='red', label='Grid Cheaper')

    # Find breakeven
    breakeven = None
    for i, (price, tco) in enumerate(zip(gas_prices, tco_at_price)):
        if tco >= grid_price and i > 0:
            # Linear interpolation
            prev_price = gas_prices[i-1]
            prev_tco = tco_at_price[i-1]
            breakeven = prev_price + (grid_price - prev_tco) * (price - prev_price) / (tco - prev_tco)
            break

    if breakeven:
        ax.axvline(x=breakeven, color='orange', linestyle=':', linewidth=2)
        ax.text(breakeven + 0.2, 85, f'Breakeven:\n${breakeven:.2f}/MMBtu',
               fontsize=11, fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    ax.set_xlabel('Natural Gas Price ($/MMBtu)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Total Cost of Ownership ($/MWh)', fontsize=12, fontweight='bold')
    ax.set_title('Fuel Price Sensitivity: When Does Onsite Gas Lose to Grid?\n(Aeroderivative @ 9,500 BTU/kWh heat rate)',
                fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlim(1.5, 11)
    ax.set_ylim(40, 130)

    # Add current price marker
    current_price = 3.0
    current_tco = base_capex_om + (heat_rate * current_price) / 1000 + (base_capex_om * 0.15)
    ax.scatter([current_price], [current_tco], s=200, c='gold', edgecolors='black', linewidth=2, zorder=5)
    ax.annotate(f'Current: ${current_price}/MMBtu\n${current_tco:.0f}/MWh',
               xy=(current_price, current_tco), xytext=(current_price + 1, current_tco + 10),
               fontsize=10, fontweight='bold',
               arrowprops=dict(arrowstyle='->', color='gold', lw=2))

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "16_fuel_sensitivity.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 16_fuel_sensitivity.png")
    plt.close()


if __name__ == "__main__":
    print("Generating TCO analysis...")
    save_data()
    plot_tco_by_technology()
    plot_arbitrage_model()
    plot_redundancy_costs()
    plot_fuel_sensitivity()
    print("\nTCO analysis complete!")
