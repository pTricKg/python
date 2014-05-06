
def my_counter():
    name = input('Enter file:')
    handle = open(name, 'r')
    text = handle.read()
    words = text.split()

    count=0
    for word in words:
        count = count + 1

    print ("There are",count,"words in this document.")

    user_decides = input("Would you like to count more?:")
    if user_decides == str('yes' or 'Yes'):
        my_counter()
    else:
        print ("Good Bye")

    
my_counter()


    



