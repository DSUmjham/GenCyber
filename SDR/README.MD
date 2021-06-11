


# Software Defined Radios
This part of the repo has examples, code, and scripts needed to run the SDRs as we did in the GenCyber camp at DSU.

* [Hardware](#Hardware)
* [Software](#Software)
	* [Setting up a new Kali VM](#setting-up-a-new-kali-VM)
	* [Gqrx](#gqrx)
	* [dump1090=fa](#dump1090-fa)
	* [Audacity](#audacity)
	* [RfCat](#rRfCat)
* [Resources](#resources)

## Hardware
In the class we are using the popular RTL2832 SDR which can be found on [Adafruit](https://www.adafruit.com/product/1497) or other suppliers.

* Cost \~$20 depending on the quantity you order and where from
* 24MHz to 1850MHz 
	* FM Radio
	* AM signals (but not AM radio)
	* CW or morse code
	* Unencrypted radio signals
	* Pagers, garage door openers, remote power outlets, other connected devices
* Receive only, does not have the ability to transmit

To transmit data using an SDR, the [YARD Stick One](https://greatscottgadgets.com/yardstickone/) is capable radio.  The official operating frequencies are: 300-348 MHz, 391-464 MHz, and 782-928 MHz.  This should be sufficient for most ISM devices.

## Software
* 64-bit Kali linux virtual machine
* [Gqrx](http://gqrx.dk) used to capture radio signals and raw wireless data.
* [dump1090-fa](https://github.com/adsbxchange/dump1090-fa) decodes ADSB aircraft beacons and comes with a web server to plot planes flying overhead.
* [Audacity](https://github.com/audacity/audacity) used to analyze raw signal captures and demodulate them
* [RfCat](https://github.com/atlas0fd00m/rfcat) software to transmit using a YARD Stick One (YS1)

### Setting up a new Kali VM
If you have a Kali virtual machine running, the following instructions will update the VM and pull down the necessary software for you:

 1.  Inside of Kali, open up the **Terminal** or **Terminator** if that is installed.
 2. Download and run the script
	```console
	sudo zsh -c "$(wget -O - https://raw.githubusercontent.com/DSUmjham/GenCyber/master/SDR/sdr_setup.sh)"
	```

### Gqrx
Gqrx is an open source software defined radio receiver (SDR).  It is useful for picking up FM radio, weather radio (narrow FM), and raw signals.  Gqrx has the ability to record signals sent which can then be processed later.

 1. Run Gqrx from anywhere in the terminal using the following command
	 ```console
	 gqrx
	 ```

2. If for some reason you need to reset the Gqrx settings, you can do so by removing the Gqrx config file:
	```console
	rm ~/.config/gqrx/default.conf
	```
### dump1090-fa
dump1090-fa is a Mode S decoder specifically designed for RTLSDR devices.  It allows us to capture ADSB beacons and plot them on a live map using Google maps.

1. To start dump1090-fa, open up a Terminal in Kali.
2. Start the dump1090-fa service (note: the SDR cannot be in use elsewhere)
	```console
	sudo service dump1090-fa start
	```
3. To check if the service is running
	```console
	sudo service dump1090-fa status
	```
4. Open the Firefox web browser and navigate to http://localhost/skyaware to view the map.  Once open, you will need to manually find your location on the map to view aircraft.
5. To view the raw data, navigate to http://localhost:30003

### Audacity
Audacity is an open-source software package used for editing audio files.  It also happens to be very useful for viewing raw wireless signals captured from an SDR.  The signals can then be manually demodulated to extract the binary patterns that the signal represents.

1. Start audacity and open the capture file that you generated from anywhere in the Terminal
	```console
	audacity
	```
### RfCat
RfCat is an open-source software program used to transmit data with a variety of SDRs.  The tool was created to allow security researchers to analyze unknown targets bad aid in reverse-engineering of hardware in a more timely way.  This tool can be used in an interactive mode or from a Python 2.7 script.

1. Start RfCat in an interactive shell, plug the USB in first and run:
	```console
	rfcat -d
	```

For sample scripts, see the [rfcat_shell.py](https://github.com/DSUmjham/GenCyber/blob/master/SDR/rfcat_shell.py) skeleton scripting this repository.

## Resources
* [Audacity](https://github.com/audacity/audacity)
* [Digital Ding Dong Ditch](http://samy.pl/dingdong/) - Writeup on Sammy Kamkar's digital ding dong ditch project
* [dump1090-fa](https://github.com/adsbxchange/dump1090-fa)
* [FCCID.io](https://fccid.io) - Lookup a device in the FCC database to learn its frequency/modulation
* [Flightradar24](https://www.flightradar24.com/) - Live plane tracking map
* [Gqrx](http://gqrx.dk)
* [hak5](https://www.rtl-sdr.com/tag/hak5/) - good videos and tutorials on how to use your SDR once it's up and running.  Also has a store to buy some additional SDR gear or at least get ideas from.
* [Jared Boon - TPMS](https://github.com/jboone/tpms) - Jared Boon's GitHub page about analyzing/tracking TPMS sensors
* [Offensive Security](https://www.offensive-security.com/kali-linux-vm-vmware-virtualbox-image-download/) - link to pre-built Kali VM images.  Still will need to install the SDR software on top of these.
* [PiAware](https://flightaware.com/adsb/piaware/) - Set up flight tracking on a Pi.
* [RTL-SDR](https://www.rtl-sdr.com) - Ideas, projects, write-ups for using the RTLSDR.
