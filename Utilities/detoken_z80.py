#!/usr/bin/python3

# Title:		Decoder for Tatung Einstein Z80 SRC files
# Author:		Dean Belfield
# Created:		17/01/2025
# Last Updated:	18/01/2025
#
# Modinfo:
# 18/01/2025:	Fixed end of file bug and tokens in comments

import sys
import os

# Array of tokenised keywoards
#
tokens = [
	"ADD",
	"AND",
	"ADC",
	"BIT",
	"CALL",
	"CP",
	"CCF",
	"CPL",
	"CPI",
	"CPIR",
	"CPD",
	"CPDR",
	"DEC",
	"DJNZ",
	"DAA",
	"DB",
	"DW",
	"DS",
	"DC",
	"DBH",
	"DBB",
	"DCW",
	"DI",
	"EQU",
	"EX",
	"EXX",
	"EI",
	"END",
	"ELSE",
	"FIN",
	"FROM",
	"HALT",
	"INC",
	"IM",
	"IN",
	"INI",
	"INIR",
	"IND",
	"INDR",
	"INCL",
	"IF",
	"JR",
	"JP",
	"KEY",
	"LD",
	"LDIR",
	"LDI",
	"LDD",
	"LDDR",
	"LOAD",
	"LEN",
	"NOP",
	"NEG",
	"OR",
	"OUT",
	"OUTI",
	"OTIR",
	"OUTD",
	"OTDR",
	"ORG",
	"PUSH",
	"POP",
	"RET",
	"RST",
	"RES",
	"RL",
	"RLC",
	"RLCA",
	"RLA",
	"RR",
	"RRC",
	"RRCA",
	"RRA",
	"RLD",
	"RRD",
	"RETI",
	"RETN",
	"SBC",
	"SUB",
	"SCF",
	"SLA",
	"SRA",
	"SRL",
	"SET",
	"SYM",
	"SEND",
	"TO",
	"WAIT",
	"XOR",
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
comment = False	# Are we in a comment?
indent = 16		# Indent for first column
bracket = 0		# Should be zero at the end of an expression

# Iterate through the file
#
while True:
	data = file.read(1)									# Read 1 byte into the buffer data
	if not data:										# If EOF then exit the loop
		break		
	byte = data[0]										# Fetch the byte 
	if byte == 0x0D:									# If it is CR then
		if(bracket > 0):								# If we need to close the brackets then do so
			print(")", end="")
		col = 0											# Reset the column to 0
		comment = False									# Reset the comment flag
		bracket = 0										# Reset the bracket balance counter 
		print("")										# Print a CR
	elif byte == 0x1A or byte = 0xFF:					# If it is EOF the
		break;											# Exit the loop
	elif byte < 0x8A or comment:						# If it is a printable character or we are in a comment
		asc = chr(byte)									# Get the ASCII character
		if asc == "," and not comment and bracket > 0:	# Do we need to insert a bracket
			print(")", end="")
			bracket -=1
		print(asc, end="")								# Print it
		col += 1										# Increment the column number
		if asc == ";":									# Flag when in a comment
			comment = True
		if not comment:									# These only apply when not in comments
			if asc == ":":								# If it is a colon (following a label) then indent
				print(" "*(indent-col), end="")		
			elif asc == "(":							# Update the bracket balancing counter
				bracket += 1
			elif asc == ")":
				bracket -=1
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
