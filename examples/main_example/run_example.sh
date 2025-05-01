#!/bin/bash
# Script to run the TBH Secure Agents examples

# Check if API key is set
if [ -z "$GOOGLE_API_KEY" ]; then
    echo "Error: GOOGLE_API_KEY environment variable is not set."
    echo "Please set your API key with: export GOOGLE_API_KEY=your_api_key_here"
    exit 1
fi

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

# Ask user which example to run
echo ""
echo "Which example would you like to run?"
echo "1) Comprehensive Example (with security profiles and guardrails)"
echo "2) Original Example (with basic security profiles)"
echo ""
read -p "Enter your choice (1 or 2): " choice

case $choice in
    1)
        echo ""
        echo "Running comprehensive example..."
        python comprehensive_example.py
        ;;
    2)
        echo ""
        echo "Running original example..."
        python main_example.py
        ;;
    *)
        echo ""
        echo "Invalid choice. Please run the script again and select 1 or 2."
        ;;
esac

# Deactivate virtual environment
deactivate
