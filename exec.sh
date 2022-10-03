#!/bin/bash

# Create python enviroment and install dependencies

# Create virtual enviroment

python -m venv venv

# Activate virtual enviroment

source venv/bin/activate

# Install dependencies

pip install -r requirements.txt

# Run the script

python main.py