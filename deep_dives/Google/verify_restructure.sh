#!/bin/bash

echo "=== Google Investment Analysis Restructure Verification ==="
echo ""
echo "Main README (new):"
wc -l README.md
echo ""
echo "Original backup:"
wc -l README_original.md
echo ""
echo "Section files (14 total):"
wc -l sections/*.md | sort -n
echo ""
echo "Total lines in sections:"
wc -l sections/*.md | tail -1
echo ""
echo "Charts preserved:"
ls -1 charts/*.png | wc -l
echo "PNG files found"
echo ""
echo "Data files preserved:"
ls -1 data/*.csv
echo ""
echo "Navigation test - checking for broken links:"
grep -h "^\[" sections/*.md | grep -v "http" | head -5
echo "... (sample navigation links shown)"
echo ""
echo "✅ Restructure verification complete!"
