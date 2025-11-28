#!/usr/bin/env python3
"""
TPU Performance History Analysis
Generates performance evolution data and visualizations for Google TPU v1-v7
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# TPU generations comprehensive specs
tpu_specs = {
    "TPU v1": {
        "year": 2016,
        "compute_tflops": None,  # INT8 only, ~92 TOPS
        "compute_tops_int8": 92,
        "memory_gb": 8,  # DDR3
        "memory_bandwidth_gbps": 34,
        "process_nm": 28,
        "power_w": 40,
        "price_per_hour": None,  # Internal only
        "mxu_size": "256x256",
        "interconnect": None,
        "notes": "First TPU, inference only, deployed in Google datacenters"
    },
    "TPU v2": {
        "year": 2017,
        "compute_tflops": 45,
        "compute_tops_int8": 90,
        "memory_gb": 16,
        "memory_bandwidth_gbps": 600,
        "process_nm": 16,  # Estimated
        "power_w": 200,  # Estimated
        "price_per_hour": None,  # Cloud Alpha
        "mxu_size": "128x128",
        "interconnect": "ICI",
        "notes": "First training TPU, bfloat16 introduced"
    },
    "TPU v3": {
        "year": 2018,
        "compute_tflops": 123,  # Per chip
        "compute_tops_int8": 246,
        "memory_gb": 32,
        "memory_bandwidth_gbps": 900,  # Estimated
        "process_nm": 16,  # Estimated
        "power_w": 200,  # Water-cooled
        "price_per_hour": 8.00,  # Per pod hour / chips
        "mxu_size": "128x128",
        "interconnect": "ICI 2D Torus",
        "notes": "Water-cooled, 100+ PFLOPS per pod"
    },
    "TPU v4": {
        "year": 2021,
        "compute_tflops": 275,
        "compute_tops_int8": 550,
        "memory_gb": 32,
        "memory_bandwidth_gbps": 1228,
        "process_nm": 7,
        "power_w": 175,
        "price_per_hour": 3.22,
        "mxu_size": "128x128",
        "interconnect": "ICI 3D Torus + OCS",
        "notes": "Optical Circuit Switching, 3D mesh interconnect"
    },
    "TPU v5e": {
        "year": 2023,
        "compute_tflops": 197,
        "compute_tops_int8": 393,
        "memory_gb": 16,
        "memory_bandwidth_gbps": 819,
        "process_nm": 5,  # Estimated
        "power_w": 150,  # Estimated
        "price_per_hour": 1.20,
        "mxu_size": "128x128",
        "interconnect": "ICI 2D Torus",
        "notes": "Cost-optimized, 2.7x better Perf/$ than v4"
    },
    "TPU v5p": {
        "year": 2023,
        "compute_tflops": 459,
        "compute_tops_int8": 918,
        "memory_gb": 95,
        "memory_bandwidth_gbps": 2765,
        "process_nm": 5,  # Estimated
        "power_w": 400,  # Estimated
        "price_per_hour": 4.20,
        "mxu_size": "128x128",
        "interconnect": "ICI 3D Torus",
        "notes": "High-performance, 8960 chip pods, Gemini training"
    },
    "TPU v6e (Trillium)": {
        "year": 2024,
        "compute_tflops": 926,
        "compute_tops_int8": 1852,
        "memory_gb": 32,
        "memory_bandwidth_gbps": 1638,  # 2x v5e
        "process_nm": 4,  # Estimated
        "power_w": 200,  # Estimated, 67% more efficient
        "price_per_hour": 2.70,
        "mxu_size": "256x256",
        "interconnect": "ICI 2x bandwidth",
        "notes": "4.7x compute vs v5e, 256x256 MXU, 3rd gen SparseCore"
    },
    "TPU v7 (Ironwood)": {
        "year": 2025,
        "compute_tflops": 4614,
        "compute_tops_int8": 9228,
        "memory_gb": 192,
        "memory_bandwidth_gbps": 5000,  # Estimated 6x Trillium
        "process_nm": 3,  # Estimated
        "power_w": 500,  # Estimated
        "price_per_hour": None,  # Not yet available
        "mxu_size": "256x256",
        "interconnect": "ICI 9216 chip pods",
        "notes": "Age of Inference focus, ultra-large embeddings, MediaTek partnership"
    }
}

# MXU evolution data
mxu_evolution = {
    "TPU v1": {"size": 256, "macs_per_cycle": 65536, "notes": "256x256 INT8"},
    "TPU v2-v5p": {"size": 128, "macs_per_cycle": 16384, "notes": "128x128 bfloat16"},
    "TPU v6-v7": {"size": 256, "macs_per_cycle": 65536, "notes": "256x256 bfloat16, 4x density"}
}

def save_data():
    """Save TPU specs to JSON"""
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    with open(data_dir / "tpu_specs.json", "w") as f:
        json.dump(tpu_specs, f, indent=2)

    with open(data_dir / "mxu_evolution.json", "w") as f:
        json.dump(mxu_evolution, f, indent=2)

    print(f"Saved TPU specs to {data_dir}")

def plot_compute_evolution():
    """Plot TPU compute performance evolution (TFLOPS)"""
    fig, ax = plt.subplots(figsize=(14, 8))

    # Filter TPUs with compute data
    tpus = [(name, spec) for name, spec in tpu_specs.items()
            if spec["compute_tflops"] is not None]

    names = [t[0] for t in tpus]
    years = [t[1]["year"] for t in tpus]
    tflops = [t[1]["compute_tflops"] for t in tpus]

    # Color by category
    colors = []
    for name in names:
        if "v5e" in name or "v6e" in name:
            colors.append('#3498db')  # Cost-optimized (blue)
        elif "v5p" in name or "v7" in name:
            colors.append('#e74c3c')  # High-performance (red)
        else:
            colors.append('#2ecc71')  # Legacy (green)

    bars = ax.bar(names, tflops, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)

    # Add value labels
    for bar, val in zip(bars, tflops):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{val:,.0f}',
               ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Log scale for y-axis
    ax.set_yscale('log')
    ax.set_ylabel('Compute Performance (TFLOPS BF16)', fontsize=12, fontweight='bold')
    ax.set_xlabel('TPU Generation', fontsize=12, fontweight='bold')
    ax.set_title('Google TPU Compute Performance Evolution (2017-2025)\nLogarithmic Scale',
                fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    plt.xticks(rotation=15)

    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#3498db', alpha=0.8, label='Cost-Optimized (v5e, v6e)'),
        Patch(facecolor='#e74c3c', alpha=0.8, label='High-Performance (v5p, v7)'),
        Patch(facecolor='#2ecc71', alpha=0.8, label='Previous Gen (v2-v4)')
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=10)

    # Add year annotations
    for i, (name, year) in enumerate(zip(names, years)):
        ax.text(i, 20, f'({year})', ha='center', fontsize=8, color='gray')

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    charts_dir.mkdir(exist_ok=True)
    plt.savefig(charts_dir / "01_tpu_compute_evolution.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 01_tpu_compute_evolution.png")
    plt.close()

def plot_memory_evolution():
    """Plot TPU memory capacity and bandwidth evolution"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    names = list(tpu_specs.keys())
    memory_gb = [tpu_specs[n]["memory_gb"] for n in names]
    bandwidth = [tpu_specs[n]["memory_bandwidth_gbps"] for n in names]
    years = [tpu_specs[n]["year"] for n in names]

    # Memory capacity
    colors1 = plt.cm.Blues(np.linspace(0.3, 0.9, len(names)))
    bars1 = ax1.bar(names, memory_gb, color=colors1, alpha=0.8, edgecolor='black')

    for bar, val in zip(bars1, memory_gb):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
               f'{val}GB',
               ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax1.set_ylabel('Memory Capacity (GB)', fontsize=12, fontweight='bold')
    ax1.set_xlabel('TPU Generation', fontsize=12, fontweight='bold')
    ax1.set_title('TPU Memory Capacity Evolution', fontsize=13, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3, linestyle='--')
    plt.sca(ax1)
    plt.xticks(rotation=30, ha='right')

    # Memory bandwidth
    colors2 = plt.cm.Oranges(np.linspace(0.3, 0.9, len(names)))
    bars2 = ax2.bar(names, bandwidth, color=colors2, alpha=0.8, edgecolor='black')

    for bar, val in zip(bars2, bandwidth):
        height = bar.get_height()
        if val >= 1000:
            label = f'{val/1000:.1f} TB/s'
        else:
            label = f'{val} GB/s'
        ax2.text(bar.get_x() + bar.get_width()/2., height,
               label,
               ha='center', va='bottom', fontsize=8, fontweight='bold')

    ax2.set_ylabel('Memory Bandwidth (GB/s)', fontsize=12, fontweight='bold')
    ax2.set_xlabel('TPU Generation', fontsize=12, fontweight='bold')
    ax2.set_title('TPU Memory Bandwidth Evolution', fontsize=13, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3, linestyle='--')
    plt.sca(ax2)
    plt.xticks(rotation=30, ha='right')

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "02_tpu_memory_evolution.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 02_tpu_memory_evolution.png")
    plt.close()

