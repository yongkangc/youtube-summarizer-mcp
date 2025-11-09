#!/bin/bash

# Script to add navigation headers to all section files

cd "$(dirname "$0")/../sections"

# Define section titles
declare -A titles=(
    ["02_company_overview.md"]="Company Overview"
    ["03_ai_thesis.md"]="The AI Thesis: Google's Innovator's Dilemma"
    ["04_seven_powers.md"]="Hamilton Helmer's 7 Powers Framework"
    ["05a_bull_case.md"]="Bull Case Analysis"
    ["05b_bear_case.md"]="Bear Case Analysis"
    ["06_financial_analysis.md"]="Financial Analysis"
    ["07_competitive_positioning.md"]="Competitive Positioning"
    ["08_strategic_initiatives.md"]="Strategic Initiatives & Execution"
    ["09_talent_dynamics.md"]="Key People & Talent Dynamics"
    ["10_acquisitions.md"]="Acquisitions & M&A Strategy"
    ["11_risks_mitigations.md"]="Risks & Mitigations"
    ["12_metrics_kpis.md"]="Quantitative Metrics & KPIs"
    ["13_appendix_data.md"]="Appendix: Data & Charts"
)

# Define navigation links
declare -A prev=(
    ["02_company_overview.md"]="01_investment_recommendation.md|Investment Recommendation"
    ["03_ai_thesis.md"]="02_company_overview.md|Company Overview"
    ["04_seven_powers.md"]="03_ai_thesis.md|AI Thesis"
    ["05a_bull_case.md"]="04_seven_powers.md|7 Powers Framework"
    ["05b_bear_case.md"]="05a_bull_case.md|Bull Case"
    ["06_financial_analysis.md"]="05b_bear_case.md|Bear Case"
    ["07_competitive_positioning.md"]="06_financial_analysis.md|Financial Analysis"
    ["08_strategic_initiatives.md"]="07_competitive_positioning.md|Competitive Positioning"
    ["09_talent_dynamics.md"]="08_strategic_initiatives.md|Strategic Initiatives"
    ["10_acquisitions.md"]="09_talent_dynamics.md|Talent Dynamics"
    ["11_risks_mitigations.md"]="10_acquisitions.md|Acquisitions"
    ["12_metrics_kpis.md"]="11_risks_mitigations.md|Risks"
    ["13_appendix_data.md"]="12_metrics_kpis.md|Metrics & KPIs"
)

declare -A next=(
    ["02_company_overview.md"]="03_ai_thesis.md|AI Thesis"
    ["03_ai_thesis.md"]="04_seven_powers.md|7 Powers Framework"
    ["04_seven_powers.md"]="05a_bull_case.md|Bull Case"
    ["05a_bull_case.md"]="05b_bear_case.md|Bear Case"
    ["05b_bear_case.md"]="06_financial_analysis.md|Financial Analysis"
    ["06_financial_analysis.md"]="07_competitive_positioning.md|Competitive Positioning"
    ["07_competitive_positioning.md"]="08_strategic_initiatives.md|Strategic Initiatives"
    ["08_strategic_initiatives.md"]="09_talent_dynamics.md|Talent Dynamics"
    ["09_talent_dynamics.md"]="10_acquisitions.md|Acquisitions"
    ["10_acquisitions.md"]="11_risks_mitigations.md|Risks"
    ["11_risks_mitigations.md"]="12_metrics_kpis.md|Metrics & KPIs"
    ["12_metrics_kpis.md"]="13_appendix_data.md|Appendix"
)

# Process each file
for file in 02_*.md 03_*.md 04_*.md 05a_*.md 05b_*.md 06_*.md 07_*.md 08_*.md 09_*.md 10_*.md 11_*.md 12_*.md 13_*.md; do
    if [ ! -f "$file" ]; then
        continue
    fi

    title="${titles[$file]}"
    prev_link="${prev[$file]}"
    next_link="${next[$file]}"

    # Build navigation
    nav="[← Back to Main](../README.md)"

    if [ -n "$prev_link" ]; then
        IFS='|' read -r prev_file prev_title <<< "$prev_link"
        nav="[← ${prev_title}](${prev_file}) | $nav"
    fi

    if [ -n "$next_link" ]; then
        IFS='|' read -r next_file next_title <<< "$next_link"
        nav="$nav | [Next: ${next_title} →](${next_file})"
    fi

    # Create header
    header="# ${title}\n\n${nav}\n\n---\n\n"

    # Remove old section header (lines starting with ## I. or ## II. etc)
    sed -i 's/^## [IVX]*\. /## /' "$file"

    # Add header at top
    echo -e "${header}$(cat $file)" > "$file"

    # Add footer navigation
    echo -e "\n---\n\n${nav}" >> "$file"

    echo "Processed: $file"
done

echo "All section headers added!"
