board = [ ]
#for [ ] in board:

for b in range(0,5):
    board.append(["O"] * 5)##appending list of zeros
   
    
    
def print_board(board):
    for row in board:
        print (" ".join(row))##removes commas from each row
        
print_board(board)

##givens
from random import randint 

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))

# Add your code below!list_name[i][j]elif board[int(guess_row)][int(guess_col)] = "X":
        ##print "You guessed that one already."
ship_row = []
ship_col = []

def random_row(board):
    return randint(0, len(board) - 1)
    
def random_col(board):
    return randint(0, len(board[0]) - 1)
    
ship_row = random_row(board)
ship_col = random_col(board)

# Add your code below!


print (ship_row)
print (ship_col)


for turn in range(4):
    turn_number = turn + 1
    print ("Turn number " + str(turn + 1))
    guess_row = input("Guess Row: ")
    guess_col = input("Guess Col: ")
    
    if ship_row == guess_row and ship_col == guess_col:
        print ("Congratulations! You sank my battleship!")
        break
        
    else:
        print ("Better luck next time, Sailor!")
        board[int(guess_row)][int(guess_col)] = "X"
        print_board(board)
        
       ## if guess_row < 0 or int(guess_row) > int(guess_row[-1]) or guess_col < 0 or int(guess_col) > int(guess_col[-1]):
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("Oops, that's not even in the ocean.")
            
        else:
            print ("You missed my battleship!")
            board[int(guess_row)][int(guess_col)] = "X"
            print_board(board)
        if turn_number == 4:
                    print ("Game Over!")

##from random import randint
##
##board = []
##
##for x in range(5):
##    board.append(["O"] * 5)
##
##def print_board(board):
##    for row in board:
##        print " ".join(row)
##
##print "Let's play Battleship!"
##print_board(board)
##
##def random_row(board):
##    return randint(0, len(board) - 1)
##
##def random_col(board):
##    return randint(0, len(board[0]) - 1)
##
##ship_row = random_row(board)
##ship_col = random_col(board)
##print ship_row
##print ship_col
##
### Everything from here on should go in your for loop!
### Be sure to indent four spaces!
##guess_row = input("Guess Row:")
##guess_col = input("Guess Col:")
##
##if guess_row == ship_row and guess_col == ship_col:
##    print "Congratulations! You sunk my battleship!"
##else:
##    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
##        print "Oops, that's not even in the ocean."
##    elif(board[guess_row][guess_col] == "X"):
##        print "You guessed that one already."
##    else:
##        print "You missed my battleship!"
##    board[guess_row][guess_col] = "X"
##    # Print (turn + 1) here!
##    print_board(board)*/

##Finished
##from random import randint
##
##board = []
##
##for x in range(5):
##    board.append(["O"] * 5)
##
##def print_board(board):
##    for row in board:
##        print " ".join(row)
##
##print "Let's play Battleship!"
##print_board(board)
##
##def random_row(board):
##    return randint(0, len(board) - 1)
##
##def random_col(board):
##    return randint(0, len(board[0]) - 1)
##
##ship_row = random_row(board)
##ship_col = random_col(board)
##print ship_row
##print ship_col
##
## Everything from here on should go in your for loop!
## Be sure to indent four spaces!
##
##
##for turn in range(4):
##    turn_number = turn + 1
##    print "Turn number " + str(turn + 1)
##    guess_row = input("Guess Row:")
##    guess_col = input("Guess Col:")
##    
##
##    if guess_row == ship_row and guess_col == ship_col:
##        print "Congratulations! You sunk my battleship!"
##        break
##    else:
##        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
##            print "Oops, that's not even in the ocean."
##        elif(board[guess_row][guess_col] == "X"):
##            print "You guessed that one already."
##        else:
##            print "You missed my battleship!"
##            board[guess_row][guess_col] = "X"
##            # Print (turn + 1) here!
##            print_board(board)
##        if turn_number == 4:
##                print "Game Over!"
    

