#!/usr/bin/python3

# Title:		PySerial wrapper
# Author:		Dean Belfield
# Created:		04/02/2025
# Last Updated:	04/02/2025
#
# Modinfo:

import serial
import time

# Class to wrap the serial port
#
class RS232:
	def __init__(self, port, baudrate, bytesize, parity, stopbits, timeout = None):
		self.serial = serial.Serial(port, baudrate, bytesize, parity, stopbits, timeout)

	def writeByte(self, b):
		self.write(bytes([b]))

	def write(self, data):
		while True:
			if self.serial.cts:
				break
		count = self.serial.write(data)
		time.sleep(0.001)
		return count 
	
	def read(self):
		return self.serial.read()

	def close(self):
		self.serial.close()