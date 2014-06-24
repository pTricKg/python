import re

## re.search() returns True or False if string matches given regex

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:',line): # if line starts with From:
        print(line)

# ^ equals begin of line
# * any number of times
# . match any character
# \S match any non-whitespace character
# +  one or more times

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X-\S+',line): # if line starts with From:
        print(line)
