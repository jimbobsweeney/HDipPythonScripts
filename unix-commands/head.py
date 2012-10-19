#!/usr/bin/python

def main():
	# Import argparse and add all the arguments. Also import 'exit' to exit if there
	# is an error.

	import argparse
	from sys import exit

	parser = argparse.ArgumentParser()
	parser.add_argument("files", nargs="+", help="Enter the file path on which to run the command.")
	parser.add_argument("-v","--verbose", action = "store_true", help = "Always print headers giving file names.")
	parser.add_argument("-q","--quiet","--silent", action = "store_true", help = "Never print headers giving file names.")
	parser.add_argument("-n","--lines", action = "store", help = "Print the first N lines of the file(s).")
	parser.add_argument("-c","--bytes", action = "store", help = "Print the first N bytes of the file(s).")
	args = parser.parse_args()

	# Filenames can be either given all the time (verbose), none of the time (quiet)
	# or if there's more than one file (normal).
	if args.verbose:
		filenames = "verbose"
	elif args.quiet:
		filenames = "quiet"
	else:
		filenames = "normal"

	# Files are scanned by lines or by bytes, with the number of each able to be
	# customised by passing the appropriate flag. 
	# Error handling included for if a non-integer is passed to the -n or -c flags.
	if args.lines:
		scan_type = "lines"
		try:
			numLines = int(args.lines)
		except ValueError:
			print "Illegal argument: must be an integer."
			exit()
	elif args.bytes:
		try:
			scan_type = "bytes"
			numBytes = int(args.bytes)
		except ValueError:
			print "Illegal argument: must be an integer."
			exit()
	else:
		scan_type = "lines"
		numLines = 10

	# The text from each of the files is put into a list within a dictionary.
	# By doing this, only one line of the file is in memory at a time.
	text = {}
	for file in args.files:
		this_file = open(file)
		text[file] = []
		
		if scan_type == "bytes":
			byte = 0
			while byte < numBytes:
				text[file].append(this_file.readline(numBytes-1))
				byte = this_file.tell()
		else:
			line = 0
			while line < numLines:
				text[file].append(this_file.readline())
				line += 1
		this_file.close()

	# Calls the decorate_filenames function at the start of each file, then
	# prints the relevant lines.
	for file in args.files:
		decorate_filenames(filenames, file, args)
		for line in text[file]:
			print line,
		print "\n",

# Puts the filename in where appropriate.
def decorate_filenames(filenames, file, args):
	if filenames == "verbose" or (filenames == "normal" and len(args.files) > 1):
		print "==> %s <==" % file

if __name__ == '__main__':
	main()