def plot_pricing_efficiency():
    """Plot TPU pricing and performance per dollar"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    # Filter TPUs with pricing data
    priced_tpus = [(name, spec) for name, spec in tpu_specs.items()
                   if spec["price_per_hour"] is not None and spec["compute_tflops"] is not None]

    names = [t[0] for t in priced_tpus]
    prices = [t[1]["price_per_hour"] for t in priced_tpus]
    tflops = [t[1]["compute_tflops"] for t in priced_tpus]
    tflops_per_dollar = [t / p for t, p in zip(tflops, prices)]

    # Pricing
    colors = ['#3498db', '#2ecc71', '#e74c3c', '#9b59b6', '#f39c12']
    bars1 = ax1.bar(names, prices, color=colors[:len(names)], alpha=0.8, edgecolor='black')

    for bar, val in zip(bars1, prices):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
               f'${val:.2f}/hr',
               ha='center', va='bottom', fontsize=10, fontweight='bold')

    ax1.set_ylabel('Price per Hour ($)', fontsize=12, fontweight='bold')
    ax1.set_xlabel('TPU Generation', fontsize=12, fontweight='bold')
    ax1.set_title('TPU Cloud Pricing (On-Demand)', fontsize=13, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3, linestyle='--')
    plt.sca(ax1)
    plt.xticks(rotation=15)

    # TFLOPS per dollar
    bars2 = ax2.bar(names, tflops_per_dollar, color=colors[:len(names)], alpha=0.8, edgecolor='black')

    for bar, val in zip(bars2, tflops_per_dollar):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
               f'{val:.0f}',
               ha='center', va='bottom', fontsize=10, fontweight='bold')

    ax2.set_ylabel('TFLOPS per $/hr', fontsize=12, fontweight='bold')
    ax2.set_xlabel('TPU Generation', fontsize=12, fontweight='bold')
    ax2.set_title('TPU Performance per Dollar (Higher = Better Value)',
                 fontsize=13, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3, linestyle='--')
    plt.sca(ax2)
    plt.xticks(rotation=15)

    # Highlight best value
    best_idx = tflops_per_dollar.index(max(tflops_per_dollar))
    bars2[best_idx].set_edgecolor('gold')
    bars2[best_idx].set_linewidth(3)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "03_tpu_pricing_efficiency.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 03_tpu_pricing_efficiency.png")
    plt.close()

def plot_generational_improvement():
    """Plot generational improvement factors"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Calculate improvement ratios between generations
    improvements = {
        "v2 → v3": {
            "Compute": 123 / 45,
            "Memory": 32 / 16,
            "Bandwidth": 900 / 600
        },
        "v3 → v4": {
            "Compute": 275 / 123,
            "Memory": 32 / 32,
            "Bandwidth": 1228 / 900
        },
        "v4 → v5p": {
            "Compute": 459 / 275,
            "Memory": 95 / 32,
            "Bandwidth": 2765 / 1228
        },
        "v5e → v6e": {
            "Compute": 926 / 197,
            "Memory": 32 / 16,
            "Bandwidth": 1638 / 819
        },
        "v6e → v7": {
            "Compute": 4614 / 926,
            "Memory": 192 / 32,
            "Bandwidth": 5000 / 1638
        }
    }

    x = np.arange(len(improvements))
    width = 0.25

    compute = [improvements[g]["Compute"] for g in improvements]
    memory = [improvements[g]["Memory"] for g in improvements]
    bandwidth = [improvements[g]["Bandwidth"] for g in improvements]

    bars1 = ax.bar(x - width, compute, width, label='Compute', color='#e74c3c', alpha=0.8)
    bars2 = ax.bar(x, memory, width, label='Memory Capacity', color='#3498db', alpha=0.8)
    bars3 = ax.bar(x + width, bandwidth, width, label='Bandwidth', color='#2ecc71', alpha=0.8)

    # Add value labels
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}x',
                   ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax.set_ylabel('Improvement Factor (x)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Generation Transition', fontsize=12, fontweight='bold')
    ax.set_title('TPU Generational Improvement Factors',
                fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(improvements.keys(), rotation=15)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.axhline(y=1, color='gray', linestyle='--', alpha=0.5)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "04_tpu_generational_improvement.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 04_tpu_generational_improvement.png")
    plt.close()

if __name__ == "__main__":
    print("Generating TPU performance history analysis...")
    save_data()
    plot_compute_evolution()
    plot_memory_evolution()
    plot_pricing_efficiency()
    plot_generational_improvement()
    print("\nTPU performance history analysis complete!")
