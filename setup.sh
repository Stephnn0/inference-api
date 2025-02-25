#!/bin/bash

echo "Updating and upgrading system packages..."
apt update && apt upgrade -y

echo "Installing Vim..."
apt install -y vim

echo "Setting up Python virtual environment..."
cd /workspace
python3 -m venv env

echo "Activating virtual environment..."
source env/bin/activate


echo "Installing Python dependencies..."
pip install transformers peft bitsandbytes trl deepeval huggingface_hub datasets flask flask_cors 

echo "Setup completed successfully!"
