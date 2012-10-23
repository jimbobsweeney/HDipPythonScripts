#!/usr/bin/python

from os import system
import time
import argparse
from os.path import exists
import csv
from sys import exit

class Cell(object):
	"""A cell on the board"""
	def __init__(self):
		# State is 0 if the cell is dead or 1 if it is alive.
		self.state = 0
		self.newstate = 0

class Board(object):
	"""The board where the game takes place"""
	def __init__(self,old_board,xsize,ysize):
		# Create a 2d array (called total_list), with all items set to 0.
		self.xsize = xsize
		self.ysize = ysize
		self.list_to_check = []
		self.total_list = []
		for x in range(0,xsize):
			row_cells = []
			for y in range(0,ysize):
				this_cell = Cell()
				row_cells.append(this_cell)
			self.total_list.append(row_cells)

		# Calls the other functions to progress the game one iteration.
		self.establish_old_board(old_board)
		self.establish_list_of_cells_to_check()
		self.check_rules()

	# Pulls in the old board and sets all the cells mentioned to be alive.
	def establish_old_board(self,old_board):
		for x, y in old_board:
			self.total_list[x][y].state = 1

	# Adds the live cells and the cells that touch them to the list_to_check.
	def establish_list_of_cells_to_check(self):
		for x in range(0,self.xsize):
			for y in range(0,self.ysize):
				if self.total_list[x][y].state == 1:
					list_to_add = [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x,y),\
						(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]

					# Removes cells from the list_to_check if they would be off the board.
					list_to_remove = []
					for a, b in list_to_add:
						if a < 0 or b < 0 or a > self.xsize-1 or b > self.ysize-1:
							list_to_remove.append((a,b))
					
					for item in list_to_remove:
						if item in list_to_add:
							list_to_add.remove(item)

					# Doesn't add the cell to the list if it's already there.
					for item in list_to_add:
						if item not in self.list_to_check:
							self.list_to_check.append(item)
			
	def check_rules(self):
		# Establish a list of the cells around the one we're checking.
		for x, y in self.list_to_check:
			if x == 0:
				xlow = self.xsize - 1
			else:
				xlow = x-1

			if x == self.xsize-1:
				xhigh = 0
			else:
				xhigh = x+1

			if y == 0:
				ylow = self.ysize - 1
			else:
				ylow = y-1

			if y == self.ysize-1:
				yhigh = 0
			else:
				yhigh = y+1

			list_to_add = [(xlow,ylow),(x,ylow),(xhigh,ylow),(xlow,y),\
						(xhigh,y),(xlow,yhigh),(x,yhigh),(xhigh,yhigh)]

			# Using the .state attribute of each Cell, find out how many of its neighbours are alive.
			alive_neighbours = 0
			for a,b in list_to_add:
				alive_neighbours = alive_neighbours + self.total_list[a][b].state

			# Set the .newstate according to the rules of the Game of Life.
			if (alive_neighbours < 2 or alive_neighbours > 3) and self.total_list[x][y].state == 1:
				self.total_list[x][y].newstate = 0
			elif alive_neighbours == 3 and self.total_list[x][y].state == 0:
				self.total_list[x][y].newstate = 1
			else:
				self.total_list[x][y].newstate = self.total_list[x][y].state

	# Sets the .newstate to the .state and returns an array of tuples
	# representing the live cells for use as the input state of the next iteration.
	def return_new_board(self):
		for row in self.total_list:
			for cell in row:
				cell.state = cell.newstate

		output_state = []
		for x in range(0,self.xsize):
			for y in range(0,self.ysize):
				if self.total_list[x][y].state == 1:
					this_tuple = (x,y)
					output_state.append(this_tuple)
		return output_state

	# Clears the screen and prints the board, giving the illusion of animation.
	def print_board(self):
		system('clear')

		for x in self.total_list:
			for y in x:
				if y.state == 1:
					print '+',
				else:
					print ' ',
			print "\n",

# Checks that the CSV file exists, and converts it to a list of tuples if it does.
# If it doesn't, it returns an error message. Also returns an error message if
# the CSV file is corrupted.
def parse_csv(args):
	if exists(args.file):
		csvfile = open(args.file, "rb")
		reader = csv.reader(csvfile)
		grand_list = []
		for line in reader:
			try:
				new_line = map(int,line)
			except Exception, e:
				return "The CSV file is corrupted."

			new_line = tuple(new_line)
			grand_list.append(new_line)

		csvfile.close()
		return grand_list
	else:
		return "There is no file in that location."

def main():
	# Takes in the CSV file as an argument.
	parser = argparse.ArgumentParser()
	parser.add_argument("file", help="Enter the CSV file path from which to start the game.")
	args = parser.parse_args()

	input_state = parse_csv(args)
	
	# Exits with an error message if there is no file.
	if type(input_state) == str:
		print input_state
		exit(-1)
	
	while True:
		# Board takes in the input state and the size of the board (x,y)
		board = Board(input_state,40,40)
		input_state = board.return_new_board()
		board.print_board()
		time.sleep(0.1)

if __name__ == '__main__':
	main()