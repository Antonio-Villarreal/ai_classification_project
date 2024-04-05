#!/bin/bash

# Check if the classification-app image exists for Linux
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if ! docker images classification-app | grep -q classification-app; then
        # Build Docker image
        docker build -t classification-app /application
    fi

    # Run Docker container
    docker run -d -p 5001:5001 -p 8501:8501 --name classification-app classification-app
    sleep 5

    # Open localhost:8501
    xdg-open http://localhost:8501

# Check if the classification-app image exists for Windows
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    if ! docker images classification-app | grep -q classification-app; then
        # Build Docker image
        docker build -t classification-app /application
    fi

    # Run Docker container
    docker run -d -p 5001:5001 -p 8501:8501 --name classification-app classification-app
    sleep 5

    # Open localhost:8501
    start http://localhost:8501

else
    echo "Unsupported operating system"
    exit 1
fi
