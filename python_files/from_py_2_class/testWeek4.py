##message = 'Happy 29th!'
##new_message = ''
##
##for char in message:
##    if not char.isdigit():
##        new_message = new_message + char
##    else:
##        new_message = new_message + str((int(char) + 1) % 10)
##
##print(new_message)
##
##message = 'Happy 29th!'
##new_message = ''
##
##for char in message:
##    if char.isdigit():
##        new_message = new_message + str((int(char) + 1) % 10)
##    else:
##        new_message = new_message + char
##
##print(new_message)
##
##message = 'Happy 29th!'
##new_message = ''
##
##for char in message:
##    new_message = new_message + str((int(char) + 1) % 10)
##
##print(new_message)
##
##message = 'Happy 29th!'
##new_message = ''
##
##for char in message:
##    if char.isdigit():
##        new_message = new_message + str((int(char) + 1) % 10)
##    new_message = new_message + char
##
##print(new_message)
##

##def common_chars(s1, s2):
##    '''(str, str) -> str
##
##    Return a new string containing all characters from s1 that appear at least
##    once in s2.  The characters in the result will appear in the same order as
##    they appear in s1.
##
##    >>> common_chars('abc', 'ad')
##    'a'
##    >>> common_chars('a', 'a')
##    'a'
##    >>> common_chars('abb', 'ab')
##    'abb'
##    >>> common_chars('abracadabra', 'ra')
##    'araaara'
##    '''
##
##    res = ''
##
##    # BODY MISSING
####    for ch in s1:
####        if ch in s2:
####            res = res + ch
##    for ch in s2:
##        if ch in s1:
##            res = res + ch
##    
##    
##
##    return res
####
##
def common_chars(s1, s2):
    '''(str, str) -> str

    Return a new string containing all characters from s1 that appear at least
    once in s2.  The characters in the result will appear in the same order as
    they appear in s1.

    >>> common_chars('abc', 'ad')
    'a'
    >>> common_chars('a', 'a')
    'a'
    >>> common_chars('abb', 'ab')
    'abb'
    >>> common_chars('abracadabra', 'ra')
    'araaara'
    '''

    res = ''

    # BODY MISSING
    for ch in s1:
        if ch in s2:
            res = res + ch
    
    return res
