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


##total = 0
##count = 0
##
##while True:
##	inp = input('Enter a number:')
##	if inp == 'done: break
##	value = float(inp)
##	total = total + value
##	count = count + 1
##average = total / count
##print('Average:',average)
