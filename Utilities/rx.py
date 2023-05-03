#!/usr/bin/python3

# Title:		RS-232 RX (Tatung -> PC) Transfer Utility
# Author:		Andy Toone
# Modified By:	Dean Belfield
# Created:		03/05/2023
# Last Updated:	03/05/2023
#
# Modinfo

import serial
import sys

# Configure serial port here. Last parameter is timeout to stop reading data, in seconds: 
#
s = serial.Serial('/dev/ttyUSB1', 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_TWO, 15)

name = sys.argv[1] if len(sys.argv) > 1 else 'output.file'
print("Opening file: ", name)
f = open(name, 'wb')

print("Transferring Tatung -> PC")
count = 0

while True:
   res = s.read()
   if len(res)==0:
      break
   count += len(res)
   if count % 256 == 0:
     sys.stdout.write(".")
     sys.stdout.flush()
   f.write(res)

f.close()
print("\nTransfer ended, bytes received: ", count)
