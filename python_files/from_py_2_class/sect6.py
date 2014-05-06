# Exercise6

def make_pairs(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list
    
    Return a new list in which each item is a 2-item list with the string from the
    corresponding position of list1 and the int from the corresponding position of list2.
    
    Precondition: len(list1) == len(list2)
    
    >>> make_pairs(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''
    
    pairs = []

##    inner_list = []  #
##    for i in range(len(list1)):
##        inner_list.append(list1[i])
##        inner_list.append(list2[i])
##        pairs.append(inner_list)
    ## results in [['A', 1, 'B', 2, 'C', 3],
    ##['A', 1, 'B', 2, 'C', 3], ['A', 1, 'B', 2, 'C', 3]]

    for i in range(len(list1)):
        pairs.append([list1[i], list2[i]])

##    for i in range(len(list1)):
##        inner_list = []
##        inner_list.append(list1[i])
##        inner_list.append(list2[i])
##        pairs.append(inner_list)

    
##    for i in range(len(list1)):
##        inner_list = []
##        inner_list.append(list1[i])
##        inner_list.append(list2[i])
##    pairs.append(inner_list)  ## results in [['C', 3]]

    return pairs

def contains(value, lst):
    ''' (object, list of list) -> bool

    Return whether value is an element of one of the nested lists in lst.

    >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]])
    True
    '''

    found = False  # We have not yet found value in the list.

##    for i in range(len(lst)):  # works
##        for j in range(len(lst[i])):
##            if lst[i][j] == value:
##                found = True

##    for item in lst:  # not desired result
##        if value == item:
##            value = True

##    for sublist in lst: # works
##        if value in sublist:
##            found = True
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            found = (lst[i][j] == value)
    
    return found

def lines_startswith(file, letter):
    '''(file open for reading, str) -> list of str

    Return the list of lines from file that begin with letter. The lines should have the
    newline removed.

    Precondition: len(letter) == 1
    '''

    matches = []

    for line in file:
        if letter in line:
            matches.append(line.rstrip('\n'))

##    for line in file:
##        if letter == line[0]:
##            matches.append(line.rstrip('\n'))
##
##    for line in file:
##        matches.append(line.startswith(letter).rstrip('\n'))
##
##    for line in file:
##        if line.startswith(letter):
##            matches.append(line.rstrip('\n'))

    

    return matches
        
