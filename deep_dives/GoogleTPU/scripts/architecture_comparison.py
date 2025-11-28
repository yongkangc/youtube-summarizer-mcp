#!/usr/bin/env python3
"""
AI Accelerator Architecture Comparison
Compares Google TPU vs NVIDIA GPU vs Groq LPU vs Huawei Ascend
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from math import pi

# Comprehensive architecture comparison data
architecture_comparison = {
    "Google TPU v5p": {
        "core_architecture": "Systolic Array (2D)",
        "compute_tflops": 459,
        "compute_tops_int8": 918,
        "memory_gb": 95,
        "memory_type": "HBM3",
        "memory_bandwidth_tbps": 2.76,
        "power_w": 400,
        "interconnect": "ICI 3D Torus + OCS",
        "software_stack": "JAX / XLA / TensorFlow",
        "availability": "Google Cloud only",
        "primary_advantage": "System TCO & Scaling",
        "year": 2023
    },
    "NVIDIA H100 SXM": {
        "core_architecture": "SIMT + Tensor Cores",
        "compute_tflops": 1979,  # With sparsity
        "compute_tops_int8": 3958,
        "memory_gb": 80,
        "memory_type": "HBM3",
        "memory_bandwidth_tbps": 3.35,
        "power_w": 700,
        "interconnect": "NVLink + InfiniBand",
        "software_stack": "CUDA / PyTorch / TensorFlow",
        "availability": "Multi-cloud + On-premises",
        "primary_advantage": "Peak Performance & Ecosystem",
        "year": 2022
    },
    "Groq LPU": {
        "core_architecture": "VLIW / Deterministic",
        "compute_tflops": 188,  # FP16
        "compute_tops_int8": 750,
        "memory_gb": 0.230,  # 230 MB SRAM
        "memory_type": "SRAM (on-chip)",
        "memory_bandwidth_tbps": 80,  # On-die bandwidth
        "power_w": 300,
        "interconnect": "TSP Chip-to-Chip",
        "software_stack": "Groq Compiler",
        "availability": "GroqCloud",
        "primary_advantage": "Ultra-Low Latency Inference",
        "year": 2024
    },
    "Huawei Ascend 910B": {
        "core_architecture": "Da Vinci 3D Cube",
        "compute_tflops": 320,
        "compute_tops_int8": 640,
        "memory_gb": 64,
        "memory_type": "HBM2e",
        "memory_bandwidth_tbps": 1.2,
        "power_w": 400,
        "interconnect": "HCCS + RoCE v2",
        "software_stack": "MindSpore / CANN",
        "availability": "China / Huawei ecosystem",
        "primary_advantage": "Sovereign Supply (China)",
        "year": 2023
    }
}

# Detailed Groq LPU data
groq_data = {
    "tokens_per_second_llama2_70b": 250,
    "tokens_per_second_llama2_7b": 500,
    "latency_first_token_ms": 100,
    "sram_total_mb": 230,
    "on_chip_bandwidth_tbps": 80,
    "chips_needed_70b_model": 576,  # ~600 chips for 140GB model
    "founder": "Jonathan Ross (ex-Google TPU architect)",
    "founded": 2016
}

# Huawei Ascend detailed data
huawei_data = {
    "910b_tflops_fp16": 320,
    "910c_tflops_fp16": 400,  # Estimated
    "process_node_910b": "7nm SMIC",
    "process_node_910c": "7nm N+2",
    "relative_to_h100": 0.60,  # ~60% performance claim
    "interconnect_issues": True,
    "sanctions_impact": "Limited to SMIC manufacturing"
}

def save_data():
    """Save comparison data to JSON"""
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    with open(data_dir / "architecture_comparison.json", "w") as f:
        json.dump(architecture_comparison, f, indent=2)

    with open(data_dir / "groq_data.json", "w") as f:
        json.dump(groq_data, f, indent=2)

    with open(data_dir / "huawei_data.json", "w") as f:
        json.dump(huawei_data, f, indent=2)

    print(f"Saved architecture comparison data to {data_dir}")

def plot_radar_comparison():
    """Create radar chart comparing architectures across multiple dimensions"""
    fig, ax = plt.subplots(figsize=(12, 10), subplot_kw=dict(polar=True))

    # Define categories (normalized to 0-10 scale)
    categories = ['Compute\n(TFLOPS)', 'Memory\nCapacity', 'Bandwidth',
                  'Power\nEfficiency', 'Ecosystem\nMaturity', 'Availability']
    N = len(categories)

    # Normalize scores (subjective 0-10 scale based on data)
    scores = {
        "Google TPU v5p": [5, 10, 7, 8, 6, 4],  # High memory, good efficiency, GCP-only
        "NVIDIA H100": [10, 8, 9, 5, 10, 10],   # Best raw perf, CUDA ecosystem, available everywhere
        "Groq LPU": [2, 1, 10, 9, 3, 3],        # Massive bandwidth, low memory, new
        "Huawei Ascend 910B": [4, 7, 3, 6, 4, 2] # China-only, interconnect issues
    }

    # Compute angles
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]  # Complete the loop

    # Colors
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']

    for i, (name, score) in enumerate(scores.items()):
        values = score + score[:1]  # Complete the loop
        ax.plot(angles, values, 'o-', linewidth=2, label=name, color=colors[i])
        ax.fill(angles, values, alpha=0.15, color=colors[i])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=11)
    ax.set_ylim(0, 10)
    ax.set_title('AI Accelerator Architecture Comparison\n(Normalized 0-10 Scale)',
                fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0), fontsize=10)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    charts_dir.mkdir(exist_ok=True)
    plt.savefig(charts_dir / "05_architecture_radar.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 05_architecture_radar.png")
    plt.close()

def plot_performance_per_watt():
    """Bar chart comparing performance per watt"""
    fig, ax = plt.subplots(figsize=(12, 7))

    chips = list(architecture_comparison.keys())
    tflops = [architecture_comparison[c]["compute_tflops"] for c in chips]
    power = [architecture_comparison[c]["power_w"] for c in chips]
    perf_per_watt = [t / p for t, p in zip(tflops, power)]

    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
    bars = ax.bar(chips, perf_per_watt, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)

    for bar, val, tfl, pw in zip(bars, perf_per_watt, tflops, power):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{val:.2f}\n({tfl} TFLOPS / {pw}W)',
               ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax.set_ylabel('TFLOPS per Watt', fontsize=12, fontweight='bold')
    ax.set_xlabel('AI Accelerator', fontsize=12, fontweight='bold')
    ax.set_title('AI Accelerator Power Efficiency Comparison\n(Higher = More Efficient)',
                fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    plt.xticks(rotation=15)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "06_performance_per_watt.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 06_performance_per_watt.png")
    plt.close()

def plot_memory_architecture():
    """Compare memory architectures"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    chips = list(architecture_comparison.keys())
    memory_gb = [architecture_comparison[c]["memory_gb"] for c in chips]
    bandwidth = [architecture_comparison[c]["memory_bandwidth_tbps"] for c in chips]

    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']

    # Memory capacity (log scale for Groq)
    bars1 = ax1.bar(chips, memory_gb, color=colors, alpha=0.8, edgecolor='black')
    ax1.set_yscale('log')

    for bar, val, chip in zip(bars1, memory_gb, chips):
        height = bar.get_height()
        label = f'{val}GB' if val >= 1 else f'{val*1000:.0f}MB'
        mem_type = architecture_comparison[chip]["memory_type"]
        ax1.text(bar.get_x() + bar.get_width()/2., height * 1.1,
               f'{label}\n({mem_type})',
               ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax1.set_ylabel('Memory Capacity (GB, log scale)', fontsize=12, fontweight='bold')
    ax1.set_xlabel('AI Accelerator', fontsize=12, fontweight='bold')
    ax1.set_title('Memory Capacity Comparison', fontsize=13, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3, linestyle='--')
    plt.sca(ax1)
    plt.xticks(rotation=15)

    # Memory bandwidth
    bars2 = ax2.bar(chips, bandwidth, color=colors, alpha=0.8, edgecolor='black')

    for bar, val in zip(bars2, bandwidth):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
               f'{val} TB/s',
               ha='center', va='bottom', fontsize=10, fontweight='bold')

    ax2.set_ylabel('Memory Bandwidth (TB/s)', fontsize=12, fontweight='bold')
    ax2.set_xlabel('AI Accelerator', fontsize=12, fontweight='bold')
    ax2.set_title('Memory Bandwidth Comparison\n(Groq: 80 TB/s on-chip SRAM)',
                 fontsize=13, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3, linestyle='--')
    plt.sca(ax2)
    plt.xticks(rotation=15)

    # Highlight Groq's exceptional bandwidth
    bars2[2].set_edgecolor('gold')
    bars2[2].set_linewidth(3)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "07_memory_architecture.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 07_memory_architecture.png")
    plt.close()

