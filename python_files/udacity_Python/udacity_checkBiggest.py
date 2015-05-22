def biggest(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

print(biggest(3,12,5))

##def bigger(a,b):
##    if a > b:
##        return a
##    else:
##        return b
##
##def biggest(a,b,c):
##    return bigger(bigger(a,b),c)
