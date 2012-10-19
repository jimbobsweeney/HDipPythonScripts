#!/usr/bin/python

def main():
	# Import argparse and add all the arguments. Also imports 'time' to run the
	# loop for the -f flag.

	import argparse
	import time

	# Adds arguments for -v,-q and -f. I wanted to do -n and -c too, but wasn't
	# happy with how they worked for lengths greater than one chunk (see below).
	parser = argparse.ArgumentParser()
	parser.add_argument("files", nargs="+", help="Enter the file path on which to run the command.")
	parser.add_argument("-v","--verbose", action = "store_true", help = "Always print headers giving file names.")
	parser.add_argument("-q","--quiet","--silent", action = "store_true", help = "Never print headers giving file names.")
	# parser.add_argument("-n","--lines", action = "store", help = "Print the first N lines of the file(s).")
	# parser.add_argument("-c","--bytes", action = "store", help = "Print the first N bytes of the file(s).")
	parser.add_argument("-f","--follow", action = "store_true", help = "Output appended data as the file grows.")
	args = parser.parse_args()

	# Filenames can be either given all the time (verbose), none of the time (quiet)
	# or if there's more than one file (normal).
	if args.verbose:
		filenames = "verbose"
	elif args.quiet:
		filenames = "quiet"
	else:
		filenames = "normal"

	# Runs the function every second to check on the files if the -f flag is passed.
	if args.follow:
		while True:
			run_tail(args,filenames)
			time.sleep(1)
	else:
		run_tail(args,filenames)


def run_tail(args,filenames):	
	numLines = 10
	chunk_size = 512
	
	text = {}
	for file in args.files:
		this_file = open(file)
		text[file] = []
		
		# Goes to the end of the file, then seeks back in 512 byte chunks.
		# Puts the resulting text into a list and removes unwanted lines.
		# They have to be reversed so that we chop off the appropriate lines.
		cumulative_lines = 0
		this_file.seek(0,2)
		full_size = this_file.tell()
		if full_size < chunk_size:
			chunk_size = full_size
		while cumulative_lines < numLines:
			this_file.seek(-chunk_size,1)
			start_position = this_file.tell()
			chunk_string = this_file.read(chunk_size)
			chunk_lines = chunk_string.split('\n')
			chunk_lines.reverse()
			cumulative_lines += len(chunk_lines)
			this_file.seek(start_position) # Rewinds it for the next chunk.
			
			if numLines < cumulative_lines:					
				for i in range(0,(cumulative_lines - numLines)):
					chunk_lines.pop()

			# Files are kept in a dictionary of lists.
			for oneline in chunk_lines:
				text[file].append(oneline)
	
		this_file.close()

	# Calls the decorate_filenames function at the start of each file, then
	# prints the relevant lines.
	for file in args.files:
		text[file].reverse()
		decorate_filenames(filenames, file, args)
		for line in text[file]:
			print line
		print "\n",

# Puts the filename in where appropriate.
def decorate_filenames(filenames, file, args):
		if filenames == "verbose" or (filenames == "normal" and len(args.files) > 1):
			print "==> %s <==" % file

if __name__ == '__main__':
	main()