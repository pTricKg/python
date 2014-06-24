import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:',line): # if line starts with From:
        print(line)

# ^ equals begin of line
# * any number of times
