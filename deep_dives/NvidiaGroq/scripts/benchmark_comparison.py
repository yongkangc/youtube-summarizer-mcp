#!/usr/bin/env python3
"""
Compile and analyze benchmark data for inference hardware comparison.
"""

import json
import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class ChipSpec:
    name: str
    memory_type: str
    capacity_gb: float
    bandwidth_tb_s: float
    power_w: int
    process_node: str
    price_usd: Optional[tuple] = None


@dataclass
class InferenceBenchmark:
    hardware: str
    model: str
    tokens_per_sec: float
    ttft_ms: Optional[float] = None
    mode: str = "standard"


def get_chip_specs():
    """Return specifications for key chips."""
    return [
        ChipSpec("Nvidia H100 SXM", "HBM3", 80, 3.35, 700, "TSMC 4N", (27000, 40000)),
        ChipSpec("Nvidia H200", "HBM3e", 141, 4.8, 700, "TSMC 4N", (31000, 31000)),
        ChipSpec("Nvidia B200", "HBM3e", 192, 8.0, 1000, "TSMC 4N", None),
        ChipSpec("Nvidia Rubin Ultra", "HBM4e", 1024, 32.0, 3600, "TBD", None),
        ChipSpec("Groq LPU", "SRAM", 0.23, 80.0, 300, "GF 14nm", None),
        ChipSpec("Cerebras WSE-3", "SRAM", 44, 21000.0, 25000, "TSMC 5nm", None),
        ChipSpec("AMD MI300X", "HBM3", 192, 5.3, 750, "TSMC 5nm", (10000, 15000)),
        ChipSpec("AMD MI400", "HBM4", 432, 19.6, 800, "TBD", None),
    ]


def get_inference_benchmarks():
    """Return published inference benchmarks."""
    return [
        InferenceBenchmark("Groq 576-LPU", "Llama 3.3 70B", 1660, 250, "speculative"),
        InferenceBenchmark("Groq 576-LPU", "Llama 3 70B", 290, 250, "standard"),
        InferenceBenchmark("Cerebras WSE-3", "Llama 3.1 70B", 2100, None, "standard"),
        InferenceBenchmark("Cerebras WSE-3", "Llama 4 Maverick", 2500, None, "standard"),
        InferenceBenchmark("8x Nvidia H100", "Llama 2 70B", 24323, 50, "batch"),
        InferenceBenchmark("8x AMD MI300X", "Llama 2 70B", 23512, None, "batch"),
    ]


def calculate_bandwidth_ratios():
    """Calculate bandwidth advantage ratios."""
    specs = get_chip_specs()
    h100_bw = next(s.bandwidth_tb_s for s in specs if s.name == "Nvidia H100 SXM")

    ratios = {}
    for spec in specs:
        if spec.name != "Nvidia H100 SXM":
            ratios[spec.name] = spec.bandwidth_tb_s / h100_bw

    return ratios


def calculate_capacity_tradeoffs():
    """Calculate capacity tradeoffs for running 70B model."""
    # Llama 3 70B requires ~140GB for INT8 weights
    model_size_gb = 140

    results = {}
    specs = get_chip_specs()

    for spec in specs:
        chips_needed = model_size_gb / spec.capacity_gb
        results[spec.name] = {
            "chips_for_70b": max(1, int(chips_needed) + (1 if chips_needed % 1 > 0 else 0)),
            "capacity_gb": spec.capacity_gb,
            "model_fits_single_chip": chips_needed <= 1
        }

    return results


def main():
    """Generate benchmark analysis summary."""
    print("\n" + "="*60)
    print("Benchmark Comparison Analysis")
    print("="*60 + "\n")

    # Bandwidth ratios
    print("BANDWIDTH RATIOS (vs H100):")
    print("-" * 40)
    ratios = calculate_bandwidth_ratios()
    for chip, ratio in sorted(ratios.items(), key=lambda x: x[1], reverse=True):
        print(f"  {chip}: {ratio:.1f}x")

    print("\n" + "-"*60 + "\n")

    # Capacity tradeoffs
    print("CAPACITY TRADEOFFS (Llama 3 70B @ INT8):")
    print("-" * 40)
    tradeoffs = calculate_capacity_tradeoffs()
    for chip, data in sorted(tradeoffs.items(), key=lambda x: x[1]["chips_for_70b"]):
        status = "single chip" if data["model_fits_single_chip"] else f"{data['chips_for_70b']} chips"
        print(f"  {chip}: {status} ({data['capacity_gb']} GB capacity)")

    print("\n" + "-"*60 + "\n")

    # Performance benchmarks
    print("INFERENCE PERFORMANCE (tokens/sec):")
    print("-" * 40)
    benchmarks = get_inference_benchmarks()
    for b in sorted(benchmarks, key=lambda x: x.tokens_per_sec, reverse=True):
        mode_str = f" ({b.mode})" if b.mode != "standard" else ""
        print(f"  {b.hardware} on {b.model}: {b.tokens_per_sec:,.0f} tok/s{mode_str}")

    # Save to JSON
    data = {
        "chip_specs": [
            {
                "name": s.name,
                "memory_type": s.memory_type,
                "capacity_gb": s.capacity_gb,
                "bandwidth_tb_s": s.bandwidth_tb_s,
                "power_w": s.power_w,
                "process_node": s.process_node,
                "price_usd": list(s.price_usd) if s.price_usd else None
            }
            for s in get_chip_specs()
        ],
        "bandwidth_ratios": ratios,
        "capacity_tradeoffs": tradeoffs,
        "inference_benchmarks": [
            {
                "hardware": b.hardware,
                "model": b.model,
                "tokens_per_sec": b.tokens_per_sec,
                "ttft_ms": b.ttft_ms,
                "mode": b.mode
            }
            for b in benchmarks
        ]
    }

    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    output_file = os.path.join(data_dir, 'benchmark_analysis.json')

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nSaved analysis to: {output_file}")


if __name__ == '__main__':
    main()
