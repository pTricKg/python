##i = 0
##while i < 10:
##    print(i)
##    i = i + 1

##def countdown(n):
##    i = n
##    while i >= 1:
##        print(i)
##        i = i - 1
##        
##    else:
##        print('blastoff')

##def print_numbers(n):
##    i = 0
##    while i > n:
##        i = i - 1
##        print(i)
##        
##countdown(12)

##n = 200
##i = 0
##while i <= n:
##    i = i + 1
n = 12
##i = 1
##while True:
##    i = i * 2
##    n = n + 1
##    if i > n:
##        break


while n != 1:
    if n % 2 == 0: # the % means remainder, so this tests if n is even
        n = n / 2
    else:
        n = 3 * n  +  1
print(n)
