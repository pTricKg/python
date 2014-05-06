# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def number_to_name(number):
    # fill in your code below
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    else:
        return "scissors"

    
def name_to_number(name):
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    else:
        return 4


def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    print("Player chooses " + number_to_name(player_number))
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(5)
    print("Computer chooses " + number_to_name(comp_number))
    
    # compute difference of player_number and comp_number modulo five
    result = ((player_number - comp_number) % 5)
    
    # use if/elif/else to determine winner

    # convert comp_number to name using number_to_name
    
    # print results
    if result == 0:
        print("Player and Computer tie!\n")
    elif result == 1:
        print("Player wins!\n")
    elif result == 2:
        print("Player wins!\n")
    elif result == 3:
        print("Computer wins!\n")
    else:
        print("Computer wins!\n")
        


    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric



