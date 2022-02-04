#!/bin/bash

if [ ! -d "./env" ]
then
    echo "Creating virtual environment for the CLI..."
    python3 -m venv env
    echo "Installing dependencies..."
    ./env/bin/pip install -r requirements.txt
fi

