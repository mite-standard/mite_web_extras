#!/bin/bash

# run data download script
echo "Started mite_web_extras"
/mite_web_extras/.venv/bin/python -m mite_web_extras.main

echo "Started image generation"
# run image generation script
./mite_web_extras/run_pymol.sh

echo "Started cleanup generation"
# run cleanup script
/mite_web_extras/.venv/bin/python -m mite_web_extras.cleanup