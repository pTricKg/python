def is_prime(x):
    while x % 1 == 0 and x % x == 0:
        return True
    else:
        return False

is_prime(2)
is_prime(263)


def is_prime(x):
    while x >= 2 and x != 2:
        if x % 1 == 0 and x % x== 0 and x / x != 1 and x % 2 != 0:
            return True
        else:
            return False
    if x == 2:
        return True
    else:
        return False
