
## test if friends name begins with D or N.

def is_friend(name):
    if name[0] == 'D':
        return True
    else:
        if name[0] == 'N':
            return True
        else:
            return False

print(is_friend('Daniel'))
print(is_friend('Nicole'))
print(is_friend('Frank'))


##<expression> or <expression>
## if the first expression evaluates to True,
##  then second expression is not evaluated
## if the first expression is False,
##  then the value is the value of second expression
##def is_friend(name):
##    return name[0] == 'D' or name[0] == 'N'
##
##print True or this_is_an_error
