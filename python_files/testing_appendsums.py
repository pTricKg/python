def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements of lst to lst.
    This is an infinite loop.
    """

    for vals in lst:
        
        #print("From list",lst[vals])
        
        lst.append(lst[- 1] + lst[ - 2] + lst[ - 3])
        print("Append",lst)            
        

## my_list = [0,1,2]
##
## appendsums(my_list)
## appendsums([0,1,2])
