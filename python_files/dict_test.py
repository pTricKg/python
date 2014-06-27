""" Using dictionary to count word frequency in text """

opn = open('romeo.txt')
rd = opn.read()
splt = rd.split()
d = {}

for i in splt:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1

print(d)
