#!/bin/bash

if [ ! -d "./env" ]
then
    echo "Creating virtual environment for installing server..."
    python3 -m venv env
    echo "Installing dependencies..."
    ./env/bin/pip install -r requirements.txt
fi

echo "Starting server..."
./env/bin/python src/server/main.py