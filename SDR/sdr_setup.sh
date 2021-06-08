#!/usr/bin/zsh

# check perms
if [[ $EUID -ne 0 ]]; then
        echo "This script must be run as root or with sudo"
        exit 1
fi

# download all of the software and dependencies
apt update
apt install gqrx pkg-config librtlsdr-dev -y
ln -sf /usr/lib/x86_64-linux-gnu/libvolk.so.1.3.1 /usr/lib/x86_64-linux-gnu/libvolk.so.1.3

# downlaod and install audacity
apt install audacity -y

# install rfcat for transmitting 
apt  install rfcat -y

# clean up any old ADSB installs
rm -rf /opt/dump1090
rm -rf /usr/local/lib/librtlsdr*

# build the new version of dump1090-fa
cd /opt
sudo bash -c "$(wget -O - https://raw.githubusercontent.com/abcd567a/piaware-ubuntu20-amd64/master/install-dump1090-fa.sh)"

# blacklist the default TV tuner driver
echo 'blacklist dvb_usb_rtl28xxu' | sudo tee --append /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf

echo 'Script finished, look for errors and reboot'