def plot_inference_latency():
    """Compare inference latency/throughput for LLMs"""
    fig, ax = plt.subplots(figsize=(12, 7))

    # Estimated tokens per second for Llama 2 70B (batch size 1)
    chips = ["Google TPU v5p", "NVIDIA H100", "Groq LPU", "Huawei Ascend 910B"]
    tokens_per_sec = [40, 35, 250, 25]  # Groq is ~7x faster than H100

    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
    bars = ax.barh(chips, tokens_per_sec, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)

    for bar, val in zip(bars, tokens_per_sec):
        width = bar.get_width()
        ax.text(width + 5, bar.get_y() + bar.get_height()/2.,
               f'{val} tok/s',
               ha='left', va='center', fontsize=11, fontweight='bold')

    ax.set_xlabel('Tokens per Second (Llama 2 70B, Batch=1)', fontsize=12, fontweight='bold')
    ax.set_title('LLM Inference Speed Comparison\n(Lower Latency = Faster Response)',
                fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.set_xlim(0, 300)

    # Add note about Groq
    ax.annotate('Groq: ~7x faster\n(SRAM-only, deterministic)',
               xy=(250, 2), xytext=(180, 3.2),
               fontsize=9, fontweight='bold',
               arrowprops=dict(arrowstyle='->', color='green'),
               bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "08_inference_latency.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 08_inference_latency.png")
    plt.close()

def create_comparison_table():
    """Create a visual comparison table"""
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.axis('off')

    # Table data
    columns = ['Metric', 'Google TPU v5p', 'NVIDIA H100', 'Groq LPU', 'Huawei 910B']
    rows = [
        ['Architecture', 'Systolic Array', 'SIMT + Tensor', 'VLIW Deterministic', 'Da Vinci 3D Cube'],
        ['Compute (TFLOPS)', '459', '1,979', '188', '320'],
        ['Memory', '95 GB HBM3', '80 GB HBM3', '230 MB SRAM', '64 GB HBM2e'],
        ['Bandwidth', '2.76 TB/s', '3.35 TB/s', '80 TB/s', '1.2 TB/s'],
        ['Power', '400W', '700W', '300W', '400W'],
        ['TFLOPS/W', '1.15', '2.83', '0.63', '0.80'],
        ['Interconnect', 'ICI 3D Torus', 'NVLink', 'TSP', 'HCCS'],
        ['Software', 'JAX/XLA', 'CUDA', 'Groq Compiler', 'MindSpore'],
        ['Availability', 'GCP only', 'Everywhere', 'GroqCloud', 'China only'],
        ['Best For', 'Large-scale TCO', 'Flexibility', 'Low-latency', 'Sovereignty']
    ]

    # Create table
    table = ax.table(cellText=rows, colLabels=columns, loc='center', cellLoc='center')

    # Style table
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 2)

    # Color header
    for j in range(len(columns)):
        table[(0, j)].set_facecolor('#2c3e50')
        table[(0, j)].set_text_props(color='white', fontweight='bold')

    # Color columns by chip
    chip_colors = ['#ecf0f1', '#d5e8f7', '#fde8e8', '#e8f5e8', '#fff5e6']
    for i in range(1, len(rows) + 1):
        for j in range(len(columns)):
            table[(i, j)].set_facecolor(chip_colors[j])

    ax.set_title('AI Accelerator Architecture Comparison Matrix',
                fontsize=16, fontweight='bold', pad=20)

    plt.tight_layout()
    charts_dir = Path(__file__).parent.parent / "charts"
    plt.savefig(charts_dir / "09_comparison_matrix.png", dpi=300, bbox_inches='tight')
    print("Saved chart: 09_comparison_matrix.png")
    plt.close()

if __name__ == "__main__":
    print("Generating architecture comparison analysis...")
    save_data()
    plot_radar_comparison()
    plot_performance_per_watt()
    plot_memory_architecture()
    plot_inference_latency()
    create_comparison_table()
    print("\nArchitecture comparison analysis complete!")
