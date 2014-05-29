import os

def my_counter():
    name = input('Enter file or path to file: ')
    dr = os.getcwd()
    print("You are here:",dr)
    print(name, "is your input")

    #try:
        
    if name.startswith("/"):
        handle = open(name, 'r')
        text = handle.read()
        words = text.split()            
    else:
        file_open = os.getcwd()
        print("Your file isn't located in this directory:",file_open)
        clarify = input("You must clarify where your file is: ")
        print(clarify)
        chngdir = os.chdir(clarify)
        print(chngdir)
        file_open = os.getcwd()
        print("Where we are now at", file_open)
        file_open = file_open.rstrip() + "/" + name
        print(file_open)
        
        handle = open(file_open, 'r')
        text = handle.read()
        words = text.split()
##    except:
##        print("Something isn't right.  Please start again")
##        my_counter()

    count=0
    for word in words:
        count = count + 1

    print ("There are",count,"words in this document.")

    user_decides = input("Would you like to count more?:")
    user_decides.lower()
    print(user_decides)
    if user_decides == str('yes'):
        my_counter()
    elif user_decides != str('yes'):
        user_decides_two = input("Yes to continue or anything else to not")
        if user_decides_two != str('yes'):
           print("Good Bye")
        
    else:
        print ("Good Bye")

    
my_counter()


    



