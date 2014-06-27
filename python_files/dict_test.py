""" Using dictionary to count word frequency in text """

opn = open('nineteen_eighty_four.txt')
rd = opn.read()
splt = rd.split()
d = {}

##for i in splt:
##    if i not in d:
##        d[i] = 1
##    else:
##        d[i] = d[i] + 1
##
##print(d)

## Better way to get same done as above
for i in splt:
    d[i] = d.get(i,0) + 1
print(d)


dval = d.values()
total = 0

for i in dval:
    total = total + i
print("Total:", total)
    


##val = d.values()
##
##print(val)
##vlist = []
##dtwo = {}
##
##for v in val:
##    vlist.append(v)
##    for i in vlist:
##        if i >= 5:
##            if i not in dtwo:
##                dtwo[i] = dtwo[i] + 1
##            else:
##                dtwo[i] = dtwo[i] + 1
##print(dtwo)


""" Using dictionary to find and count freq """

##opn = open('nineteen_eighty_four.txt')
##rd = opn.read()
##splt = rd.split()
##d = {}
##
##for i in splt:
##    if i.find('@') > 0:
##        if i not in d:
##            d[i] = 1
##        else:
##            d[i] = d[i] + 1
##
##print(d)
