#! /usr/bin/env sh

# Run pre-start script
bash /app/bash_scripts/pre_start.sh

# Run server
python /app/main.py
