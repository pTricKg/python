# indices

s = 'abccdeffggh'

def count_adjacent_repeats(s):
    ''' (str) -> int

    Return the number of occurances of a character and an adjacent character
    being the same.

    >>> count_adjacent_repeats('abccdeffggh')
    3
    '''

    repeats = 0
##    for i in range(len(s)): ## throws error
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeats = repeats + 1

    return repeats

def shift_right(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the right
    and shift the last item to the first position.

    Precondition: len(L) >= 1
    '''

    last_item = L[-1]

##    for i in range(1, len(L)):
##        L[len(L) - i] = L[len(L) - i - 1]
    for i in range(1, len(L)):
        L[i] = L[i + 1]

    L[0] = last_item

def shift_left(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the left and shift the first item
    to the last position.

    Precondition: len(L) >= 1
    '''

    first_item = L[0]

    for i in range(1, len(L)):
        L[i - 1] = L[i]

    L[-1] = first_item

# Parallel lists and Strings

def count_matches(s1, s2):
    ''' (str, str) -> int

    Return the number of positions in s1 that contain the
    same character at the corresponding position of s2.

    Precondition: len(s1) == len(s2)

    >>> count_matches('ate', 'ape')
    2
    >>> count_matches('head', 'hard')
    2
    '''

    num_matches = 0 # accumulator for matches indices

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            num_matches = num_matches + 1

    return num_matches


def sum_items(list1, list2):
    ''' (list of number, list of number) -> list of number

    Return a new list in which each item is the sum of the items at the
    corresponding position of list1 and list2.

    Precondition: len(list1) == len(list2)

    >> sum_items([1, 2, 3], [2, 4, 2])
    [3, 6, 5]
    '''

    sum_list = [] #empty list to be filled

    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])

    return sum_list

def calculate_average(asn_grades):
    ''' (list of list of [str, number]) -> float

    Return the average of the grades in asn_grades.

    >>> calculate_average([['A1', 80], ['A2', 90]])
    85.0
    '''

    total = 0
    for item in asn_grades:
        total = total + item[1]

    return total / len(asn_grades)


def averages(grades):
    '''
    (list of list of number) -> list of float

    Return a new list in which each item is the average of the
    grades in the inner list at the corresponding position of
    grades.

    >>> averages([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
    [75.0, 85.0, 90.0]
    '''

    averages = []

    for grades_list in grades:
        # Calculate the average of grades_list and append it
        # to averages.

        total = 0
        for mark in grades_list:
            total = total + mark

        averages.append(total / len(grades_list))

    return averages


## loop play

##for i in range(3, 10):
##    for h in range(1, 4):
##        print(i, h)


def mystery(lst):
    for sublist in lst:
        total = 0
        for num in sublist:
            total = total + num
            
    return total
    

print(mystery([[10, 20], [20], [40, 10]]))

