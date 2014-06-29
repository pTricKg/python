##num = int(input())
##my_list = [int(input()) for _ in range(num)]

##num = input("Enter a number: ")
##my_list = [int(s) for s in num.split()]
##my_list.append(num)
#n = int(input("Enter a number: "))
##n = 0
##l = [int(input("Enter a number: ")) for _ in range(n)]

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    else:
        
        my_list = [int(s) for s in num.split()]
        for num in my_list:
            largest = num
            smallest = num
            if num > largest:
                largest = num
                continue
            if num < smallest:
                smallest = num
                continue
    print (num, largest, smallest)
    

print ("Maximum is",largest)
print ("Minimum is",smallest)
