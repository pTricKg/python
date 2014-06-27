#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# convert number to name function
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

# convert name to number function   
def name_to_number(name):
    
    if name == "rock":
        return 0
    elif name == "Spock".lower():
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
# Greeting
print("""
         iiiii     aaa     mmmm  mm
         iiii     aa aa    mmmm  mmm
        iiii     aa  aa    mm mmm mmm
        iiii    aaaaaaaa   mm  mm  mm
        iiii   aaaaaaaaa   mm  mm  mmm
        iiii   aa     aa   mm  mm  mmmm
        iiii   aa    aaa   mmm mmm mmmmm""")

print("""
                        +
                       +++               +
                       +..~=7. .,,::~~=+++.                     
                ..??I~.,,:::~~==+++??I,:+I$..               
                 ..II?,,,:::~~==+++???III7.                 
               .,:,,,,,,::::~===+++???77II~..               
               ~::::::::::~~~===++++??III7I7..              
             .,~~~::::::~~~~====++++????IIII7.              
              =~~~~~~I~~~======+++++????????I.              
             .====~+D+78:~====+++++?+DD$+????I              
             :+====+NZI$~~=+++++++++8778Z~+??I              
             ,+++====~~~~=+++++++++??DZZ~==+?I              
             .?++++++++++++++++++????+===+++?I              
             .II???????+?+++++?????+++++++?+??              
             .:~OOIIII???????????????????IID7,              
       ,,,,:~+Z~~==+?ZNO77IIIIIIIIII$ND7$$$$7O++?I?.        
     ..,,,::~~+I===++++??IIIIIII77I77$$$$$$$?~===++I:.      
     ..,,:::~~??===+++????IIIIIIIII7$$$$$$$7~===+++?7.      
     ..::::~~~??==++++????IIIIIIII7777$$$$$7===++++?I.      
     ..:~~~~=+??+++++?????IIIIIIII777777777I+++++++?,.      
     ..~~~===??I++++?????IIIIIIII7777777777I++++++??..      
       +====???I????????IIIIIII?77IIIII7777I????????..      
       ?+++?????I???????IIIIII?IIIIIIIIIII7I????????..      
       +++??????7I????IIIII???IIIIIIIIIIIIIII???????        
       .??????+?III?IIIIII???IIIIIIIIIIIIIIIII????+I        
       .II????+?IIIIIIII???IIIIIIIIIIIIIIIIII???+?+?        
       .7I??????I$7IIII?IIIIIIIIIIIII????II7.?II+.          
       ...~7II=I$$$7777IIIIIIIIIIII??????II7......          
           .. .=$$$7777IIIIIIIIIII???????II7::,:.           
               .$$$$777IIIIIIIIII??????III77::::,,,         
               .$$$$77777IIIIIIIIIIIIIII77$+:::::,,,        
                .$$$$$77777777777777777ZZZZ+:::::,,,,       
                .II77$Z$$$7$777$$?8O7$$ODMM+::::::,,.       
                .INNMMMNOOO:~~~::~+I7$$Z$ZO+::::::,,        
                .?II777ZOZZ~~~~~~:??I777$ZZ=:::::,.         
                ..I777$ZZZ8:~~~~~~DNDZ8NMD$+::. .           
                ..ZNMMMMDZZ:~~~: .+?I7$ZZZZ+,.              
                ..7$$7ZZZZZ=~..  .7I7$ZZZZZ.                
                  $777ZZZZ$.       ..~~..                   
                 . .. ......       ......
                 """)

# Game Title and Rules
print("\t***Welcome to Rock Paper Scissors Lizard Spock Challenge***")
answers = ['rock', 'paper', 'scissors', 'lizard', 'Spock']
print("\n\tLets battle!\n\nUsable answers are " + str(answers))
print("\n\nLet's play best out of five throws!")

# How to play
print("\n\nThe rules are as follows: ")
print("\n\tScissors cut Paper\n\
        Paper covers Rock\n\
        Rock crushes Lizard\n\
        Lizard poisons Spock\n\
        Spock smashes Scissors\n\
        Scissors decapitates Lizard\n\
        Lizard eats Paper\n\
        Paper disproves Spock\n\
        Spock vaporizes Rock\n\
        Rock crushes Scissors")

# count iterations of while loop
count_win = 0
count_lose = 0
count = 0
countWinnerUser = 0
countWinnerComp = 0
tie = 0
while count < 5:
    count = count + 1
    ur_answer = str(input("\nThrow yours! ").lower())
    print("\n\nYou threw " + ur_answer)

    # check for valid input
    # add try/except to get errors handled
    try:
        # convert name to player_number using name_to_number
        player_number = name_to_number(ur_answer)

        # compute random guess for comp_number using random.randrange()
        comp_number = random.randrange(5)
        print("\nProgram chooses " + number_to_name(comp_number).capitalize())

        # compute difference of player_number and comp_number modulo five
        result = ((player_number - comp_number) % 5)

        if result == 0:
            tie = tie + 1
            print("\nUser and Program tie!")
            print("\n")
        elif result == 1:
            count_win = count_win + 1
            countWinnerUser = countWinnerUser + 1
            print("\nUser wins!")
            print("\n")
        elif result == 2:
            count_win = count_win + 1
            countWinnerUser = countWinnerUser + 1
            print("\nUser wins!")
            print("\n")
        elif result == 3:
            count_lose = count_lose + 1
            countWinnerComp = countWinnerComp + 1
            print("\nProgram wins!")
            print("\n")
        else:
            count_lose = count_lose + 1
            print("\nProgram wins!")
            countWinnerComp = countWinnerComp + 1
            print("\n")
    except:
        print("Invalid input!".upper())
# Rules...
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

#Finally    
if count_win > count_lose:
    print("The force is with this one")
elif count_win == count_lose:
    print("It's a draw, User!")
else:
    print("User is no match for Program!\n\n")
print("User won " + str(countWinnerUser) + " ,Program won " \
      + str(countWinnerComp) + " and draw " + str(tie))
print(
        """
         _____       ___       ___  ___   _____  
        /  ___|     /   |     /   |/   | |  ___| 
        | |        / /| |    / /|   /| | | |__   
        | |  _    / ___ |   / / |__/ | | |  __|  
        | |_| |  / /  | |  / /       | | | |___  
        \_____/ /_/   |_| /_/        |_| |_____|
         
         _____   _     _   _____   _____   
        /  _  \ | |   / / |  ___| |  _  \  
        | | | | | |  / /  | |__   | |_| |  
        | | | | | | / /   |  __|  |  _  /  
        | |_| | | |/ /    | |___  | | \ \  
        \_____/ |___/     |_____| |_|  \_\

        """
        )    
