#!/bin/bash

set -e

VENV_PATH="venv"
if ! [ -x "$VENV_PATH" ]; then
    echo "Setting up virtual environment and installing dependencies..."
    # Check for Python 3.10 and create a virtual environment
    PYTHON_BIN=$(command -v python3.10 || command -v python3)
    if [ -z "$PYTHON_BIN" ]; then
        echo "Error: Python 3.10 is not installed. Please install Python 3.10 before running this script." >&2
        exit 1
    fi

    # Create virtual environment
    $PYTHON_BIN -m venv "$VENV_PATH"
    source "$VENV_PATH/bin/activate"

    # Install requirements
    if [ -e "requirements.txt" ]; then
        pip install -r requirements.txt
    else
        echo "Error: requirements.txt not found. Please ensure the file exists before running this script." >&2
        exit 1
    fi

    echo "Virtual environment setup completed."
else
    echo "Virtual environment already set up."
    source "$VENV_PATH/bin/activate"
fi

python3 download.py

cd application

# Start Flask backend
echo "Starting Flask backend..."
python3 flask_backend.py &

# Wait for Flask to start (adjust sleep time as needed)
sleep 5

# Start Streamlit frontend
echo "Starting Streamlit frontend..."
streamlit run streamlit_frontend.py
