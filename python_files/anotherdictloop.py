import string

""" Testing dictionarys """

inpt = input('Enter your file name:')

if len(inpt) < 1 : inpt = "nineteen_eighty_four.txt"

try:
    inpt = open(inpt)
except:
    print('Whoops, file cannot be opened or found!')
    exit()

counts = dict()

for line in inpt:
    # add check for punctuation and remove if present
    for c in string.punctuation:
        line = line.replace(c,"")
    #line = line.translate(string.maketrans('',''),string.punctuation)
    # lowercase
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

mylst = list(counts) # make list
mylst.sort() # alphabetize
print(mylst)

for key in mylst:
    print(key, counts[key])

for key in counts:
    if counts[key] > 5:
        print('Word that appears at least 5 times:',key, '->', counts[key])


## This didnt't do what I needed
mylst = []

for key, value in counts.items():
    mylst.append([key, value])

print(mylst)

print(mylst.sort())
