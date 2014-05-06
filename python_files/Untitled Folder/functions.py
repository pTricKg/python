
def median(lst):
    ''' takes a list, sorts list, and give median value'''
    lst.sort()
    if len(lst) % 2 == 0:               # checks if even
        one = int(len(lst) / 2.0)       # declares variable to hold first median
        two = int((len(lst) / 2.0) - 1) # delcares second variable
        return (lst[one] + lst[two]) / 2.0 # averages the two median values
        print (lst[one],lst[two])       # for testing
    else:
        three = int(len(lst) / 2.0) # for non-even lists,
        return 1st[three]           # just half to get median value
        print (lst[three])

def remove_duplicates(lst):
    new = []
    while len(lst) >= 1:
        for i in lst:
            if i not in new:
                new.append(i)
            
        return new
    return new
    
print remove_duplicates([1,2,2,3,3,5,5])

def product(integers):
	''' Loops through list and multiplies elements.
	Returns product
	 '''
    i = 1
    for ints in integers:
        i *= ints
    return i
    
print product([2,2,3])

def purify(lst):
	'''Takes list and removes odd numbers.
	>>> purify([2,3,2,20,10,13,23])
	[2, 2, 20, 10]'''

    i = 0
    while(i<len(lst)):
        if lst[i] % 2 == 0:
            i += 1
        else:
           del lst[i]
    return lst

purify([2,3,2,20,10,13,23])

def reverse(text):
    # creates empty string to populate
    new_text = ""
    # set length of text to less than 0
    x = len(text)-1
    ## loops while x has at least one char
    while x != -1: 
        new_text+=text[x] # adds x to new_text
        x -= 1  # decrementing x
    return new_text
## testing , results in 'txet'
reverse('text')

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if not x & 1:
        return False
    for n in range(3, int(x**0.5)+1,2):
        if x % n == 0:
            return False
    return True

def factorial(x):
    total=1
    total *= x
    x -= 1
    while x > 0:
        total *= x
        x -= 1
    return total

def digit_sum(n):
    if n % 10 != n:
        return n % 10 + digit_sum(n // 10)
    else:
        return n

def is_int(x):
    if x % 2 == 0 or x % 2 == 1:
        return True
    else:
        return False

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
        
