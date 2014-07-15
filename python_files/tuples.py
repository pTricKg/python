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

#
w = ['check', 'tuples', 'assignment']
x, y, z = w # assign letters to words

print(x, y, z)

