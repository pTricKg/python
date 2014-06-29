##while True:
##    my_list = []
##    num = input("Enter a number: ")
##    print(my_list)
##    print(num)
##    for n in num:
##        my_list = my_list.append(n)
##        my_list.append(my_list)
##        print(n)
##        print(my_list)
##    continue
##    break

##while True:
##    line = input('>')
##    if line[0]=='#':
##        continue
##    if line=='done':
##        break
##    print(line)
##print('Done')

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    #l = [int(input()) for i in range(num)]
    my_list = [int(num) for i in num.split()]
    my_list[0]= my_list.append(num)
    print (my_list)

print (my_list,"Maximum", largest)

##line = input("number: ")
##numbers = [int(s) for s in line.split()]
##
##print(line, numbers)
