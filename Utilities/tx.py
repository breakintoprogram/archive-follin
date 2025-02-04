#!/usr/bin/python3

# Title:		RS-232 TX (PC -> Tatung) Transfer Utility
# Author:		Dean Belfield
# Created:		03/05/2023
# Last Updated:	04/02/2025
#
# NB:
# This must be used in conjunction with the BBC BASIC for Z80 program TRANSFER.BBC on the Tatung Einstein side
#
# Modinfo:
# 15/01/2025:	Added handshaking
# 04/02/2025:	Moved common serial code into libSerial

import sys
import os

import libSerial	# In this folder, libSerial.py

# Change this to your serial port
#
port = '/dev/ttyWCH0'

# Configure serial port here. Last parameter is timeout to stop reading data, in seconds: 
#
s = libSerial.RS232(port, 9600, 8, "N", 2)

name = sys.argv[1] if len(sys.argv) > 1 else 'output.file'
size = os.path.getsize(name)
print("Opening file ", name)
f = open(name, 'rb')

print(f"Transferring PC -> Tatung")
print(f"Sending {size} bytes")

count = 0

s.writeByte(size%256)
s.writeByte(int(size/256))

if size > 0:
	while True:
		data = f.read(1)
		count += s.write(data)
		if count % 256 == 0:
			sys.stdout.write(".")
			sys.stdout.flush()	
		if count == size:
			break

f.close()
s.close()

print(f"\nTransfer ended, bytes sent: {count}")

