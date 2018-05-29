#!/bin/bash

# Download all of the software and dependencies
apt-get update
apt-get install gqrx pkg-config librtlsdr-dev -y
ln -sf /usr/lib/x86_64-linux-gnu/libvolk.so.1.3.1 /usr/lib/x86_64-linux-gnu/libvolk.so.1.3

# Get dump1090 for decoding ADS-B and isntall
git clone https://github.com/antirez/dump1090.git /opt/dump1090
cd /opt/dump1090
make 