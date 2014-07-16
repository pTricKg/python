import string

""" Playing with Tuples two
    This uses tuples, dicts, and lists
    to count words; ten most common"""

opn = input("Enter file: ")

# file handling
if len(opn) < 1: opn = "nineteen_eighty_four.txt"
rd = open(opn)
#rd = rd.readlines()

count = dict()

for line in rd:
    line = line.translate(string.punctuation)
    line = line.lower()
    words = line.split()

    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

lst = list()
for key, value in count.items(): # key and value both interation variables
    lst.append((value, key))

lst.sort(reverse = True)

for key, value in lst[:10]:
    print(key, value)
