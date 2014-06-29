def set_range(a, b, c):
##    if a > b:  # a excludes b
##        if b > c:  # a excludes c
####            if b > c:  #b excludes c
##            return a - c #so range = a-c
####            else:
####                return a - b
##        else:
##            return a - b
####            if c > b:
####                return c - a
####            else:
####                return c - b
##    else:
##        if a > c:
##            return b - c
####            
##        else:
##            if c > a:
##                return b - a
##            else:
##                return c - a
    if a > b:
        if a > c:
            if b > c:
                return a - c
            else:
                return a - b
        else:
            return c - b
    else:
        if a > c:
            return b - c
        else:
            if c > b:
                return c - a
            else:
                return b - a
  
print(set_range(10, 4, 7))

print(set_range(1.1, 7.4, 18.7))



