#!/bin/bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment
source env/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install the required modules
pip install -r requirements.txt

# Run your script
python main.py