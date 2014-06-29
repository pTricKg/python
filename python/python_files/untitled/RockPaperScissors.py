from random import choice

# takes user input and capitalizes
name = input("Enter your name : \n").capitalize()

# prints input and describes game
print (name + ", to be clear, Rock breaks Scissors, Scissors cuts Paper, Paper covers Rock\n")

# list we use for choices
rps = ['rock','paper','scissors']

#score tracking variables
u = 0
v = 0

#Here is the while loop, which will continue till break. The below text is intended to fit into the while loop.
while 1:
    #print ("R: Rock,      P: Paper,     S: Scissor\n")

    # ask user for choice
    user = input("Choose Rock, Paper or Scissors: ")

    # lowercase user input
    user = user.lower()

    # creates program choice using list of choices and random choice generator
    py = choice(rps)
    
    if user == py:
        print ("You chose ",user, ". We tied!\n")

    elif user == 'rock' and py == 'scissors':
        print ('You entered Rock. I had Scissor. You win!\n')
        u+=1
    elif user == 'rock' and py == 'paper':
        print ('You entered Rock. I had Paper. You lose!\n')
        v+=1
    elif user == 'scissors' and py == 'paper':
        print ('You entered Scissor. I had Paper. You win!\n')
        u+=1
    elif user == 'scissors' and py == 'rock':
        print ('You entered Scissor. I had Rock. You lose!\n')
        v+=1
    elif user == 'paper' and py == 'scissors':
        print ('You entered Paper. I had Scissor. You lose!\n')
        v+=1
    elif user == 'paper' and py == 'rock':
        print ('You entered Paper. I had Rock. You win!\n')
        u+=1
    # check for invalid input
    elif user != 'rock' and user != 'scissors' and user != 'paper':
        print ("Invalid input!\n")

    # gives current score during each iteration
    print ("Your score is now: " + str(u))
    print ("Program's score is: " + str(v) + "\n")

    if v == 5:
        print ("Program wins!")
        # kill while loop
        break
    elif u == 5:
        print ("User wins! Congrats " + name)
        # kill while loop
        break
