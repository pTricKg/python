def find_element(p,t): ## index is i, stop condition is when i reaches length of p
    i = 0              ##t = target; check if current element = t
    while i < len(p):
        if p[i] == t:
            return i ##stop here and would run forever, need to increment i
        i = i + 1
    return -1         ##if no matched elements, return -1

##with for loop-no track
def find_element(p,t):
    i = 0
    for e in p:       ##goes through all elements, compare e and t, return matched increments
        if e == t:
            return i
        i = i + 1
    return -1

##list operation
##<list>.index(<value>)

##if <value> is in the <list>,
##returns the first position where
##<value> is found in <list>.
##otherwise, produces an error.

##in operation  or not in
##<value>in<list> or <value> not in <list>
##3 in p
#if <value> is in the <list>,
##output is True. Otherwise, output is False
p = [0,1,2]
print p.index(3)
print 2 in p

def find_element(p,t):
    if t in p:
        return p.index(t)
    else:
        return -1

##or with not in
def find_element(p,t):
    if t not in p:
        return -1
    return p.index(t)

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)
##pop
<list>.pop() # element, mutates the list by removing and
                ##returning last element




