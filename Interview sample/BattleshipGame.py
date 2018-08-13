"""This is a basic game of battleship where the user has to guess the exact
location of the battleship  hidden on the board.
This uses the list data structure"""
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row)) #joins the rows and column for game UI

print_board(board) #prints board for user to begin game

def random_row(board):
  return randint(0, len(board) - 1) #generates random loaction on board

def random_col(board):
  return randint(0, len(board[0]) - 1)#generates random loaction on board

ship_row = random_row(board) #battleship row hidden at
ship_col = random_col(board) #battleship hidden at this column
# print (ship_row)  shows exact location were ship hidding CHEATING!!!
# print (ship_col)  shows exact location were ship hidding CHEATING!!!

print ("Welcome to Battleship. Let the game begin")
for turn in range(4):
  print ("Turn", turn + 1)#user has 4 tries
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sank my battleship!") #user wins
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print ("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )#coordinates already marked 'X'
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    print_board(board)
    if(turn==3):
      print ("Game Over!!!")#if user has exhausted all their tries game over

print ("Thanks for playing battleship!!")
