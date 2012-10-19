#!/usr/bin/python

# Import the argparse module to deal with command line arguments.
import argparse

def main():
	# Take in an argument at the command line.
	parser = argparse.ArgumentParser(description='Enter the argument on which to run the script.')
	parser.add_argument('argument',
	                   help='Enter the argument on which to run the factorial function (must be an integer).')
	args = parser.parse_args()

	number = parse_argument(args.argument)

	# Makes sure the factorial function isn't called if a non-integer has been input.
	if number != "Argument must be an integer.":	
		result = factorial(number)
		print result
	else:
		print number

# Parses the input from a string to an integer, and throws an error if it's impossible.
def parse_argument(inputted):
	try:
		outputted = int(inputted)
		return outputted
	except ValueError:
		return "Argument must be an integer."

# Does the factorial function and outputs the result.
def factorial(number):
	result = 1
	if number < 0:
		return "The argument cannot be less than zero."
	else:
		while number > 0:
			result = result * number
			number = number - 1
		return result

if __name__ == '__main__':
	main()