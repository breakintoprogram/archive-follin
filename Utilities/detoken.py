#!/usr/bin/python3

# Title:		Decoder for Tatung Einstein 6502 SRC files
# Author:		Dean Belfield
# Created:		29/04/2023
# Last Updated:	05/05/2023
#
# Modinfo:
# 04/05/2023:	Added bounds checking on the tokens array
# 05/05/2023:	Fixed python indenting, tweaked error handling

import sys
import os

# Array of tokenised keywoards
#
tokens = [
	"ADC",	# 0x00
	"AND",
	"ASL",
	"BNE",
	"BEQ",
	"BCC",
	"BCS",
	"BIT",
	"BMI",
	"BPL",
	"BRK",
	"BVC",
	"BVS",
	"CLC",
	"CMP",
	"CPX",
	"CPY",	# 0x10
	"CLD",
	"CLI",
	"CLV",
	"DEC",
	"DEX",
	"DEY",
	"DB",
	"DW",
	"DS",
	"DC",
	"DBH",
	"DBB",
	"DCW",
	"EQU",
	"EOR",
	"END",	# 0x20
	"ELSE",
	"FROM",
	"FIN",
	"INC",
	"INX",
	"INY",
	"INCL",
	"IF",
	"JSR",
	"JMP",
	"KEY",
	"LDA",
	"LDX",
	"LDY",
	"LSR",
	"LOAD",	# 0x30
	"LEN",
	"NOP",
	"ORA",
	"ORG",
	"PHA",
	"PLA",
	"PHP",
	"PLP",
	"RTS",
	"ROL",
	"ROR",
	"RTI",
	"SBC",
	"STA",
	"STX",
	"STY",	# 0x40
	"SEC",
	"SED",
	"SEI",
	"SYM",
	"SEND",
	"TAX",
	"TAY",
	"TXA",
	"TXS",
	"TYA",
	"TSX",
	"TO",
	"WAIT",
	"*?*",
	"*?*",
	"*?*",	# 0x50
	"ADD",	# 0x51 - Pseudo instruction
	"SUB",	# 0x52 - Pseudo instruction
]

tokens_len = len(tokens)								# Length of tokens list

# Open the file for reading
#
name = sys.argv[1]										# Get the filename
full_path = os.path.expanduser(name)					# Expand the full path to the file and
file = open(full_path, "rb")							# Open it up as a binary file

file_stdout = sys.stdout								# Store the current stdout file handle
sys.stdout = open(full_path + ".DTK", "w")				# Redirect stdout for the detokenised file output

col = 0			# Current column # (used for tabbing the listing)
indent = 16		# Indent for first column

# Iterate through the file
#
while True:
	data = file.read(1)									# Read 1 byte into the buffer data
	if not data:										# If EOF then exit the loop
		break		
	byte = data[0]										# Fetch the byte 
	if byte == 0x0D:									# If it is CR then
		col = 0											# Reset the column to 0
		print("")										# Print a CR
	elif byte == 0x1A:									# If it is EOF the
		break;											# Exit the loop
	elif byte < 0x8A:									# If it is a printable character
		asc = chr(byte)									# Get the ASCII character
		print(asc, end="")								# Print it
		col += 1										# Increment the column number
		if(asc == ":"):									# If it is a colon (following a label) then tab to the column specified by indent
			print(" "*(indent-col), end="")		
	else:												# Otherwise try to detokenise
		if(col == 0):									# If we are at the first column, then it's a token without a label
			print(" "*indent, end="")					# Tab to the column specified by indent
		byte -= 0x8A									# Get index into array
		if(byte < tokens_len):							# Check bounds
			token = tokens[byte]						# Fetch the token from the tokens table
			token += " "*(5-len(token))					# Pad it to fit into 5 characters
		else:											# Otherwise
			token = "<UNKNOWN " + hex(byte+0x8A) + ">"	# It's an invalid token output this
		print(token, end="")							# Print it
		col += len(token)								# Adjust column by the width of the token

file.close()											# We've done so close the files

sys.stdout.close()										# Close and restore stdout
sys.stdout = file_stdout
