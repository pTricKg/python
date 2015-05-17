import random

def getRange():
    rbegin = input("Start range: ")
    rstop = input("End range: ")

    print("You gave: from " + rbegin + " to " + rstop)
    rsp = input("Is this okay? ")
    print("You said " + "" + rsp + "")

    lst = list()
    for letters in rsp:
        print(letters)
        
        lst.append(letters)

        print(lst)

