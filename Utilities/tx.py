#!/usr/bin/python3

# Title:		RS-232 TX (PC -> Tatung) Transfer Utility
# Author:		Dean Belfield
# Created:		03/05/2023
# Last Updated:	03/05/2023
#
# Modinfo:

import serial
import sys

# Configure serial port here. Last parameter is timeout to stop reading data, in seconds: 

s = serial.Serial('/dev/ttyUSB1', 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_TWO, 15)

name = sys.argv[1] if len(sys.argv) > 1 else 'output.file'
print("Opening file ", name)
f = open(name, 'rb')

print("Transferring PC -> Tatung")
data = f.read()
if data:
   count = s.write(data)

f.close()
print("\nTransfer ended, bytes sent: ", count)
