#!/usr/bin/python

# Import the argparse module to parse arguments and the exists command.
import argparse
from os.path import exists

# Parses the arguments and calls the method to run the game.
def main():
	parser = argparse.ArgumentParser(description='Enter the details of the game.')
	parser.add_argument('--input', action='store',
	                   help='Enter the pattern at the start of the game.')
	parser.add_argument('--place', action='store',
	                   help='Enter the letter to place (X or O).')
	parser.add_argument('-x', action='store',
	                   help='Enter the X co-ordinate for your letter (0 for left column, 1 for middle, 2 for right).')
	parser.add_argument('-y', action='store',
	                   help='Enter the Y co-ordinate for your letter (0 for top row, 1 for middle, 2 for bottom).')
	parser.add_argument('--file', action='store',
						help='Enter a file to read a game board from.')
	parser.add_argument('-n', '--new', action='store_true',
						help='Sets up a new game, to be stored in the file specified with --file.')

	args = parser.parse_args()

	# Calls the parse_arguments function which validates the arguments given.
	this_board, error, using_file = parse_arguments(args)
	
	# Error message.
	if error:
		using_file = False
		print error
	
	# Winning message.
	if type(this_board) == Board:
		print_board(this_board)
		if this_board.won and not error:
			print "You have won. Nice work!"

		# If using a file, saves the state to the file.
		if using_file == True:
			file_in_question = open(args.file, "w")
			for_appending = []
			for slot in this_board.slots:
				slot.value = slot.value.replace(' ','+')
				for_appending.append(slot.value)
			file_in_question.write("".join(for_appending))
			file_in_question.close()

def parse_arguments(args):	
	input_string = None
	using_file = False
	if args.file:
		# Open the file (if it exists) and get the contents.
		if exists(args.file):
			file_in_question = open(args.file)
			contents = file_in_question.read()
			file_in_question.close()
			input_string = contents
			using_file = True
	
	# If there hasn't been a file input, the program uses the argument to --input.
	if input_string == None:
		input_string = args.input

	# Uses a blank board if the -n flag is passed.
	if args.new and args.file:
		using_file = True
		input_string = "+++++++++"

	# Calls the function which runs the game.
	this_board, error = runTheThing(input_string,args.place,args.x,args.y)
	return this_board, error, using_file

# Classes for the game board and for each slot on the game board.
class Slot(object):
	"""Slot class for each of the nine slots on the board"""
	def __init__(self,value):
		self.value = value

class Board(object):
	"""Board with nine slots"""
	def __init__(self, input_board):
		self.slots = [None,None,None,None,None,None,None,None,None]
		self.won = False
		count = 0

		for item in input_board:
			item = item.replace('+',' ')
			self.slots[count] = Slot(item)
			count +=1		

# Validates the --input board string.
def parse_input(input_string, error):
	input_board = list(input_string.upper())
	
	if len(input_board) != 9:
		error = "Input must be nine characters long (X, O and + allowed)."

	for letter in input_board:
		if not letter.upper() in ("X","O","+"):
			error = "Input may only contain Xs, Os or +'s."

	return input_board, error

# Validates the --place character.
def parse_place_character(inputted):
	if not inputted.upper() in ("X","O"):
		error = "You must place either an X or an O."
		return error

# Validates the -x and -y co-ordinates.
def parse_co_ordinate(inputted):
	try:
		if not int(inputted) in range(0,3):
			error = "You have entered an invalid co-ordinate. They must all be 0, 1 or 2."
			return error
	except ValueError:
		error = "Co-ordinate was not in the correct format. Please enter an integer."
		return error

# Places a letter on the board, if the relevant slot is empty.
def place_letter(board,value,x,y):
	position = (y*3)+x

	if board.slots[position].value == ' ':
		board.slots[position].value = value
		return None
	else:
		error = "There is already a letter in that position."
		return error

# Reverses the letter placement (only called if the move is illegal).
def reverse_letter_placement(board,value,x,y):
	position = (y*3)+x
	board.slots[position].value = ' '

# Prints the board to the screen.
def print_board(board):
	count = 1
	for item in board.slots:
		item.value = item.value.replace('+',' ')
		if count % 3 == 0:
			print board.slots[count-1].value
		else:
			print board.slots[count-1].value,
		count +=1

# Checks that the --input argument has given a valid string.
def checkValidBoard(input_list):
	error = None
	numberOfXs = input_list.count("X")
	numberOfOs = input_list.count("O")
	difference = numberOfXs - numberOfOs

	if difference < -1 or difference > 1:
		error = "Invalid board entered (There can only be one more X than the number of Os, and vice versa)."

	return error

# Checks if the letter that is being placed is an illegal move.
def checkValidMove(board,value,x,y):
	input_list = []
	for slot in board.slots:
		input_list.append(slot.value)

	error = None
	numberOfXs = input_list.count("X")
	numberOfOs = input_list.count("O")
	difference = numberOfXs - numberOfOs

	if difference < -1 or difference > 1:
		error = "Invalid move entered (There can only be one more X than the number of Os, and vice versa)."
		reverse_letter_placement(board,value,x,y)

	return error

# Checks if the player has won.
def checkForWin(board):
	ones_to_check = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

	for one in ones_to_check:
		if board.slots[one[0]].value == "X" or board.slots[one[0]].value == "O":
			if board.slots[one[0]].value == board.slots[one[1]].value and board.slots[one[1]].value == board.slots[one[2]].value:
				board.won = True

# This function runs the game, calling the other functions in turn.
def runTheThing(arginput,argplace,argx,argy):
	error = None
	this_board = None
	if arginput:
		inputted_board, error = parse_input(arginput, error)
		if error:
			return inputted_board, error
		error = checkValidBoard(inputted_board)
		this_board = Board(inputted_board)
		checkForWin(this_board)
	else:
		error = "No board entered. Please enter one."
		return this_board, error
	if argplace:
		error = parse_place_character(argplace)
		if error:
			return this_board, error
		if argx == None or argy == None:
			error =  "Please enter X and Y co-ordinates for your placement."
			return this_board, error
		else:
			error = parse_co_ordinate(argx)
			if error:
				return this_board, error
			
			error = parse_co_ordinate(argy)
			if error:
				return this_board, error
			
			error = place_letter(this_board,argplace.upper(),int(argx),int(argy))
			if error:
				return this_board, error
			error = checkValidMove(this_board,argplace.upper(),int(argx),int(argy))
			checkForWin(this_board)
			return this_board, error
	else:
		return this_board, error

# Calls the main function.
if __name__ == '__main__':
	main()