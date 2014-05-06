##def mystery(s):
##    i = 0
##    result = ''
##
##    while not s[i].isdigit():
##        result = result + s[i]
##        i = i + 1
##
##    return result
##
##def example(L):
##    ''' (list) -> list
##    '''
##    i = 0
##    result = []
##    while i < len(L):
##        result.append(L[i])
##        i = i + 3
##    return result
##
##def compress_list(L):
##    ''' (list of str) -> list of str
##
##    Return a new list with adjacent pairs of string elements from L
##    concatenated together, starting with indices 0 and 1, 2 and 3,
##    and so on.
##
##    Precondition: len(L) >= 2 and len(L) % 2 == 0
##
##    >>> compress_list(['a', 'b', 'c', 'd'])
##    ['ab', 'cd']
##    '''
##    compressed_list = []
##    i = 0
##
##    while i < len(L):
##        compressed_list.append(L[i] + L[i + 1])
##        # MISSING CODE HERE
##        i = i + 1
##
##    return compressed_list
##
##def while_version(L):
##    ''' (list of number) -> number'''
##    i = 0
##    total = 0
##
##    while i < len(L) and L[i] % 2 != 0:
##        total = total + L[i]
##        i = i + 1
##
##    return total
##
##def cap_song_repetition(playlist, song):
##    '''(list of str, str) -> NoneType
##
##    Make sure there are no more than 3 occurrences of song in playlist.
##    '''
####    while playlist.count(song) > 3:
####        playlist.remove(song)
####    while playlist.count(song) > 3:
####        playlist.pop(playlist.index(song))
##    
##    
##a = [1, 2, 3]
##b = [1, 2, 3]
##
##b[1] = 'AB'
##a[1] = a[1][0]
##print(a, b)

##a = [1, 2, 3]
##b = [1, 2, 3]
##
##b[-2] = 'A'
##print(a, b)
##
##a = [1, 2, 3]
##b = [1, 2, 3]
##
##a[1] = 'A'
##print(a, b)
####
##a = [1, 2, 3]
##b = [1, 2, 3]
##
##a = [1, 'A', 3]
##b = [1, 'A', 3]
##print(a, b)

##def increment_items(L, increment):
##    i = 0
##    while i < len(L):
##        L[i] = L[i] + increment
##        i = i + 1
##
##values = [1, 2, 3]
##print(increment_items(values, 2))
##print(values)

##values = []
##for num in range(1, 4):
##    values.append(num * 3)
##print(values)
##values = []
##for num in range(3, 9, 3):
##    values.append(num)
##print(values)

##values = []
##for num in range(3, 10, 3):
##    values.append(num)
##print(values)

##values = []
##for num in range(1, 3):
##    values.append(num * 3)
##print(values)
##i = 0
##for num in range(1523, 10503, 2):
##    sum = i + num
##print(sum)

def while_version(L):
    ''' (list of number) -> number'''
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
        total = total + L[i]
        i = i + 1

    return total

def for_version1(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True
 
    return total

def for_version2(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
        elif not found_even:
            found_even = True

    return total

def for_version3(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
            found_even = True

    return total

def for_version5(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
        found_even = True

    return total
    
        
