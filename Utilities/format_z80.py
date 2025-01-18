#!/usr/bin/python3

# Title:		Formatter for Tatung Einstein Z80 SRC files
# Author:		Dean Belfield
# Created:		06/05/2023
# Last Updated:	18/01/2025
#
# Modinfo:
# 06/05/2023:	Tweaked for comments on first line, and file EOL
# 16/11/2024:	Fixed for Windows line endings
# 18/01/2025:	Fixed for Linux line endings and end of file

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
string = False	# Are we in a string?
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
	if byte == 0x1A or byte == 0xFF:					# If EOF then exit the loop
		break
	asc = chr(byte)
	line += asc
	col += 1											# Increment the column number
	if asc == ";":										# Flag when in a comment or string literal
		comment = True
	if asc == '"':
		string = not string
	if asc == ":" and not comment and not string:		# If it is a colon (following a label) and not in comment or string then indent
		line += " "*(indent-col)						# Indent
		label = True	
	if byte == 0x0D:									# If it is LF then
		if not label and line[0] != ";":				# If this line doesn't contain a label and the first character isn't a comment
			line = (" "*indent) + line 					# Indent 
		print(line, end="")								# Print the line
		col = 0											# Reset the column to 0
		comment = False									# Reset the comment flag
		label = False									# Reset the label flag	
		line = ""										# Reset the line

file.close()											# We've done so close the files

sys.stdout.close()										# Close and restore stdout
sys.stdout = file_stdout
