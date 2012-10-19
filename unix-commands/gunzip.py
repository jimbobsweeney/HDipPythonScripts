#!/usr/bin/python

# Argparse used in main function. Gzip used in the gunzip_file function.
import argparse
import gzip

def main():
	# Add the files as arguments and the -c flag to print to the screen.
	parser = argparse.ArgumentParser()
	parser.add_argument("files", nargs="+", help="Enter the files on which to run the command.")
	parser.add_argument("-c", action = "store_true", help = "Print the contents of the gunzipped file out.")
	args = parser.parse_args()

	# If the -c flag is passed, the program only prints the contents. If not, it unzips the file.
	if args.c:
		for file in args.files:
			to_gunzip, file_for_writing = gunzip_file(file)
			print_contents(to_gunzip)
	else:
		for file in args.files:
			to_gunzip, file_for_writing = gunzip_file(file)
			gunzip_to_file(file, to_gunzip, file_for_writing)

# Unzips the file.
def gunzip_file(file):
    to_gunzip = gzip.GzipFile(file, 'r')
    file_for_writing = str(file).rstrip('.gz')
    return to_gunzip,file_for_writing
    
# Writes the unzipped contents to a file and saves it.
def gunzip_to_file(file, to_gunzip,file_for_writing):
	gunzipped = open(file_for_writing, 'w')
	gunzipped.write(to_gunzip.read())
	gunzipped.close()
	to_gunzip.close()
	print "%s has been unzipped." % file

# Prints the unzipped contents to the screen.
def print_contents(to_gunzip):
	contents = to_gunzip.read()
	print contents
	to_gunzip.close()

if __name__ == '__main__':
	main()