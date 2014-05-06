# mutability and aliasing

##lst = [0, 2, 4, 6, 8, 10]
##
##lst[2] = 5 # modifies variable in memory
##
##lst = [0, 2, 4, 6, 8, 10]
##list2 = list1 # modifies variable
##list1[-1] = 17 # aliasing to asign another variable to memory
##print(list1[-1])
##print(list2[-1])
##
##
##list1 = [1, 2, 3]
##list2 = list1
##list2.append(4)


##def double_even_indices(lst):
##    '''(list of int) -> NoneType
##
##    Double every other int in lst, starting at index 0.
##    '''
##
##    i = 0
##    while i < len(lst):
##        lst[i] = lst[i] * 2
##        i = i + 2
##
##list1 = [11, 12, 13, 14, 15, 16, 17]
##print(list1)
##double_even_indices(list1)
##print(list1)
##
##
##def double_first_element(lst):
##    if len(lst) > 0:
##        lst[0] = lst[0] * 2
##
##list1 = [10, 100, 1000]
##double_first_element(list1)

##def double_first_element(lst):
##    if len(lst) > 0:
##        lst[0] = lst[0] * 2
##
##list1 = [10, 100, 1000]
##double_first_element(list1)

##def interrupted(s):
##    s[-1] = "-"
##    
##greeting = "how are you"
##interrupted(greeting)
##print(greeting)

# range

for num in range(10):
    print(num)

0
1
2
3
4
5
6
7
8
9

for i in range(len(s)):
	print(i)

0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15

for i in range(1, len(s)):
	print(i)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15    

for i in range(1, len(s), 2):
	print(i)

	
1
3
5
7
9
11
13
15

def print_every_third_char(s):
    for i in range(0, len(s), 3):
        print(i)
