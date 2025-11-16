#!/usr/bin/env python3
"""
HBM Technology Roadmap Analysis
Generates roadmap visualizations for HBM3, HBM3E, and HBM4 across suppliers
"""

import json
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
from datetime import datetime

# Technology specs by generation
tech_specs = {
    "HBM3": {
        "bandwidth_per_stack": 819,  # GB/s
        "pin_speed": 6.4,  # Gbps
        "interface_width": 1024,  # bits
        "max_capacity_8hi": 24,  # GB
        "power_per_gb": 1.0,  # Relative baseline
        "released": "2022-Q1"
    },
    "HBM3E": {
        "bandwidth_per_stack": 1229,  # GB/s (9.6 Gbps)
        "pin_speed": 9.6,  # Gbps
        "interface_width": 1024,  # bits
        "max_capacity_8hi": 24,  # GB
        "max_capacity_12hi": 36,  # GB
        "power_per_gb": 0.7,  # 30% reduction (Micron claim)
        "released": "2024-Q1"
    },
    "HBM4": {
        "bandwidth_per_stack": 2048,  # GB/s (estimated 8 Gbps × 2048 bits)
        "pin_speed": 8.0,  # Gbps (conservative estimate)
        "interface_width": 2048,  # bits (doubled)
        "max_capacity_12hi": 48,  # GB (32Gb dies)
        "max_capacity_16hi": 64,  # GB
        "power_per_gb": 0.5,  # Estimated 50% of HBM3
        "released": "2026-Q1"
    }
}

# Supplier roadmap timeline
roadmap = {
    "SK hynix": {
        "HBM3": {"start": "2022-Q2", "mass_prod": "2022-Q4", "yield": 75},
        "HBM3E": {"start": "2024-Q1", "mass_prod": "2024-Q3", "yield": 80},
        "HBM4": {"samples": "2025-Q1", "mass_prod": "2026-Q3", "yield": 70}
    },
    "Samsung": {
        "HBM3": {"start": "2023-Q3", "mass_prod": "2023-Q4", "yield": 55},
        "HBM3E": {"start": "2024-Q2", "mass_prod": "2024-Q4", "yield": 50},
        "HBM4": {"samples": "2025-Q2", "mass_prod": "2025-Q4", "yield": 60}
    },
    "Micron": {
        "HBM3": {"start": None, "mass_prod": None, "yield": None},  # Skipped
        "HBM3E": {"start": "2024-Q1", "mass_prod": "2024-Q2", "yield": 70},
        "HBM4": {"samples": "2025-Q1", "mass_prod": "2026-Q1", "yield": 65}
    }
}

def save_data():
    """Save technology data to JSON"""
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    with open(data_dir / "tech_specs.json", "w") as f:
        json.dump(tech_specs, f, indent=2)

    with open(data_dir / "roadmap.json", "w") as f:
        json.dump(roadmap, f, indent=2)

    print(f"✓ Saved technology data to {data_dir}")

