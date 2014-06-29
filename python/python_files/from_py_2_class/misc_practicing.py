##x = 2
##y = 3 - x
##x = 3
##def f(y):
##    x = y * 3
##    return y + x

##start = 'L'
##middle = 8
##end = 'R'

##def swap_words(two_words):
##    '''(str) -> str
##
##    Precondition: two_words is a string containing two words separated by one space.
##
##    Return a new string where the words are in reverse order, again separated by
##    one space.
##
##    >>> swap_word('Hello World')
##    World Hello
##    '''
##
##    first = two_words[:two_words.find(' ')]
##    second = two_words[two_words.find(' ') + 1:]
####    print(second + ' ' + first)
##    return second + ' ' + first

## 6

##def count_max_letters(s1, s2, letter):
##    '''(str, str, str) -> int
##
##    s1 and s2 are strings, and letter is a string of length 1.  Count how many
##    times letter appears in s1 and in s2, and return the bigger of the two
##    counts.
##
##    >>> count_max_letters('hello', 'world', 'l')
##    2
##    >>> count_max_letters('cat', 'abracadabra', 'a')
##    5
##    '''
##
##    return max(s1.count(letter), s2.count(letter)) # CODE MISSING HERE

## 7
##def same_length(L1, L2):
##    '''(list, list) -> bool
##
##    Return True if and only if L1 and L2 contain the same number of elements.
##    '''
##    if len(L1) == len(L2):
##        return True
##    else:
##        return False
##
#### 9
##def reverse(s):
##    '''(str) -> str
##
##    Return the reverse of s.
##
##    >>> reverse('abc')
##    'cba'
##    >>> reverse('a')
##    'a'
##    >>> reverse('madam')
##    'madam'
##    >>> reverse('1234!')
##    '!4321'
##    '''
##
##    result = ''
##    i = len(s) - 1
##    while i >= 0:
##        result = result + s[i]
##        i = i - 1# CODE MISSING HERE
##
##    return result
##
#### 10
##def get_keys(L, d):
##    '''(list, dict) -> list
##
##    Return a new list containing all the items in L that are keys in d.
##
##    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
##    ['a', 1]
##    '''
##
##    result = []
##    for k in d:# CODE MISSING HERE
##        if k in L:
##            result.append(k)
##
##    return result

#### 11
def count_values_that_are_keys(d):
    '''(dict) -> int

    Return the number of values in d that are also keys in d.

    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 3})
    3
    >>> count_values_that_are_keys({1: 1})
    1
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 0})
    2
    >>> count_values_that_are_keys({1: 2})
    0
    '''

    result = 0
    for k in d:
        if d in [d]:# CODE MISSING HERE
            result = result + 1

    return result

#### 12

## 13
##def get_negative_nonnegative_lists(L):
##    '''(list of list of int) -> tuple of (list of int, list of int)
##
##    Return a tuple where the first item is a list of the negative ints in the
##    inner lists of L and the second item is a list of the non-negative ints
##    in those inner lists.
##
##    Precondition: the number of rows in L is the same as the number of
##    columns.
##
##    >>> get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]])
##    ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
##    '''
##
##    nonneg = []
##    neg = []
##    for row in range(len(L)):
##        for col in range(len(L)):
##            # CODE MISSING HERE
##            if L[row][col] < 0:
##                neg.append(L[row][col])
##
##            nonneg.append(L[row][col]) ## Nope
##            if L[row][col] < 0:
##                neg.append(L[row][col])
##            else:
##                nonneg.append(L[row][col]) ## Yup
##            if L[row][col] > 0:
##                nonneg.append(L[row][col])
##            elif L[row][col] < 0:
##                neg.append(L[row][col])
##            else:
##                nonneg.append(L[row][col])  ## Yup
##            if 0 <= L[row][col]:
##                nonneg.append(L[row][col])
##            else:
##                neg.append(L[row][col])  ## Yup
##            if L[row][col] > 0:
##                nonneg.append(L[row][col])
##            else:
##                neg.append(L[row][col])  ## Nope


##    return (neg, nonneg)

## 14
def add_to_letter_counts(d, s):
    '''(dict of {str: int}, str) -> NoneType

    d is a dictionary where the keys are single-letter strings and the values
    are counts.

    For each letter in s, add to that letter's count in d.

    Precondition: all the letters in s are keys in d.

    >>> letter_counts = {'i': 0, 'r': 5, 'e': 1}
    >>> add_to_letter_counts(letter_counts, 'eerie')
    >>> letter_counts
    {'i': 1, 'r': 6, 'e': 4}
    '''

    for c in s:
        # CODE MISSING HERE
        d['': 0] = c + s
