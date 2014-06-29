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

numbers = list(nums)
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
