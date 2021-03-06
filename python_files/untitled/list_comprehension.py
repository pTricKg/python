## List Comprehension


## makes list of even squares of 1 to 10
even_squares = [x**2 for x in range(1,11) if x % 2 == 0]

print even_squares

## makes list of cubed number divised evenly by 4
cubes_by_four = [x**3 for x in range(1,11) if (x**3) % 4 == 0]

print cubes_by_four

## list slicing
## [start:end:stride] stride is increments of list items selected
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]
# prints [9, 25, 49, 81]

## print out list elements via slicing
## following will print odd elements
my_list = range(1, 11) # List of numbers 1 - 10

print my_list[::2] 
''' preceding has null value for start, so python assumes beginning of list
	end has null value, so python assumes end of list,
	stride equals 2 so pulls 2 item from list and on and on,
	in this case it is odd numbers'''

## positve strides go through list from start to finish or left to right
## negative strides go through list backwards
my_list = range(1, 11)

backwards = my_list[::-1]

print backwards

## another going backwards through list by tens
to_one_hundred = range(101)

backwards_by_tens = to_one_hundred[::-10]

print backwards_by_tens

## 
to_21 = range(1,22)

odds = to_21[::2]
middle_third = to_21[7:14:1]

print odds + middle_third

## prints [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 8, 9, 10, 11, 12, 13, 14]


