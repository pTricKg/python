##num = 10
##
##while num < 100:
##    num = num * 2
##    print(num)

##s = 'yosemite'
s = ''
##i = 0


##for char in s:
##    print(char)


##while not (s[i] in 'aeiouAEIOU'):
##    print(s[i])
##    i = i + 1


##while i < len(s) and not (s[i] in 'aeiousAEIOU'):
##    print (s[i])
##    i = i + 1

    
##i = 0
##while i < len(s) and not (s[i] in 'aeiouAEIOU'):
##    print(s[i])
##    i = i + 1
##for char in s:
##    if not (char in 'aeiouAEIOU'):
##        print(char)

def get_answer(prompt):
    ''' (str) -> str

    Use prompt to ask the user for a "yes" or "no"
    answer and continue asking until the user gives
    a valid response. Return the answer.
    

    >>> based on user input so no prediction.
    '''
    answer = input(prompt)
    
    while not (answer == 'yes' or answer == 'no'):
        answer = input(prompt)

    return answer

    

def up_to_vowel(s):

    '''(str) -> str

    Return a substring of s from index 0 up to but
    not including the first vowel in s.

    >>>up_to_vowel('hello')
    'h'
    >>> up_to_vowel('there')
    'th'
    >>> up_to_vowel('cs')
    'cs'
    '''
    # before_vowel contains all the characters found in s[0:i].
    before_vowel = ''
    i = 0

    # Accumulate the non-vowels at the beginning of the string.
    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        before_vowel = before_vowel + s[i]
##        print(s[i])
        i = i + 1

    return before_vowel

def last_vowel(s):
    """(str) -> str
    Return the last vowel in s if one exists; otherwise, return None.
    >>> last_vowel("cauliflower")
    "e"
    >>> last_vowel("pfft")
    None
    """
    i = len(s) - 1
    while i >= 0:
        if s[i] in 'aeiouAEIOU':
            return s[i]
        i = i - 1

    return None



    