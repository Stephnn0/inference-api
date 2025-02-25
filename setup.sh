# curl -X POST https://rft2llt7bwlu6a-3000.proxy.runpod.net/stream \
#-H "Content-Type: application/json" \
#-d '{"prompt": "hello"}'


#!/bin/bash

# scp -r -P 26488 -i ~/.ssh/tapiastephano0@gmail.com /home/system-1/Documents/ai/tuning_results/checkpoint-550 root@38.147.83.21:/workspace/training

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
