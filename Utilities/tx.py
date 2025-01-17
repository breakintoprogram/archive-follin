#!/usr/bin/python3

# Title:		RS-232 TX (PC -> Tatung) Transfer Utility
# Author:		Dean Belfield
# Created:		03/05/2023
# Last Updated:	15/01/2025
#
# NB:
# This must be used in conjunction with the BBC BASIC for Z80 program TRANSFER.BBC on the Tatung Einstein side
#
# Modinfo:
# 15/01/2025:	Added handshaking

import serial
import sys
import time
import os

def writeByte(b):
	while True:
		s = serial.Serial('/dev/ttyUSB0', 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_TWO)
		if s.getCTS():
			break
		s.close()
	count = s.write(b)
	s.close()
	return count

name = sys.argv[1] if len(sys.argv) > 1 else 'output.file'
size = os.path.getsize(name)
print("Opening file ", name)
f = open(name, 'rb')

print(f"Transferring PC -> Tatung")
print(f"Sending {size} bytes")

count = 0

writeByte(bytes([size%256]))
writeByte(bytes([int(size/256)]))

if size > 0:
	while True:
		data = f.read(1)
		count += writeByte(data)
		if count % 256 == 0:
			sys.stdout.write(".")
			sys.stdout.flush()	
		if count == size:
			break

f.close()
print(f"\nTransfer ended, bytes sent: {count}")

