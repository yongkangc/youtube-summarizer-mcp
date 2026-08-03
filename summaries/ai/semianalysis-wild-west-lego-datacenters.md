---
title: "The Wild Wild West of LEGO Datacenters"
source: "https://newsletter.semianalysis.com/p/the-wild-wild-west-of-lego-datacenters"
publication: "SemiAnalysis"
authors:
  - "Nicolas Bontigui"
  - "Eric (Junqi) Wen"
  - "Jeremie Eliahou Ontiveros"
  - "Nigel Chiang"
  - "Reyk Knuhtsen"
  - "Dylan Patel"
published: "2026-07-29T22:09:56Z"
modified: "2026-07-29T22:09:56Z"
access: "Paid article; full article body and 72 embedded images were accessible during review"
tags:
  - ai-infrastructure
  - datacenters
  - modular-construction
  - power
  - cooling
  - labor
  - industrials
---

# The Wild Wild West of LEGO Datacenters

Source: [SemiAnalysis](https://newsletter.semianalysis.com/p/the-wild-wild-west-of-lego-datacenters)

## Source and evidence note

This archive uses the complete approximately 68,000-character article body, its taxonomy, vendor examples, and important embedded charts. The authors' model figures are estimates, not independently audited capacity, schedule, cost, or revenue results. Specific vendor performance figures remain vendor or SemiAnalysis claims unless backed by a commissioned-project dataset.

## One-sentence thesis

AI datacenter builders are moving repeatable electrical, cooling, white-space, and shell work from scarce on-site construction labor into parallel factory production; this can shorten a full 50 MW build by about eight months, but the industry calls many incompatible products "modular," and factory assembly does not remove power, logistics, site integration, or commissioning bottlenecks.

## Theory of edge

The structural edge is **time-to-compute under scarce skilled labor**.

- Electricians represent roughly `30–40%` of datacenter construction man-hours.
- Abilene reportedly needed more than `9,000` workers at peak; Crusoe raised wages by `30%` to attract labor.
- SemiAnalysis forecasts an electrician shortage from `2027`, especially in Texas and Ohio.
- Factory work can run while foundations and shells are built, use standardized instructions, and draw from a different labor pool.
- Earlier commissioned capacity matters because GPUs depreciate while idle and live compute earns revenue.

Market pays modular suppliers only where building completion is the binding date. If grid power, generation, GPUs, permits, or commissioning finish later, construction speed has no incremental value.

## Headline numbers

SemiAnalysis' tracking and estimates:

- More than `1,000` sites using some prefabrication or modular strategy.
- `61.5 GW` tracked modular capacity by `2028`.
- Modular share of tracked datacenter capacity rises from `5.6%` in `2022` to `31%` in `2028`.
- Forecast modular penetration: `30%+` of total live capacity by end-`2028`.
- Full modular 50 MW hall: roughly `14 months` midpoint, `12–18` month range.
- Pure stick-build: roughly `22 months` midpoint, `18–24` month range.
- Today's partly modular baseline: roughly `20 months`, `19–21` month range.
- Full modular saving versus pure stick-build: `8 months`, or `36%`.
- Full modular all-in cost: about `$13.5M/MW` versus `$14.6M/MW`, a `$1.1M/MW` or `7.6%` reduction.
- Moving MEP work into factory: on-site labor falls about `63%`, from `12,000` to `4,500` hours/MW; licensed-electrician hours fall about `85%`.
- Vertiv full-stack content opportunity: roughly `$7M/MW`, versus historical roughly `$3.5M/MW`.

Important: `61.5 GW` and `31%` are tracked/modelled future capacity, not proof every project will commission on time.

## What "LEGO datacenter" means

Modularization means breaking facility into factory-built units that can be transported, installed, connected, and tested on site.

It does **not** mean every vendor's block plugs into every other block.

### Prefabrication versus modularization

- **Prefabricated:** any piece manufactured off site and delivered ready to install.
- **Modular:** self-contained room, box, skid, or facility block shipped substantially complete and connected on site.

Every module is prefabricated. Not every prefabricated component is a module.

### Facility layers

1. **Site:** land, grading, utility routes, foundations. Cannot be moved into factory.
2. **Shell:** frame, walls, roof, weather enclosure.
3. **Systems:** power, cooling, white space, controls, storage, fire safety, and associated equipment.

Most economic modularization occurs in systems, not site.

## Modular taxonomy

### Component

Single factory-made equipment item.

### Skid

Multiple components arranged and connected on open frame.

### Module

Enclosed skid or factory-built room.

### Container

Module constrained to transport-friendly ISO dimensions.

### Prefab datacenter block

Large integrated block combining multiple modules into near-complete facility.

Greater factory integration can reduce field work but creates more design rigidity, logistics complexity, vendor dependence, and integration risk.

## Shell modularization

### Phase 1: precast or tilt-up concrete

Moves forming and curing away from field or onto slab. Still preserves conventional building design.

- CloudHQ Ashburn example still took about `18–20 months`.
- Tilt-up can be cheapest for simple single-story building but remains weather/site exposed.

### Phase 2: standardized steel halls

Uses repeatable bays and factory-made panels.

- QTS Cedar Rapids current `420 MW` phase: approximately `2.8M ft²`, `28,000 tons` structural steel, topping-out in five months, broader building in about `11 months`.
- Crusoe Abilene: roughly `672` panels/building, made in under `40 days`, installed `15–20/day`, dried-in shell under eight weeks.

Real gain comes from simpler, single-story repeatability, not steel alone. Trade-off: more land.

### Phase 3: purpose-built rapid enclosures

Meta Prometheus uses roughly `125,000 ft²` aluminum-frame, fabric-clad halls.

Eight structures stood by April `2026` after July `2025` announcement. This is not a nine-month complete datacenter: tents only accelerate enclosure. Utility interconnection, power, cooling, systems integration, and commissioning remain.

Trade-off: lower durability and future flexibility.

## System modularization

### Power blocks

Factory-built electrical rooms packaging transformers, switchgear, UPS, batteries, busway, controls, HVAC, and fire systems.

Power naturally modularizes because equipment chain is defined and field wiring/testing is extensive.

For a `50 MW` hall:

- Electrical fit-out and commissioning: `5.5–16.7 months` in article's broad benchmark.
- Power scope is roughly `26%` of build content.
- Power modularization alone: approximately `13 months` to IT-ready versus `16.7`, `22%` faster and about `5%` cheaper/MW.
- Mechanical/electrical fit-out can fall from `5.5` to `2.5 months`.

New "software-defined" power blocks, such as DG Matrix, replace parts of transformer/switchgear/UPS chain with multi-port power electronics connecting grid, generation, storage, and DC loads.

### Cooling blocks

Factory-built CDUs, pumps, buffer tanks, controls, leak detection, piping, and mechanical-yard equipment.

- Modine/Airedale CDU skid: about `2 MW` class.
- Karman CO2 heat-processing unit claim: `4–5x` conventional power density and `60–80%` less yard footprint.

Cooling modularity becomes more valuable as dense liquid cooling expands piping and controls. But hundreds of outdoor units create recirculation and heat-islanding risks.

### Factory-built white space

Prepared rack hall with rack positions, overhead busway, cooling water loop, containment, fiber, and cabling.

- Schneider EcoStruxure Pod: up to `40` racks.
- Schneider reportedly supports `30+` Nvidia-related reference designs.
- AWS Project Houdini falls in this category.

### Containerized datacenter

IT, power, batteries, and cooling inside transportable enclosure.

Best for edge, remote sites, and location-specific inference. Portability limits layout and density.

### All-in-one prefab block

Near-complete datacenter shipped in sections.

- Vertiv MegaMod `1 MW` reference: around `26.5m × 24m × 4m`; MegaMod Plus up to `31m` wide.
- Still must be split into transportable sections, assembled, interconnected, and commissioned.

### Platform/reference design

Nvidia DSX covers compute, networking, storage, facility power, cooling, controls, civil, structural, and architectural design.

- DSX Max-Q targets tokens/watt under fixed power.
- DSX Flex coordinates facility load with grid and onsite generation.
- Omniverse DSX Blueprint creates digital twin for layouts, thermal behavior, power topology, and operations.
- Vertiv OneCore packages `12.5 MW` pods.
- EdgeConneX says common design can advance project to `30–60%` permit set before site localization.

Reference design is not commissioned capacity. Site-specific code, utility, soils, climate, equipment, transport, controls, and reliability still require engineering.

## Who owns integration

### Operator-led

Hyperscaler specifies design, buys equipment, owns inventory/lead-time risk, and hires factory assembler.

Examples: AWS Houdini with Cupertino Electric; Aligned's own architecture with external factories.

Advantages:

- control and vendor flexibility;
- procurement leverage at hyperscale;
- design tailored to workload.

Risks:

- deep internal engineering required;
- operator carries scarce-equipment inventory and schedule risk.

### EPC/system-integrator-led

Integrator sources third-party gear, assembles, wires, pipes, tests, and ships module.

Examples: Comfort Systems, Sterling Infrastructure, Quanta/Cupertino Electric, PCX, Nautilus, DXN, Infra Partners, Bladeroom.

Advantages:

- vendor agnostic;
- operator keeps design and preferred equipment;
- field construction becomes factory construction.

Comfort Systems reportedly has `3.5M+ ft²` of shop floor through Environmental Air Systems and TAS Energy.

### OEM-led

OEM sells own power/cooling/white-space stack as integrated product.

Examples: Vertiv OneCore, Schneider, Eaton, Siemens.

Advantages:

- single architecture and accountability;
- OEM captures more content.

Risks:

- customer lock-in;
- factory and integration capacity constrain growth;
- execution extends beyond OEM's historical scope.

Vertiv modular lead times exceed `12 months` according to article, showing modular demand can simply shift bottleneck into factory slots.

## Actual project cycle

### 1. Design and simulation

Facility-level load, equipment, single-line diagram, layout, short-circuit, protection coordination, and arc-flash analysis must precede module design.

At `415/480VAC`, templates are mature. `800VDC` is not yet standardized.

Aran claims software can compress a `>2 month`, multi-engineer design process into hours of compute plus one engineer's review.

### 2. Documentation

Separate packages:

- IFF: issued for fabrication;
- IFC: issued for construction;
- permitting and commissioning documents.

Single design model can reduce redraw and drift.

### 3. Assembly and factory acceptance testing

Module is assembled through inspection gates, then powered and tested as standalone unit.

`1-10-100` rule: `$1` defect fix in design/assembly may cost `$10` in production and `$100` after shipping.

### 4. Transport and installation

Logistics is not trivial.

- Permit-free US width: `102 inches`.
- Gross vehicle limit: `80,000 lb`, leaving roughly `24 tons` for module on standard deck.
- Oversize permit: roughly `$15–100/state`.
- Line-haul: `$12–14/loaded mile`; `500 miles` costs around `$6,000–7,000/trailer`.
- Superload review: `7–21 days/state`, potentially months across route.
- State thresholds differ.
- Crane cost: roughly `$5,000–25,000/day`.
- Example Schneider `500 kW` power module: `50,000 lb`, six lifting points.

Transport creates vibration, braking, insurance, bridge clearance, route, crane, and damage risks.

### 5. Site commissioning

Factory test proves standalone module. Site commissioning proves integrated facility.

Article says full commissioning takes `3–8 months`.

- L1: factory witness test.
- L2: delivery and installation verification.
- L3: startup.
- L4: functional performance.
- L5: integrated systems test under simulated failures.

L2 onward largely occurs on site. Utility, generators, BESS, cooling, controls, and failover behavior only meet there.

Main bottleneck can be L3 point-to-point verification across hundreds of PDUs and BMS points.

Aggressive `6–9 month` schedules may compress commissioning and transfer latent risk into operations.

## Schedule economics

### Construction windows, permitting excluded

- Stick-build: `18–24 months`, chart midpoint `22`.
- Today's baseline: `19–21`, midpoint `20`.
- MEP-heavy skids: `16–18`, midpoint `17`, `23%` faster than stick-build.
- Full modular: `12–18`, midpoint `14`, `36%` faster.
- Containerized: about `12`, `45%` faster.

Permitting adds roughly `12–13 months` in author's model, producing approximately `30–35+ months` all-in for stick-build and `24–30` for modular.

### Labor bridge

A 50 MW AI hall:

- roughly `600,000` field hours;
- around `300` craft workers at peak;
- MEP factory shift lowers on-site hours by about `63%`;
- electrician hours fall roughly `85%`.

Schedule shrinks less than hours because some work moves off site and overlaps other phases.

### Revenue/depreciation value

SemiAnalysis uses:

- CSP revenue: about `$12–15M/IT MW/year`, or `$1–1.25M/MW/month`.
- Some model-lab API revenue: more than `$50M/MW` claim.
- Nvidia cluster GPU basis: around `$30M/MW`, five-year depreciation, or `$500k/MW/month`.
- Wholesale colo lease: roughly `$190k/MW/month`.

Eight-month acceleration on 50 MW at `$500k/MW/month` creates roughly `$200M`, or `$4M/MW`, of undiscounted value in model.

Critical caveat: value exists only if building date is latest of:

`building ready | power available | GPUs delivered`

If another date binds, modular speed creates zero acceleration value.

## Cost bridge

SemiAnalysis chart moves from `$14.6M/MW` stick-build to `$13.5M/MW` modular:

Savings:

- construction services: `-$0.6M/MW`;
- equipment installation: `-$0.5M/MW`;
- escalation: `-$0.3M/MW`;
- contingency: `-$0.2M/MW`;
- change orders: `-$0.1M/MW`;
- site general conditions: `-$0.2M/MW`.

Penalties:

- double margin: `+$0.6M/MW`;
- factory burden: `+$0.1M/MW`;
- module premium: `+$0.1M/MW`.

Net: `-$1.1M/MW`, or `-7.6%`.

Hardware itself does not become much cheaper. Same transformers, UPS, switchgear, and cooling equipment remain. Savings come from labor productivity and shorter project duration.

## Vendor claims versus whole-project result

Different scopes make headline percentages incomparable:

- Vertiv SmartRun: `85%`, but overhead busway/containment only.
- Schneider EcoStruxure: `60%`, power/cooling modules only.
- Vertiv MegaMod: `50%`, module deployment versus on-site build.
- ABB prefab/eHouse: `50%`, described as `30%` prefab plus `20%` pre-design.
- SemiAnalysis whole construction estimate: `36%`.
- Flex PMDC whole-project claim: `30%`.

Vendor claim can be true for module and misleading for complete commissioned facility.

## Quality case and counterevidence

Claimed factory first-pass quality:

- modular: more than `95%`;
- field baseline: `60–70%`.

Benefits: controlled environment, repeated work instructions, inspection gates, repeatable FAT.

Counterpoint: some operators and MEP contractors report reliability problems in modular solutions. Field remediation can erase schedule savings and threaten expensive IT hardware. Article does not provide enough defect-rate data to determine which view dominates.

## Operator examples

### AWS

- Added almost `3.9 GW` capacity through end-`2025`, per article.
- Project Houdini factory-built white space.
- Claimed deployment reduction: up to `15 weeks` to `2–3 weeks`.
- More than `50,000` on-site electrician hours eliminated per module.
- Target: roughly `25 weeks` from construction start to first server room.

This is one subsystem schedule, not full site commissioning.

### Meta

Prometheus rapid fabric structures speed enclosure. They do not speed utility, power, cooling, or commissioning equally and may sacrifice long-term durability.

### Crusoe

- Abilene shell panels under eight weeks.
- Bought Easter-Owens in `2022` to vertically integrate modular electrical/facility production.
- Spark units approximately `1 MW` each.
- Redwood deployment grew from four units with `12 MW` microgrid to announced 24 units.

### Hut 8

- Beacon Point uses Vertiv OneCore for `704 MW` IT lease.
- Nvidia DSX design; AEP utility relationship; Jacobs EPCM; Vertiv power/cooling.

This is planned/commercialized capacity, not proof all 704 MW is commissioned.

### Nebius

- New Jersey planned phased expansion to `300 MW`.
- Precast shell plus Bloom behind-the-meter fuel cells.
- France project reuses Bridgestone plant to avoid some greenfield shell/permitting work.

### Compass

- Estimated `70–85%` of building manufactured off site.
- Framework/roof erected in `18–21 days`.
- Repeatable `1.25 MW` Schneider power centers.
- Siemens agreement up to `1,500` modular MV switchgear units over five years.

### QTS

- Around `7M ft²` warehouse capacity in Kansas for long-lead equipment.
- Freedom pods: `1.5 MW` UPS/switchgear with `2.25 MW` generator.
- New repeatable `60 MW` hall blocks.
- QTS estimates labor pressure increased cost by `20–30%/MW`.

Warehousing shifts supply-chain risk onto balance sheet but improves schedule control.

### Aligned

- Standardized `2 MW` UPS container.
- Delta³ air cooling: up to about `50 kW/rack`.
- DeltaFlow liquid cooling: above `350 kW/rack`.
- Common chilled-water interfaces allow cooling mix to change.
- Project Caprock: `540 MW`, six buildings, `1.65M ft²`.

## Beneficiary map

### Integrated OEMs

Vertiv, Schneider, Eaton, Siemens.

Benefit: sell more of power, thermal, white-space, controls, and steel stack per MW. Vertiv's potential content doubles from about `$3.5M/MW` to `$7M/MW`.

Risk: factory slots, working capital, supplier capacity, execution outside historical product scope, customer lock-in resistance.

### EPCs and system integrators

Comfort Systems (`FIX`), Sterling Infrastructure (`STRL`), Quanta/Cupertino Electric (`PWR`) and private specialists.

Benefit: convert customer-specified equipment into tested factory modules while preserving vendor neutrality.

Risk: modular work can still be project-based, labor-heavy, low-margin, and exposed to cost overruns.

### Contract manufacturers and component assemblers

Flex/Anord Mardix (`FLEX`), Modine/Airedale and others.

Benefit: volume shifts from jobsites to scalable production floors.

Risk: customer concentration, factory underutilization after capex cycle, double-margin pressure.

### Structural/fabrication suppliers

Steel, precast, panel, and modular-enclosure vendors cited across article, plus private builders.

Need program-level wins and margin evidence; generic steel exposure is not enough.

## Winners and losers by business model

Likely winners:

- suppliers controlling scarce factory capacity close to build clusters;
- OEMs able to integrate full power/cooling stack reliably;
- EPC integrators retaining equipment neutrality;
- digital engineering, simulation, commissioning, BMS, and logistics specialists;
- operators with standardized fleet designs and procurement scale.

Potential losers:

- traditional field labor and contractors unable to move into prefab;
- small developers lacking procurement leverage or minimum order size;
- single-product OEMs whose content gets bundled by full-stack vendor;
- operators locking into immature architecture before rack density, cooling, or voltage standards stabilize.

## What "LEGO" analogy hides

Actual interoperability can fail across:

- dimensions and lifting points;
- AC/DC voltage and protection scheme;
- busway and connector interfaces;
- liquid loop chemistry, pressure, temperature, and flow;
- firmware and controls;
- BMS telemetry and naming;
- network/cable topology;
- fire and building codes;
- utility requirements;
- transport routes;
- commissioning and failover behavior.

Modules are repeatable within a controlled architecture. They are not generally interchangeable commodity bricks.

## Main caveats

1. **Modelled capacity is not commissioned capacity.** Announced projects can slip or change scope.
2. **No universal modular definition.** One vendor means busway; another means whole facility.
3. **Vendor percentages use different clocks.** Compare start/end points and excluded scope.
4. **Permitting and site work remain.** Foundation and utility cannot be factory-built.
5. **Commissioning remains local.** L2–L5 and integrated failure tests happen on site.
6. **Speed has value only on critical path.** No value if power/GPU delivery binds.
7. **Quality evidence is mixed.** Factory yields claimed strong, operator reliability concerns unresolved.
8. **Design freezes earlier.** Late rack-density, cooling, or electrical changes become expensive.
9. **Bottlenecks move.** Field labor shortage can become factory-slot, transformer, logistics, crane, or integrator bottleneck.
10. **Equity upside is not automatic.** Require shipments, pricing, margins, working capital, FCF, and valuation.

## KPIs to track

Industry:

- commissioned modular MW, not announced MW;
- construction start to IT-ready and permit-to-commission timeline;
- on-site hours/MW and licensed-electrician hours/MW;
- factory first-pass yield and field rework rate;
- L3/L5 commissioning duration;
- cost/MW after change orders and remediation;
- percentage of projects where building was true critical path;
- transport damage and schedule slippage;
- repeat orders across campuses.

Public companies:

- modular backlog converted to revenue;
- content/MW and attach rate;
- modular gross margin versus legacy equipment/project work;
- inventory and working-capital growth;
- factory utilization and capacity additions;
- cancellation/deferral rates;
- customer concentration;
- warranty and rework reserves;
- free cash flow after factory capex.

## Falsification tests

Article thesis weakens if:

- modular sites fail to commission materially faster end to end;
- grid/interconnect consistently dominates timeline, making building speed irrelevant;
- factory defects and field remediation erase schedule savings;
- modular cost exceeds stick-build after double margin, logistics, and change orders;
- changing rack power/cooling standards cause stranded designs;
- labor supply catches up or datacenter demand slows;
- vendors cannot turn higher content/MW into higher gross profit and FCF;
- announced 61.5 GW fails to convert into live capacity.

## My read

Strong article because it separates subsystem marketing from whole-site economics. Real edge is not "prefab is cheaper." It is factory parallelism against scarce field labor plus avoiding idle GPU depreciation. Best businesses should control integration, test quality, factory slots, and scarce components—not merely manufacture boxes.

Vertiv has clearest content/MW upside, while Comfort Systems/Sterling/Quanta offer equipment-neutral integration. But modularization may shift rather than eliminate bottlenecks, and a reference design is not a plug-and-play datacenter. Investment proof must appear in margins and cash flow, not tracked GW or vendor speed claims.
