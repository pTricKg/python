opn = input("Enter file: ")

if len(opn) < 1: opn = "nineteen_eighty_four.txt"
rd = open(opn)

#print(rd)
print(opn)
words = str(rd)
words = words.split()
print(words)
lst = list()
print(lst)
for word in rd:
    lst.append((len(word), word))

lst.sort(reverse = True)

rev = list()
for length, word in lst:
    rev.append(word)

#print(rev)
