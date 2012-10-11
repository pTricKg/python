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
    
        
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below
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

    # convert name to number using if/elif/else
    # don't forget to return the result!


def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    print("\nPlayer chooses " + number_to_name(player_number))

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(5)
    print("\nComputer chooses " + number_to_name(comp_number))

    # compute difference of player_number and comp_number modulo five
    result = ((player_number - comp_number) % 5)

    if result == 0:
        print("\nPlayer and Computer tie!")
        print("\n")
    elif result == 1:
        print("\nPlayer wins!")
        print("\n")
    elif result == 2:
        print("\nPlayer wins!")
        print("\n")
    elif result == 3:
        print("\nComputer wins!")
        print("\n")
    else:
        print("\nComputer wins!")
        print("\n")
        

	# use if/elif/else to determine winner

##scissor cut paper
##paper covers rock
##rock crushes lizard
##lizard poisons Spock
##Spock smashes scissors
##scissors decapitates lizard
##lizard eats paper
##paper disproves Spock
##Spock vaporizes rock
##rock crushes scissors
    
    
### test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
##
### always remember to check your completed program against the grading rubric
##
##
##
