#!/bin/bash
# Script to run the TBH Secure Agents main example

# Check if virtual environment exists, create if not
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Run the example
echo "Running main example..."
python main_example.py

# Deactivate virtual environment
deactivate
