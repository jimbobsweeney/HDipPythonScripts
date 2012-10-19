import unittest
from factorial import *

# Test the factorial function with positive, zero and negative integers.
class TestFactorial(unittest.TestCase):
	def testPositive(self):
		assert factorial(5) == 120, "Failed on 5."

	def testZero(self):
		assert factorial(0) == 1, "Failed on 0."

	def testNegative(self):
		result = factorial(-1)
		assert result == "The argument cannot be less than zero."

# Test the argument parser can handle inputs that are not integers.
class TestParseArgument(unittest.TestCase):
	def testStringInput(self):
		result = parse_argument("fish")
		assert result == "Argument must be an integer."

	# I was going to test for input of floats here, but arguments from the
	# command line come in as strings, so it is covered by the above test.

if __name__ == '__main__':
	unittest.main()