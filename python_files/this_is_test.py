##character = [2,3,0,8]
##
##char = ''.join(chr(i) for i in character)
##    
##
##print(char)
import random


from random import choice
charlist = "abcdefghijklmnopqrstuvwxyz"
total = 0
while total != 248410397744610:
    total = 0
    countone = 0
    counttwo = 0
    print("-----------")
    while total < 248410397744610:
        
        countone = ord(choice(charlist))
        counttwo = charlist.index(chr(countone))
        counttwo = counttwo + 1
        total = total*17
        total = total + counttwo
        print(chr(countone))
        
        if total == 248410397744610:
            print("Success!")
            quit()
