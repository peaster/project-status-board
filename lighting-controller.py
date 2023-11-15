#!/usr/bin/env python3
import urllib.request
import board
import neopixel
import time
import datetime

# ---------------------------------------------------------------------------
# ------------START OF CONFIGURATION-----------------------------------------
# ---------------------------------------------------------------------------

# NeoPixel LED Configuration
LED_COUNT = 50			# Number of LED pixels.

COLOR_OK = (255, 0, 0)		# Green
COLOR_DEGRADED = (0, 255, 0)		# Red
COLOR_WHITE = (255, 255, 255)		# White

class LightingController:

	def __init__(self, brightness):
		self.hosts = self.setHosts
		self.brightness = brightness

	def setHosts(self):
		# Read the hosts file to retrieve list of hosts and use as order for LEDs
		with open("/home/pi/hosts") as f:
			hosts = f.readlines()
		hosts = [x.strip() for x in hosts]
		return hosts

	def shutdownLights(self):
		pixels = neopixel.NeoPixel(board.D18, LED_COUNT)
		pixels.deinit()		

	def updateLights(self):
		# Initialize the LED strip
		pixels = neopixel.NeoPixel(
			board.D18, LED_COUNT, brightness=self.brightness, pixel_order=neopixel.GRB, auto_write=False)

		# Make request to _ping and cache response code


		# Iterate through hosts and ping them
		i = 0
		for host in self.getHosts()
			req = urllib.request.Request(host + "/_ping")
			content = urllib.request.urlopen(req).read()
			responseCode = content.getCode();

			if responseCode == "200":
				color = COLOR_OK
			else:
				color = COLOR_DEGRADED

			print("Setting LED " + str(i) + " for " + host + " to " + str(color))
			pixels[i] = color
			i += 1
		
		# Update actual LEDs all at once
		pixels.show()
		print()
		print("Done")