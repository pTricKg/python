txttoread = open('romeo.txt')

counts = dict()

for line in txttoread:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        # above looks if word in dict, if it is add word to dict
        # if it isn't, default to 0

lst = list() # set temp list for sorting tuples

for key, val in counts.items():
    lst.append( (val, key) ) # append tuples into temp list

lst.sort(reverse=True) # reverse sort by val

for val, key in lst[:10]: # go through val up to 10
    print(key, val)
