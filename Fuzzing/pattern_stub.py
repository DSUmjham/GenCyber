#! /usr/bin/python
import sys

# ***** INSERT BUF VARIABLE HERE *****

def printHelp():
	print "Usage Instructions:\n--------------------"
	print "\nTo create an offset, use the following (int is the number of bytes to generate):"
	print sys.argv[0] + " create <int>"
	print "\nTo find an offset, use the following command (must be at least 3 chars):"
	print sys.argv[0] + " offset <offset>"
	print "\nIf your offset is > 20280 bytes, you must specify how many bytes you used to generate the pattern:"
	print sys.argv[0] + "offset <offset> <int>"


def printPattern(size):
	# ***** FINISH ME *****

def decode_offset(offset):
	# ***** FINISH ME *****

def findOffset(offset, size):
	try:
		# ***** FINISH ME *****
	except ValueError:
			print "Offset not found."


if __name__ == "__main__":
	if len(sys.argv) < 3: # make sure the user enters in the correct number of parameters
		printHelp()
	elif sys.argv[1] != "create" and sys.argv[1] != "offset": # they had the right number of parameters, but were they right?
		printHelp()

	try: 
		if sys.argv[1] == "create" and sys.argv[2].isdigit(): # if they are creating a pattern, the second param needs to be a number
			printPattern(sys.argv[2])
	except IndexError:
		"To trim the pattern, you must specify an integer value."

	try:
		if sys.argv[1] == "offset" and sys.argv[2]: # if the user is calculating an offset, check the number and tyep of params
			try:
				size = int(sys.argv[3])
			except IndexError:
				size = 0

			findOffset(sys.argv[2], size)
			
	except IndexError:
		print ("If your fuzzing string was > 20280, you must specify size.")
