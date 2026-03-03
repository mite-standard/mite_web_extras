#!/bin/bash

# run data download script
echo "Started mite_web_extras"
python -m mite_web_extras.main

echo "Started image generation"
# run image generation script
./mite_web_extras/run_pymol.sh

echo "Started cleanup generation"
# run cleanup script
python -m mite_web_extras.cleanup