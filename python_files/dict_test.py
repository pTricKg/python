""" Using dictionary to count word frequency in text """

##opn = open('nineteen_eighty_four.txt')
##rd = opn.read()
##splt = rd.split()
##d = {}
##
####for i in splt:
####    if i not in d:
####        d[i] = 1
####    else:
####        d[i] = d[i] + 1
####
####print(d)
##
#### Better way to get same done as above
##for i in splt:
##    d[i] = d.get(i,0) + 1
##print(d)
##
##
##dval = d.values()
##total = 0
##
##for i in dval:
##    total = total + i
##print("Total:", total)
##    
##
##
##val = d.values()
##dtwo = {}
##
##print(val)
##
##for k,v in d.items():
##    if v >= 5:
##       dtwo[k] = v
##print("Second dictionary:",dtwo)



""" Using dictionary to find and count freq """

opn = open('nineteen_eighty_four.txt')
rd = opn.read().lower()
splt = rd.split()
d = {}

for i in splt:
    if 'speak' in i or 'double' in i or 'think' in i or 'party' in i:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
    else:
        continue

print(d)
