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
# [] list inside
# ? prevents greedy search, will stop as soon match found(without find biggest
# string
# () extract from inside


import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X-\S+',line): # if line starts with From:
        print(line)

y = re.findall('[0-9]+',x) # find matching strings via regex
x = re.findall('\S+@\S+', x) # find email
z = re.findall('^From (\S+@\S+)',x)
