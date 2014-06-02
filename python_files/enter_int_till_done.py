while True:
    nums = []
    inp = raw_input('Enter a number: ')
    if inp == 'done' : 
        break

    try:
        num = float(inp)
        nums.append(float(inp))
    except:
        print 'Invalid input'
        continue                            

numbers = list(num)
minimum = None       
maximum = None

for num in numbers :                          
    if minimum == None or num < minimum :
        minimum = num

for num in numbers :        
    if maximum == None or maximum < num :
        maximum = num

print 'Maximum:', maximum
print 'Minimum:', minimum


total = 0
count = 0

while True:
	inp = input('Enter a number:')
	if inp == 'done: break
	value = float(inp)
	total = total + value
	count = count + 1
average = total / count
print('Average:',average)
