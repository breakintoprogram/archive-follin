#!/usr/bin/python3

# Title:		Formatter for Tatung Einstein Z80 SRC files
# Author:		Dean Belfield
# Created:		06/05/2023
# Last Updated:	06/05/2023
#
# Modinfo:

import sys
import os

# Open the file for reading
#
name = sys.argv[1]										# Get the filename
full_path = os.path.expanduser(name)					# Expand the full path to the file and
file = open(full_path, "rb")							# Open it up as a binary file

file_stdout = sys.stdout								# Store the current stdout file handle
sys.stdout = open(full_path + ".DTK", "w")				# Redirect stdout for the detokenised file output

col = 0			# Current column # (used for tabbing the listing)
comment = False	# Are we in a comment?
label = False	# Does this line contain a comment?
indent = 16		# Indent for first column
line = ""		# Storage for line

# Iterate through the file
#
while True:
	data = file.read(1)									# Read 1 byte into the buffer data
	if not data:										# If EOF then exit the loop
		break			
	byte = data[0]										# Fetch the byte 
	if byte == 0x1A:
		break
	asc = chr(byte)
	line += asc
	col += 1											# Increment the column number
	if asc == ";":										# Flag when in a comment
		comment = True
	if asc == ":" and not comment:						# If it is a colon (following a label) and not in comment then indent
		line += " "*(indent-col)						# Indent
		label = True	
	if byte == 0x0A:									# If it is CR then
		if not label:									# If this line doesn't contain a label
			line = (" "*indent) + line 					# Indent 
		print(line, end="")								# Print the line
		col = 0											# Reset the column to 0
		comment = False									# Reset the comment flag
		label = False									# Reset the label flag	
		line = ""										# Reset the line

file.close()											# We've done so close the files

sys.stdout.close()										# Close and restore stdout
sys.stdout = file_stdout
