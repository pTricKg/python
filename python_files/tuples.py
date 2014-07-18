""" playing with tuples """

txt = 'but soft what light in yonder window breaks'

words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
t.sort(reverse = True)

res = list()
for length, word in t:
    res.append(word)

print(res)

# assign tuples
w = ['check', 'tuples', 'assignment']
x, y, z = w # assign letters to words

print(x, y, z)

# swapping elements of tuple
x,y,z = y, x, z

print(x,y,z)
print(y,x,z)

addy = 'monty@python.org'
uname, domain = addy.split('@')

print(uname, domain)


# dicts and tuples
d = {'a':101011, 'b':10010, 'c':101110}
t = d.items()
print(t)

# stupid python 3 breaks the sort so following doesn't work
t.sort()
print(t)

l = list()
for key, value in d.items():
    print(key, value)
    l.append((value, key))
    print(l)
    l.sort(reverse=True)
print(l)
print(value, key)

