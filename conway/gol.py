from os import system
import time

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

def main():
	# Set one of the below to be called 'input_state', then watch it go!
	glider = [(2,3),(4,3),(3,4),(4,4),(3,5)]
	two_gliders_same_track = [(2,3),(4,3),(3,4),(4,4),(3,5),(10,11),(12,11),(11,12),(12,12),(11,13)]
	two_gliders_vertical = [(7,3),(9,3),(8,4),(9,4),(8,5),(2,3),(4,3),(3,4),(4,4),(3,5)]
	toad = [(1,1),(2,1),(3,1),(0,2),(1,2),(2,2)]
	blinker = [(1,1),(2,1),(3,1)]
	block = [(1,1),(2,1),(1,2),(2,2)]
	lightweight_spaceship = [(2,2),(5,2),(6,3),(2,4),(6,4),(3,5),(4,5),(5,5),(6,5)]
	figure_of_8 = [(3,3),(4,3),(5,3),(3,4),(4,4),(5,4),(3,5),(4,5),(5,5),(6,6),(7,6),(8,6),(6,7),(7,7),(8,7),(6,8),(7,8),(8,8)]
	glider_gun_vertical = [(2,6),(3,6),(2,7),(3,7),(12,6),(12,7),(12,8),(13,5),(13,9),(14,4),(14,10),(15,4),(15,10),(16,7),(17,5),(17,9),(18,6),(18,7),(18,8),(19,7),(22,4),(22,5),(22,6),(23,4),(23,5),(23,6),(24,3),(24,7),(26,2),(26,3),(26,7),(26,8),(36,4),(36,5),(37,4),(37,5)]
	input_state = [(6,2),(6,3),(7,2),(7,3),(6,12),(7,12),(8,12),(5,13),(9,13),(4,14),(10,14),(4,15),(10,15),(7,16),(5,17),(9,17),(6,18),(7,18),(8,18),(7,19),(4,22),(5,22),(6,22),(4,23),(5,23),(6,23),(3,24),(7,24),(2,26),(3,26),(7,26),(8,26),(4,36),(5,36),(4,37),(5,37)]
	
	while True:
		# Board takes in the input state and the size of the board (x,y)
		board = Board(input_state,60,60)
		input_state = board.return_new_board()
		board.print_board()
		time.sleep(0.1)

if __name__ == '__main__':
	main()