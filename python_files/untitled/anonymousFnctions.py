## creating anonymous functions with lambda
lambda variable: expression

## usually only useful when function only needed once or so

'''Python allows for a style of programming called functional programming, 		which means that you're allowed to pass functions around just as if they 	were variables or values. '''

''' lambda x: x % 3 == 0
Is the same as

def by_three(x):
    return x % 3 == 0'''

## eg
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

# prints [0, 3, 6, 9, 12, 15]

# using 
languages = ["HTML", "JavaScript", "Python", "Ruby"]

#lambda languages: "Python"
print filter(lambda x : x == "Python", languages) ## first parameter set to find python, second sets where to find or first set set filter, second sets what to filter 

## 
threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]

print threes_and_fives

## prints [3, 5, 6, 9, 10, 12, 15]

## pulling out secret message 
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-2]
print message

# message is backwards and each character wanted is x 2

'''another example of lambda and filter() to pull out hidden message.
	this makes new variable which filters out "X" from list'''
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda x : x != "X" , garbled)
print message



