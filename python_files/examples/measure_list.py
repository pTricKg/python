#finding how many variables in a list element
def measure_list(U):
    count = 0
    for e in U:
        if e[0] == 'U':
            count = count + 1
    return count

print( measure_list(['Dave', 'Sabastian', 'Katy']))
print( measure_list(['Umika', 'Umberto', 'Jack']))
print( measure_list(['udacity', 'United States', 'union', 'U2']))
