##factorial(n) =
##    n * (n - 1) * (n - 2)

def factorial(n):
    result = 1
    while n >= 1:
        result = result * n
        n = n - 1
    return result

print(factorial(4))
