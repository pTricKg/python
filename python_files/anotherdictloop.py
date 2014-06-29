inpt = input('Enter your file name:')
if len(inpt) < 1 : inpt = "nineteen_eighty_four.txt"
try:
    inpt = open(inpt)
except:
    print('Whoops, file cannot be opened or found!')
    exit()

counts = dict()
for line in inpt:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

mylst = list(counts)
mylst.sort()
print(mylst)

for key in mylst:
    print(key, counts[key])

for key in counts:
    if counts[key] > 5:
        print('Words that appear at least 5 times:',key, counts[key])


##mylst = []
##for key, value in counts.items():
##    mylst.append([key, value])
##print(mylst)
##
##print(mylst.sort())
