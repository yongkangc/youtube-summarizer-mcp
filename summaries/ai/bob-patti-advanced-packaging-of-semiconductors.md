# Bob Patti: Advanced Packaging of Semiconductors

Source: https://www.youtube.com/watch?v=3qX2Zd0l8TI

## TL;DR

Bob Patti argues advanced packaging / 3D integration is the post-Moore’s-law path to better semiconductor cost, performance, power, and system customization. Core claim: transistors are no longer main bottleneck; wires are. Shorten wires, stack heterogeneous dies, and move from monolithic chips to chiplet systems.

## Key Insights

- Root bottleneck = wire, not transistor. Patti says transistors are effectively fast and low-power relative to interconnect. Modern chips lose time and power moving signals across wires.
- Moore’s Law economics are ending. Old node shrinks delivered lower cost per transistor. That cost curve no longer works cleanly, so industry needs another route to give consumers more value without $10,000 phones.
- Advanced packaging wins by shortening interconnect. Vertical integration can replace millimeter-scale horizontal routes with micron-scale vertical links. He gives example stacks around ~100–120 microns total height, layers around ~12 microns, TSVs around ~1.6 microns.
- Wire delay is square-law painful. Halving wire length makes delay ~4x better and power roughly half; cutting wire by order of magnitude gives order-of-magnitude power improvement.
- Chiplets are already mainstream. Intel Ponte Vecchio has ~47 chiplets; AMD uses chiplets; cameras/sensors already use 3D integration. This is not lab curiosity.
- 3D integration enables heterogeneous materials. Silicon can be combined with indium phosphide, gallium antimonide, image sensors, photonics, MEMS, chemical sensors, quantum devices, etc. Materials that cannot be fabricated together can be built separately then bonded.
- Photonic compute is one killer use case. Lens/matrix-multiply operations can be much more power-efficient for AI-like workloads, but need packaging to combine photonics with CMOS control/readout.
- Silicon/glass “circuit boards” become new substrate layer. Instead of old PCB-style board assembly, enhanced semiconductor builds high-density silicon/fused-silica interposers / circuit boards with fine TSVs and redistribution.
- Customization beats one-size-fits-all SoCs. Monolithic SoC world forces everyone to buy same giant chip and use maybe 10% of capability. Chiplet world lets vendors assemble many variants, potentially cutting intrinsic material cost while adding targeted functionality.
- Clock-domain/span control improves. 3D lets designers bring more transistors into same clock domain, reducing retiming burden and clock power. Patti notes current processors already retime frequently across die distance.
- Power delivery can be harder than cooling. He mentions future stacked systems around 30mm x 30mm, multiple layers, and thousands of watts; at one volt, 7,000W implies 7,000A, making delivery huge problem.
- Quantum compute needs advanced packaging. His claim is absolute: important quantum computers will not exist without advanced packaging because qubits/control/readout need dense, low-parasitic integration.
- Security/reverse-engineering improves but not perfectly. 3D stacks are harder to delayer, inspect, or tamper with; x-ray tomography exists but resolution limits and destructive layers can make reverse engineering much harder.
- Workforce is bottleneck. Advanced packaging is more “schmorgasbord” engineering than standardized foundry work. It needs mechanical, electrical, materials, process, and physics intuition; he says physics is especially useful because it teaches deduction from incomplete evidence.
- Business angle: US advanced-packaging capacity is scarce. Enhanced Semiconductors has a North Carolina fab and is building larger capacity in Indiana, targeting lots of local university/trade-school hiring.

## Notable Quotes

- “The root of all evil is wire.”
- “We’re effectively at the end of Moore’s Law” — in cost-per-transistor economics, not transistor invention.
- “Advanced packaging is a schmorgasbord.”
- “Quantum compute is fundamentally enabled by advanced packaging… period, end of sentence.”

## Investor / Operator Read-Through

- Structural edge claim: value shifts from transistor scaling alone to interconnect density, heterogeneous integration, packaging yield, thermal/power delivery, and chiplet ecosystem design.
- Bottleneck underwriting: look for companies controlling high-density bonding, interposers/substrates, TSV processes, advanced inspection/metrology, thermal, power delivery, and design tools.
- Risk: packaging is not one standard recipe. More SKU diversity and heterogeneous materials mean yield, tooling, reliability, and workforce are real constraints.
- AI infra implication: as accelerator scaling gets wire/power-bound, advanced packaging becomes core infrastructure, not back-end commodity assembly.

## One-Line Summary

Advanced packaging is Patti’s answer to post-Moore’s-law economics: kill wire length, stack heterogeneous chiplets, and make system-level performance/cost gains where transistor scaling no longer pays alone.
