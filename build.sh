#!/bin/bash

set -e

cd application

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

# Download h5 files
if [ -d "models" ] && [ -f "models/face_model.h5" ] && [ -f "models/image_model.h5" ]; then
    echo "Skipping download process for models..."
else
    echo "Initiating download process for models..."
    python3 download.py
fi

start_backend() {
    echo "Starting Flask backend..."
    gnome-terminal -- python3 flask_backend.py
}

start_frontend() {
    echo "Starting Streamlit frontend..."
    gnome-terminal -- bash -c "streamlit run streamlit_frontend.py --server.enableCORS false; exec bash"
}

# Start Flask backend
start_backend
sleep 5

# Start Streamlit frontend
start_frontend
