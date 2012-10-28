##s = 'Hi there!'
##for char in s:
##    print(char)
##
##def collect_vowels(s):    
##    '''(str) -> str
##    
##    Return the vowels from s. Do not treat the letter y as a vowel.
##    
##    >>>collect_vowels('Happy Anniversary!')
##    'aAiea'
##    >>>collect_vowels('xyz')
##    ''
##    '''
##
##    vowels = ''
##    for char in s:
##        if char in 'aeiouAEIOU':
##            vowels = vowels + char
##
##    return vowels
##
### accumulator = only runs when characters are present in passed string
##def count_vowels(s):
##    '''(str) -> int
##    Return the number of vowels in s. Do not treat the letter y as a vowel.
##    >>>count_vowels('Happy Anniversary!')
##    5
##    >>>count_vowels('xyz')
##    0
##    '''
##    num_vowels = 0 # count vowels
##    for char in s:
##        if char in 'aeiouAEIOU':
##            num_vowels = num_vowels + 1 # increments
##    return num_vowels
##
##collect_vowels('xyz')
##
##def has_vowel(s):
##    """(str) -> bool
##    
##    Return True if and only if s has at least one vowel, not including y.
##    
##    >>> has_vowel("Anniversary")
##    True
##    >>> has_vowel("xyz")
##    False
##    """
##    vowel_found = False
##    for char in s:
##        if char in 'aeiouAEIOU':
##            vowel_found = True
##            
##    return vowel_found
##
##digits = '0123456789'
##result = 100
##
##for digit in digits:
##    result = result - int(digit)
##
##print(result)
##
##digits = '0123456789'
##result = 0
##
##for digit in digits:
##    result = digit
##
##print(result)
##
##digits = '0123456789'
##result = ''
##
##for digit in digits:
##    result = result + digit * 2
##
##print(result)
##
##
##
##
##digits = '0123456789'
##result = 0
##
##for digit in digits:
##    result = result + int(digit)
##
##print(result)
##digits = '0123456789'
##result = 0
##
##for digit in digits:
##    result = digit
##
##print(result)
##digits = '0123456789'
##result = ''
##
##for digit in digits:
##    result = result + digit * 2
##
##print(result)
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
message = 'Happy 29th!'
new_message = ''

for char in message:
    if char.isdigit():
        new_message = new_message + str((int(char) + 1) % 10)
    new_message = new_message + char

print(new_message)