def plot_bandwidth_evolution():
    """Plot bandwidth improvements across generations"""
    generations = list(tech_specs.keys())
    bandwidths = [tech_specs[g]["bandwidth_per_stack"] for g in generations]

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(generations, bandwidths, color=['#3498db', '#e74c3c', '#2ecc71'],
                  alpha=0.8, edgecolor='black', linewidth=1.5)

    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{height:.0f} GB/s',
               ha='center', va='bottom', fontsize=12, fontweight='bold')

    # Add improvement percentages
    for i in range(1, len(bandwidths)):
        improvement = ((bandwidths[i] / bandwidths[i-1]) - 1) * 100
        x_pos = i
        y_pos = (bandwidths[i-1] + bandwidths[i]) / 2
        ax.annotate(f'+{improvement:.0f}%',
                   xy=(x_pos - 0.5, y_pos),
                   fontsize=11, fontweight='bold', color='green',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))

    ax.set_ylabel('Bandwidth per Stack (GB/s)', fontsize=12, fontweight='bold')
    ax.set_title('HBM Bandwidth Evolution by Generation',
                fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_ylim(0, max(bandwidths) * 1.2)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    charts_dir.mkdir(exist_ok=True)
    plt.savefig(charts_dir / "hbm_bandwidth_evolution.png", dpi=300, bbox_inches='tight')
    print(f"✓ Saved chart: hbm_bandwidth_evolution.png")
    plt.close()

def plot_supplier_timeline():
    """Create Gantt-style timeline for supplier roadmaps"""
    fig, ax = plt.subplots(figsize=(14, 8))

    suppliers = ["SK hynix", "Samsung", "Micron"]
    generations = ["HBM3", "HBM3E", "HBM4"]
    colors = {'HBM3': '#3498db', 'HBM3E': '#e74c3c', 'HBM4': '#2ecc71'}

    def quarter_to_num(q_str):
        """Convert 'YYYY-QN' to numeric value for plotting"""
        if not q_str:
            return None
        year, quarter = q_str.split('-Q')
        return int(year) + (int(quarter) - 1) * 0.25

    base_date = 2022.0
    y_positions = {supplier: i * 3 for i, supplier in enumerate(suppliers)}

    for supplier_idx, supplier in enumerate(suppliers):
        for gen_idx, gen in enumerate(generations):
            if roadmap[supplier][gen]["mass_prod"] is None:
                continue  # Skip (Micron HBM3)

            start = quarter_to_num(roadmap[supplier][gen].get("start"))
            mass = quarter_to_num(roadmap[supplier][gen]["mass_prod"])

            if start and mass:
                y_base = y_positions[supplier] + gen_idx * 0.8
                duration = mass - start

                # Development phase (lighter)
                ax.barh(y_base, duration, left=start - base_date, height=0.6,
                       color=colors[gen], alpha=0.4, edgecolor='black', linewidth=0.5)

                # Mass production phase (darker)
                ax.barh(y_base, 1.5, left=mass - base_date, height=0.6,
                       color=colors[gen], alpha=0.9, edgecolor='black', linewidth=1)

                # Add yield label
                yield_val = roadmap[supplier][gen]["yield"]
                if yield_val:
                    ax.text(mass - base_date + 0.75, y_base,
                           f'{yield_val}%',
                           ha='center', va='center', fontsize=8,
                           fontweight='bold', color='white',
                           bbox=dict(boxstyle='round,pad=0.2', facecolor='black', alpha=0.7))

    # Set y-axis
    y_ticks = [y_positions[s] + 0.8 for s in suppliers]
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(suppliers, fontsize=11, fontweight='bold')

    # Set x-axis
    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_xlim(0, 5.5)
    ax.set_xticks(range(0, 6))
    ax.set_xticklabels([2022, 2023, 2024, 2025, 2026, 2027])

    ax.set_title('HBM Technology Roadmap by Supplier (2022-2027)',
                fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3, linestyle='--')

    # Legend
    legend_elements = [mpatches.Patch(facecolor=colors[g], alpha=0.7, label=g)
                      for g in generations]
    legend_elements.append(mpatches.Patch(facecolor='gray', alpha=0.4, label='Development'))
    legend_elements.append(mpatches.Patch(facecolor='gray', alpha=0.9, label='Mass Production'))
    ax.legend(handles=legend_elements, loc='upper left', fontsize=9)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "hbm_supplier_roadmap.png", dpi=300, bbox_inches='tight')
    print(f"✓ Saved chart: hbm_supplier_roadmap.png")
    plt.close()

def plot_power_efficiency():
    """Plot power efficiency improvements"""
    generations = list(tech_specs.keys())
    power_per_gb = [tech_specs[g]["power_per_gb"] for g in generations]

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.bar(generations, power_per_gb, color=['#95a5a6', '#3498db', '#27ae60'],
                  alpha=0.8, edgecolor='black', linewidth=1.5)

    # Add value labels
    for bar, val in zip(bars, power_per_gb):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{val:.1f}x',
               ha='center', va='bottom', fontsize=12, fontweight='bold')

    # Add improvement arrows
    for i in range(1, len(power_per_gb)):
        improvement = (1 - power_per_gb[i] / power_per_gb[i-1]) * 100
        ax.annotate(f'-{improvement:.0f}%',
                   xy=(i - 0.5, max(power_per_gb[i-1], power_per_gb[i]) * 0.8),
                   fontsize=11, fontweight='bold', color='green',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.7))

    ax.set_ylabel('Relative Power per GB (HBM3 = 1.0x)', fontsize=12, fontweight='bold')
    ax.set_title('HBM Power Efficiency Evolution\n(Lower is Better)',
                fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_ylim(0, 1.3)
    ax.axhline(y=1.0, color='red', linestyle='--', alpha=0.5, label='HBM3 Baseline')
    ax.legend()

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "hbm_power_efficiency.png", dpi=300, bbox_inches='tight')
    print(f"✓ Saved chart: hbm_power_efficiency.png")
    plt.close()

if __name__ == "__main__":
    print("Generating HBM technology roadmap analysis...")
    save_data()
    plot_bandwidth_evolution()
    plot_supplier_timeline()
    plot_power_efficiency()
    print("\n✓ Technology roadmap analysis complete!")
