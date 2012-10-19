import unittest
from tictactoe import runTheThing, parse_arguments, argparse

class TestsOnWinning(unittest.TestCase):
	def testIfWon(self):
		board, error = runTheThing("x+xo+oxox","o",1,1)
		assert board.won == True

	def testIfLost(self):
		board, error = runTheThing("x+xo+oxox","o",1,2)
		assert board.won == False

class TestInputs(unittest.TestCase):
	def testIfNoInput(self):
		board, error = runTheThing(None, None, None, None)
		assert error == "No board entered. Please enter one."

	def testIfCorrectInput(self):
		board, error = runTheThing("+++++++++","x",1,2)
		assert error == None

	def testIfNotXOrO(self):
		board, error = runTheThing("+++++++++","p",1,2)
		assert error == "You must place either an X or an O."

	def testIfInputTooShort(self):
		board, error = runTheThing("++++++++","x",1,2)
		assert error == "Input must be nine characters long (X, O and + allowed)."
		
	def testIfInputTooLong(self):
		board, error = runTheThing("+++++++++++","x",1,2)
		assert error == "Input must be nine characters long (X, O and + allowed)."

	def testIfInputNotXOOrHyphen(self):
		board, error = runTheThing("+++p+++++","x",1,2)
		assert error == "Input may only contain Xs, Os or +'s."

	def testIfCo_ordinateLessThan0(self):
		board, error = runTheThing("+++++++++","x",-1,2)
		assert error == "You have entered an invalid co-ordinate. They must all be 0, 1 or 2."

	def testIfCo_ordinateOver2(self):
		board, error = runTheThing("+++++++++","x",1,4)
		assert error == "You have entered an invalid co-ordinate. They must all be 0, 1 or 2."

	def testLetterInSamePlace(self):
		board, error = runTheThing("x++++++++","o",0,0)
		assert error == "There is already a letter in that position."

	def testForInvalidMove(self):
		board, error = runTheThing("x++++++++","x",0,1)
		assert error == "Invalid move entered (There can only be one more X than the number of Os, and vice versa)."

	def testForInvalidBoard(self):
		board, error = runTheThing("xx+++++++",None,None,None)
		assert error == "Invalid board entered (There can only be one more X than the number of Os, and vice versa)."

	def testIfStringEnteredAsCo_ordinate(self):
		board, error = runTheThing("+++++++++","X","faceplant",0)
		assert error == "Co-ordinate was not in the correct format. Please enter an integer."

class TestsOnFiles(unittest.TestCase):
	def setUp(self):
		self.parser = argparse.ArgumentParser()
		self.args = self.parser.parse_args()
		self.args.input = None
		self.args.place = None
		self.args.x = None
		self.args.y = None
		self.args.file = None
		self.args.new = False

	def testIfNewAndNoFile(self):
		self.args.new = True
		self.args.file = None
		this_board, error, using_file = parse_arguments(self.args)
		assert error == "No board entered. Please enter one."

	def testIfNoFileInLocationGiven(self):
		self.args.file = "nofile.txt"
		this_board, error, using_file = parse_arguments(self.args)
		assert error == "No board entered. Please enter one."

if __name__ == '__main__':
	unittest.main()