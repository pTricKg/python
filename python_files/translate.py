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
val = 0

for words in opn:
    
    d[words] = words
    print(d,'\n')
