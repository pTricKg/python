import random

##translate = dict()
##
##translate['one'] = 'uno'
##
##translate['two'] = 'dos'
##
##def get_inp():
##    usr = str(input("Give me number:"))
##
##    if usr != '':
##        if usr == 'one':
##            print(translate['one'])
##            get_inp()
##        elif usr != translate['one']:
##            print('Whoops')
##        
##    else:
##        print("Give me something")
##        get_inp()
##
##get_inp()

d = dict()

opn = open('romeo.txt')
val = ['dumb', 'as if', 'like, really', 'oh my gosh', 'shoot']

for words in opn:
    word = words.split()
##    print(word)
    d[words] = random.choice(word)
    print(d,'\n')
    print(words in d)
print(d,'\n')

