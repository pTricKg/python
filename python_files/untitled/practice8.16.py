squares = [x*2 for x in range(1,11) if x*2 % 2 == 0]

print (squares)

squares1 = [ x**2 for x in range(1,11)]
print (squares1)

print (filter(lambda x : x >= 30 and x <= 70, squares1))

