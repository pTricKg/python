def count(sequence,item):
    ''' Finds items within given list'''
    
    found = 0
    for i in sequence:
        if i == item:
            found += 1
    return found
    #print (found)
            
count(['i','t','e','m'], 't')
count([23,14,'you', 'mom', 444], 'you')
