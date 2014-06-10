def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements of lst to lst.
    """

    # first get length of list
##    lst_len = len(lst) - 1 # must subtract one to actual indexing from 0
##    for n in lst:

##    val1 = lst[lst_len]
##    val2 = lst[lst_len - 1]
##    val3 = lst[lst_len - 2]
##
##    final = val1 + val2 + val3
##
##    print(val1,val2,val3,"and final sum:",final)
    
    
    for vals in lst:

        print("From list",lst[vals])
        lst.append(vals)
        print("Append",lst)
        
        

## my_list = [0,2,3]
##
## appendsums(my_list)
##appendsums([0,1,2])
