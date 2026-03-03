#!/bin/bash

# run data download script
python -m mite_web_extras.main

# run image generation script
./mite_web_extras/run_pymol.sh

# run cleanup script
python -m mite_web_extras.cleanup