### This goes through given input, makes list
### then give maximum and minumum from input

nums = list()
while True:

    inp = input('Enter a number: ')
    if inp == 'done' :
        break

    try:
        num = float(inp)
        nums.append(num)
    except:
        print ('Invalid input')
        continue


numbers = nums
minimum = None
maximum = None

for num in numbers :
    if minimum == None or num < minimum :
        minimum = num

for num in numbers :
    if maximum == None or maximum < num :
        maximum = num

print ('Maximum:', maximum)
print ('Minimum:', minimum)
print ('From given input:',nums)

# This is a simple averaging program

total = 0
count = 0

while True:
	inp = input('Enter a number:')
	if inp == 'done': break
	value = float(inp)
	total = total + value
	count = count + 1
average = total / count
print('Average:',average)

# A bit cleaner version of above using built-in functions and list

numlist = []

while True:
    inp = input('Enter a number:')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average:', average)
