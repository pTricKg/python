""" Tuples play """

nme = tuple('patrick')

print(nme)

cnt = 0

for l in nme:
    cnt += 1
    print(cnt)
    if l is 'a' or l is 'i':
        l = '' + nme[cnt - 1]
        print(l)
    print(nme)
    



