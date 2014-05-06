## dictionary looping

d = {'x': 9, 'y': 10, 'z': 20}

for key in d:
    # Your code here!
    print key + ' ' + str(d[key])

##using indexing with enumerate
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index + 1, item 

##multiple list looping with zip
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Add your code here!
    if a > b:
        print a
    else:
        print b

##for/else loops
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'
>>You have...
A banana
A apple
A orange
A tomato is not a fruit!

##is it divisible by 2
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

##return true for int and float
def is_int(x):
    if x % 2 == 0 or x % 2 == 1:
        return True
    else:
        return False
## Summing digits in number
def digit_sum(n):
    if n % 10 != n:
        return n % 10 + digit_sum(n // 10)
    else:
        return n

##factorial
def factorial(x):
    total=1
    total *= x
    x -= 1
    while x > 0:
        total *= x
        x -= 1
    return total
