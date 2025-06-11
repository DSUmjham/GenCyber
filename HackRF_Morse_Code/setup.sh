#!/bin/bash
set -e

echo "Updating package list..."
sudo apt update

echo "Installing system packages: Python3, pip, HackRF, GQRX, Audacity..."

sudo apt install -y python3 python3-pip hackrf gqrx-sdr audacity alsa-utils

echo "Installing required Python packages (numpy, scipy)..."
python3 -m venv ~/py_envs
source ~/py_envs/bin/activate
python3 -m pip install numpy

pip3 install numpy scipy