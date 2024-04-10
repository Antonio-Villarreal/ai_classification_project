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
if [ -f "face_model.h5" ] && [ -f "image_model.h5" ]; then
    echo "Skipping download process for models..."
else
    echo "Initiating download process for models..."
    python3 download.py
fi

start_backend_linux() {
    echo "Starting Flask backend..."
    if ! command -v gnome-terminal &> /dev/null; then
        echo "gnome-terminal is not installed. Installing it now..."
        sudo apt update
        sudo apt install -y gnome-terminal
    fi

    gnome-terminal -- python3 flask_backend.py
}

start_frontend_linux() {
    echo "Starting Streamlit frontend..."
    gnome-terminal -- bash -c "streamlit run streamlit_frontend.py --server.enableCORS false; exec bash"
}

start_backend_mac() {
    echo "Starting Flask backend..."
    open -a Terminal python3 flask_backend.py
}

start_frontend_mac() {
    echo "Starting Streamlit frontend..."
    open -a Terminal bash -c "streamlit run streamlit_frontend.py --server.enableCORS false; exec bash"
}

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Start Flask backend
    start_backend_linux
    sleep 15
    
    # Start Streamlit frontend
    start_frontend_linux
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # Start Flask backend
    start_backend_mac
    sleep 15
    
    # Start Streamlit frontend
    start_frontend_mac
else
    echo "Unsupported operating system"
    exit 1
fi
