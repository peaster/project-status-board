# Project Status Board
Software driver to output HTTP response color codes to a WS8211 LED string. The hardware used as an example for the sake of this README is a Raspberry Pi and Neopixel LEDs. 


## Hardware Setup
* Install [Raspberry Pi OS Lite](https://www.raspberrypi.org/software/) on SD card
* [Enable Wi-Fi and SSH](https://medium.com/@danidudas/install-raspbian-jessie-lite-and-setup-wi-fi-without-access-to-command-line-or-using-the-network-97f065af722e)
* Install SD card and power up Raspberry Pi
* SSH into the Raspberry and configure password and timezones
	* `passwd`
	* `sudo raspi-config`
* Update packages 
	* `sudo apt-get update`
	* `sudo apt-get upgrade`
* Create a `hosts` file at the root of this repo and populate each URL you wish to poll on each line.
* Install python3 and pip3 if not already installed
	* `sudo apt-get install python3`
	* `sudo apt-get install python3-pip`
* Install required python libraries for the project
	* [Neopixel](https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage): `sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel`
* Attach WS8211 LEDs to Raspberry Pi, if you are using just a few, you can connect the directly, otherwise you may need to also attach external power to the LEDs. For my purpose with 22 powered LEDs it was fine to just connect it directly. You can find [more details about wiring here](https://learn.adafruit.com/neopixels-on-raspberry-pi/raspberry-pi-wiring).

## Set up as a systemd service		
To run the client permanently and to ensure it starts when you apply power to the Raspberry Pi, set up a service:

`sudo vim /etc/systemd/system/host-poller.service`
```
[Unit]
Description=host polling service

[Service]
ExecStart=python3 host-poller.py
WorkingDirectory=<THE LOCATION OF THIS REPO>
Restart=always
RestartSec=10
User=pi

[Install]
WantedBy=multi-user.target 
```
And then enable it
```
sudo systemctl enable mqtt-client.service
sudo systemctl start mqtt-client.service
```
