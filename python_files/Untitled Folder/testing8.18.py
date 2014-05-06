def median(lst):
    ''' takes a list, sorts list, and give median value'''
    lst.sort()
    if len(lst) % 2 == 0:               # checks if even
        one = int(len(lst) / 2.0)       # declares variable to hold first median
        two = int((len(lst) / 2.0) - 1) # delcares second variable
        return (lst[one] + lst[two]) / 2.0 # averages the two median values
        print (lst[one],lst[two])       # for testing
    else:
        three = int(len(lst) / 2.0) # for non-even lists,
        return 1st[three]           # just half to get median value
        print (lst[three])
