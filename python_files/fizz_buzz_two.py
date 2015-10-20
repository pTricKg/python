print("Going to print fizz if number divisible by 3 and buzz if divisible 5\
, fizzbuzz if both.")

num = 0

count_fizz = 0
count_buzz = 0

while num < 100:
    num += 1
    if num % 5 == 0 and num % 3 == 0:
        print(num, '= fizzbuzz')
    ## check if divisible by 3
    elif num % 3 == 0:
        count_fizz += 1
        print(num, '= fizz')
    ## check if divisible by 5
    elif num % 5 == 0:
        count_buzz += 1
        print(num, '= buzz')
    else:
        print(num)
print("Fuzz count: ", count_fizz)
print("Buzz count: ", count_buzz)
