import operator

saved_string = ''

def remove_letter(): #Remove a selected letter from a string
    user_string = str(input("Enter a string: "))
    remove_letter = str(input("Enter letter to remove: "))
    indx = 0
    remove_letter = remove_letter[0] ## index set in indx
    str_len = len(user_string)

    while (indx < str_len):
        if user_string[indx] == remove_letter:
            user_string = user_string[:indx] + user_string[indx + 1::]
        str_len -= 1
        indx += 1
    print("Your string: %s" % user_string)
    
    return

def num_compare(): #Compare 2 numbers to determine the larger
    num = int(input("Enter first number to compare: "))
    num2 = int(input("Enter second number to compare: "))
    if num > num2:
        print (num, " is greater")
    elif num2 > num:
        print (num2, " is greater")
    else:
        print ("Numbers are equal")
    return

def print_string(): #Print the previously stored string
    print (saved_string)
    return

def calculator(): #Basic Calculator (addition, subtraction, multiplication, division)
    return

def accept_and_store(): #Accept and store a string
    global saved_string
    saved_string = str(input("Please input a string: "))
    return

def main(): #menu goes here
    select = [accept_and_store, remove_letter, num_compare, print_string] # list for menu

    while(True):
        print ("Please select operation:")
        print ("1. Enter string")
        print ("2. Remove a letter")
        print ("3. Greater of two numbers")
        print ("4. Your string")
        user_select = input("Please make selection: ")

        if user_select == "":
            print ("You have exited program")
            raise SystemExit
        elif user_select != "":
            user_select = int(user_select)
            user_select -= 1 # reduce 
            select[user_select]()
        
    return

main()
