#!/bin/bash
# Run all chart generation scripts for Google deep dive analysis

set -e  # Exit on error

echo "======================================================================"
echo "Google (Alphabet) Investment Analysis - Chart Generation"
echo "======================================================================"
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

# Install dependencies if needed
echo "Checking dependencies..."
if ! python3 -c "import yfinance" 2>/dev/null; then
    echo "Installing required Python packages..."
    pip3 install -r requirements.txt --quiet
fi

echo ""
echo "======================================================================"
echo "Step 1: Fetching Financial Data from Yahoo Finance"
echo "======================================================================"
python3 fetch_financials.py

echo ""
echo "======================================================================"
echo "Step 2: Generating Revenue Charts"
echo "======================================================================"
python3 generate_revenue_charts.py

echo ""
echo "======================================================================"
echo "Step 3: Generating Profitability Charts"
echo "======================================================================"
python3 generate_profitability.py

echo ""
echo "======================================================================"
echo "Step 4: Generating Cloud Analysis Charts"
echo "======================================================================"
python3 generate_cloud_analysis.py

echo ""
echo "======================================================================"
echo "Step 5: Generating CapEx Analysis Charts"
echo "======================================================================"
python3 generate_capex_analysis.py

echo ""
echo "======================================================================"
echo "All charts generated successfully!"
echo "======================================================================"
echo ""
echo "Charts saved to: $SCRIPT_DIR/../charts/"
ls -lh ../charts/*.png

echo ""
echo "Data files saved to: $SCRIPT_DIR/../data/"
ls -lh ../data/*.csv

echo ""
echo "Done! Check the charts directory for visualizations."
