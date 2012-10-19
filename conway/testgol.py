import unittest
from gol import *

class TestsOnCreatingObjects(unittest.TestCase):
	def testCanCreateBoard(self):
		input_state = [(0,0)]
		board = Board(input_state,2,3)
		assert type(board) == Board

	def testCreatesCells(self):
		input_state = [(0,0)]
		board = Board(input_state,2,3)
		assert type(board.total_list[1][1]) == Cell

	def testCreatesCellsAsDead(self):
		input_state = [(0,0)]
		board = Board(input_state,2,3)
		assert board.total_list[1][1].state == 0

	def testChangesInputCellsToLive(self):
		input_state = [(1,1)]
		board = Board(input_state,2,3)
		assert board.total_list[1][1].state == 1

	def testListOfCellsToCheckIsComplete(self):
		input_state = [(1,1)]
		board = Board(input_state,4,4)
		assert board.list_to_check == [(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)]

	def testNewBoardIsCorrect(self):
		input_state = [(1,1),(1,2),(2,1),(2,2)] # Using a block.
		board = Board(input_state,4,4)
		assert board.return_new_board() == [(1,1),(1,2),(2,1),(2,2)]

	def testUnderpopulatedCellDies(self):
		input_state = [(1,1),(0,1)]
		board = Board(input_state,4,4)
		output_state = board.return_new_board()
		assert (1,1) not in output_state

	def testOverPopulatedCellDies(self):
		input_state = [(1,1),(0,1),(2,1),(1,0),(1,2)]
		board = Board(input_state,4,4)
		output_state = board.return_new_board()
		assert (1,1) not in output_state

	def testDeadCellComesAlive(self):
		input_state = [(0,1),(2,1),(1,0)]
		board = Board(input_state,4,4)
		output_state = board.return_new_board()
		assert (1,1) in output_state

	def testCellStaysAsItWas(self):
		input_state = [(1,1),(0,1),(2,1),(1,0)]
		board = Board(input_state,4,4)
		output_state = board.return_new_board()
		assert (1,1) in output_state and (1,1) in input_state

if __name__ == '__main__':
	unittest.main()