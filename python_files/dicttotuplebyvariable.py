d = {'a':20, 'b':5, 'c':10} # created dict

tmplst = [] # empty list to be filled with tuples

for k, v in d.items(): # go thru key:value pairs
    tmplst.append( (v, k) ) # append tuples to list with value:key

print(tmplst)

tmplst.sort(reverse=True) # sort in reverse 

print(tmplst)

# use list comprehension
print(sorted( [ (v, k) for k, v in d.items() ] ))
