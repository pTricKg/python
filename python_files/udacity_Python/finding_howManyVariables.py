#finding how many variables in a list element
def measure_udacity(U):
    count = 0
    for e in U:
        if e[0] == 'U':
            count = count + 1
    return count

print( measure_udacity(['Dave', 'Sabastian', 'Katy']))
print( measure_udacity(['Umika', 'Umberto', 'Jack']))
print( measure_udacity(['udacity', 'United States', 'union', 'U2']))
