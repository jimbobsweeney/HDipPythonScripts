#!/usr/bin/python

# Imports the Regular Expressions library and the ability to check if the file exists.
import re
from os.path import exists

def main():
	# Checks if the file exists, and displays an error message if not.
	if exists("austinpowers.txt"):
		# Opens the file, reads it, and finds the number of occurrences of the word 'groovy'.
		ap = open("austinpowers.txt")
		aptext = ap.read()
		matches = re.findall(r"groovy", aptext.lower())
		occurrences = len(matches)

		# Closes the file and prints the result to the screen.
		ap.close()
		print "There are %d occurrences of the word 'groovy' in the Austin Powers script."\
		% occurrences
	else:
		print "There is no austinpowers.txt file in this directory."

if __name__ == '__main__':
	main()