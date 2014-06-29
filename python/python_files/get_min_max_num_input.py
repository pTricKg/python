# Getting min and max numbers from user input

minimum = None
maximum = None

while True:
    num = input('Enter a number: ')
    if num == 'done': 
        break

    try:
        num_check = float(num)
    except:
        print ('Invalid input')
        continue                            

    if minimum is None or num_check < minimum:
        minimum = num_check

    if maximum is None or num_check > maximum:
        maximum = num_check

print ('Maximum is', maximum)
print ('Minimum is', minimum)

# Same as above but with built-in functions and list

mylist = []

minimum = None
maximum = None

while True:
    num = input('Enter a number:')
    if num == 'done': break
    try:
        num_check = float(num)
        mylist.append(num_check)
    except:
        print('Invalid input')
        continue
    maximum = max(mylist)
    minimum = min(mylist)
print ('Maximum is', maximum)
print ('Minimum is', minimum)
print ('From list you gave:',mylist)

