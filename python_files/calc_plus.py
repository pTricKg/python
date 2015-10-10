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
    return

def print_string(): #Print the previously stored string
    return

def calculator(): #Basic Calculator (addition, subtraction, multiplication, division)
    return

def accept_and_store(): #Accept and store a string
    return

def main(): #menu goes here
    return

main()
