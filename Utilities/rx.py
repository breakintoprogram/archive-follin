#!/usr/bin/python3

# Title:		RS-232 RX (Tatung -> PC) Transfer Utility
# Author:		Andy Toone
# Modified By:	Dean Belfield
# Created:		03/05/2023
# Last Updated:	04/02/2025
#
# NB:
# Use "COPY file TO SRL:<O>" on the Tatung to transfer files to PC
#
# Modinfo
# 04/02/2025:	Moved common serial code into libSerial

import sys

import libSerial	# In this folder, libSerial.py

# Change this to your serial port
#
port = '/dev/ttyWCH0'

# Configure serial port here. Last parameter is timeout to stop reading data, in seconds: 
#
s = libSerial.RS232(port, 9600, 8, "N", 2, 15)

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
s.close()

print("\nTransfer ended, bytes received: ", count)
