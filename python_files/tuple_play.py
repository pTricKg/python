""" Playing with Tuples  """

opn = input("Enter file: ")

# file handling
if len(opn) < 1: opn = "nineteen_eighty_four.txt"
rd = open(opn)
rd = rd.readlines()
#print(rd)
#print(opn)

words = str(rd)
words = words.split()
print("word list: ",words)

lst = list()
#print(lst)
# loop through words to get length of words
for word in words:
    lst.append((len(word), word))
print("here is first loop: ",lst)
lst.sort(reverse = True)

rev = list()
# loop through tuple in list append in order of length
for length, word in lst:
    rev.append(word)

print("here is final loop: ",rev)
