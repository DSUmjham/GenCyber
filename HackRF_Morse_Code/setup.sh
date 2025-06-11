#!/bin/bash
set -e

echo "Updating package list..."
sudo apt update

echo "Installing system packages: Python3, pip, HackRF, GQRX, Audacity..."
sudo apt install -y python3 python3-pip hackrf gqrx-sdr audacity

echo "Installing required Python packages (numpy, scipy)..."
pip3 install --user numpy scipy