#!/bin/bash

# run data download script
uv run python3 -m mite_web_extras.main

# run image generation script
./mite_web_extras/run_pymol.sh