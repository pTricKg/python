inpt = input('Enter your file name:')
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
