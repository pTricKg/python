# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

##import frame
import random
##import math

# initialize global variables used in your code
num_range = 100

message = "Pick a number from 0 and 100"
print (message)



# define event handlers for control panel
##def init():
##    print ("New game. Range is 0 to 100.")
##    get_input(guess)
##    if range100():
##        print ("New game. Range is 0 to 100.")
##    elif range1000():
##        print ("New game. Range is 0 to 1000.")   
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    num_range = random.randrange(1, 100)
    return num_range
    while True:
        user = int(input())
        if user < num_range:
            print ("Higher")
        elif user > num_range:
            print ("Lower")
        elif user == num_range:
        	break
    
    
    

##def range1000():
##    # button that changes range to range [0,1000) and restarts
##    global num_range
##    num_range = random.randrange(1, 1000)
##    return num_range

def get_input(guess):
    # main game logic goes herede
    

    if guess != str(range100()):
        if guess < str(range100()):
            print ("\nGuess was", guess)
            print("Higher\n")
            
            
            
        elif guess > str(range100()):
            print ("\nGuess was", guess)
            print("Lower\n")
            
            
    else:
        print("You win!")

get_input(guess)

### create frame
##f = frame.create_frame("Guess the number", 200, 200)
##
### register event handlers for control elements
##f.add_button("Range is [0, 100]", range100, 200)
##f.add_button("Range is [0, 1000]", range1000, 200)
##f.add_input("Enter a guess", get_input, 200)
##
### start frame
##frame.start()

##            New game. Range is 0 to 100.
##            Number of remaining guesses is 7
##
##            Guess was 50.
##            Number of remaining guesses is 6.
##            Lower or Higher or Correct!

