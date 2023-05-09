"""
	Given two players, create a python program to take in user inputs and fill the board.
	Display the board
"""

import os
from random import randint 
#from time import sleep

def display_board(board: list) -> None:
	'''
	Displays the board
	'''
	if(os.name == 'posix'):
  		 os.system('clear')
	# else screen will be cleared for windows
	else:
   		os.system('cls')
	print(board[1] + '|' + board[2] + '|' + board[3])
	print('-' + '|' + '-' + '|' + '-' )
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-' + '|' + '-' + '|' + '-' )
	print(board[7] + '|' + board[8] + '|' + board[9])


def player_input() -> tuple:
	'''
	OUTPUT = (Player 1 marker, Player 2 marker)
	'''
	marker = ''

	while marker != 'X' and marker != 'O':
		marker = input('Player 1: Choose X or O: ').upper()

		if marker == 'X':
			return ('X', 'O')
		else:
			return ('O', 'X')


def place_marker(board: list, marker: str, position: int) -> None:
	'''
	update the marker at the given position on the board
	'''
	board[position] = marker


def win_check(board: list, mark: str) -> bool:
	'''
	check for the winning pattern
	'''
	# ALL ROWS, check to see if they all have the same marker
	# ALL COLUMNS, check to see if they all have the same marker
	# TWO DIAGONALS, check to see if they match
	return (( board[1] == board[2] == board[3] == mark ) or 
	( board[4] == board[5] == board[6] == mark ) or 
	( board[7] == board[8] == board[9] == mark ) or 
	( board[1] == board[4] == board[7] == mark ) or 
	( board[2] == board[5] == board[8] == mark ) or 
	( board[3] == board[6] == board[9] == mark ) or 
	( board[1] == board[5] == board[9] == mark ) or 
	( board[3] == board[5] == board[7] == mark ))


def choose_first() -> str:
	'''
	check for which player goes first
	OUTPUT: Player No.
	'''
	flip = randint(0,1)

	if flip == 0:
		return 'Player 1'
	else:
		return 'Player 2'


def space_check(board: list, position: int) -> bool:
	'''
	Check whether a space on the board is freely available
	'''
	return board[position] == ' '


def full_board_check(board: list) -> bool:
	'''
	Check whether the board is full, return True if full, False otherwise
	'''
	for i in range(1,10):
		if space_check(board, i):
			return False
	
	# Board is full
	return True

def player_choice(board: list) ->  int:
	'''
	Ask for a player's next position(as a number 1-9) and then use the space_check
	function to check if the position is free. if it is, then retutn the position
	'''
	position = 0
	while position not in [1,2,3,4,5,6,7,8,9]  or not space_check(board, position):
		position = int(input('Choose a position: (1-9) '))

	return position


def replay() ->  bool:
	'''
	Ask the player if they want to play agaub abd return True if they want to
	'''
	choice = input("Play again? Enter Yes or No: ")
	return choice == 'Yes'

# Main
print('Welcome to TIC TAC TOE')

# While loop to keep running the game
while True:
	# Play the game

	## Set everything up (Board, Who goes first, marker they choose)
	initial_board = [' ']*10
	player1_marker, player2_marker = player_input() 

	turn = choose_first()
	print(turn + ' will fo first')

	play_game = input('Ready to play? Yes or No: ')
	if play_game == 'Yes':
		game_on = True
	else:
		game_on = False

	## Game Play
	while game_on:
		if turn == 'Player 1':
			## Player 1 turn

			# Show the board
			display_board(initial_board)
			# Choose a position
			position = player_choice(initial_board)
			# Place the marker on the position
			place_marker(initial_board, player1_marker, position)

			# Check if they won
			if win_check(initial_board, player1_marker):
				display_board(initial_board)
				print('Player 1 WON!!!')
				game_on = False
			else:
				if full_board_check(initial_board):
					display_board(initial_board)
					print("TIE Game! :( ")
					game_on = False
				else:
					turn = 'Player 2'
		
		## Player 2 turn
		else:
			# Show the board
			display_board(initial_board)
			# Choose a position
			position = player_choice(initial_board)
			# Place the marker on the position
			place_marker(initial_board, player2_marker, position)

			# Check if they won
			if win_check(initial_board, player2_marker):
				display_board(initial_board)
				print('Player 2 WON!!!')
				game_on = False
			else:
				if full_board_check(initial_board):
					display_board(initial_board)
					print("TIE Game! :( ")
					game_on = False
				else:
					turn = 'Player 1'
	
	#Break out of while based on replay() function.
	if not replay():
		break


# Test Code
############
# initial_board = [' '] * 10
# display_board(initial_board)
# #sleep(5)
# test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# display_board(test_board)
# #sleep(5)

# player1_marker, player2_marker  = player_input()
#print(player1_marker, player2_marker)

# place_marker(initial_board, player1_marker, 5)
# display_board(initial_board)

# display_board(test_board)
# print(win_check(test_board, 'X'))