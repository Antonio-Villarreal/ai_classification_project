#!/bin/bash

# Check the operating system
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Get the container ID for classification-app
    container_id=$(docker ps -qf "name=classification-app")

    # Stop the container
    docker stop $container_id
    # Remove the container
    docker rm $container_id
    # Remove the image
    if [[ "$1" == "--clear" || "$1" == "-c" ]]; then
        docker rmi classification-app
    fi
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Stop the container
    docker stop classification-app
    # Remove the container
    docker rm classification-app
    # Remove the image
    if [[ "$1" == "--clear" || "$1" == "-c" ]]; then
        docker rmi classification-app
    fi
else
    echo "Unsupported operating system"
    exit 1
fi
