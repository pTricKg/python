'''A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
'''


def is_valid_word(wordlist, word):
    ''' (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    >>> is_valid_word(['BEAT', 'BOOM', 'BANG'], 'BOOM')
    True
    >>> is_valid_word(['BEAT', 'BOOM', 'BANG'], 'BLING')
    False
    '''
    if word in wordlist:
        return True
    else:
        return False


def make_str_from_row(board, row_index):
    ''' (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'XSOB'
    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B'], ['D', 'U', 'D', 'E']], 2)
    'DUDE'
    '''
    list = []
    for i in range(len(board)):
        list.append(board[row_index])
        list = ''.join(board[row_index])
        return list

def make_str_from_column(board, column_index):
    ''' (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 2)
    'TO'
    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 3)
    'TB'
    '''
    list1 = []
    for j in range(len(board)):
        list1 = board[0][(column_index)] + board[1][(column_index)]
        return list1
        

def board_contains_word_in_row(board, word):
    ''' (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'BOB')
    False
    '''

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    ''' (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'TO')
    True
    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'XA')
    False
    '''
    for column_index in range(len(board)):
        if word in make_str_from_column(board, column_index):
            return True
    return False


def board_contains_word(board, word):
    '''(list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    '''
    b = len(board)
    for word in b:
        for row_index in range(len(board)):
            if word in make_str_from_row(board, row_index):
                return True
        for column_index in range(len(board)):
            if word in make_str_from_column(board, column_index):
                return True

        return False


def word_score(word):
    '''(str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character in word
                 7-9: 2 points per character in word
                 10+: 3 points per character in word

    >>> word_score('DRUDGERY')
    16
    >>> word_score('UP')
    0
    >>> word_score('PUNK')
    4
    >>> word_score('ENVIRONMENT')
    33    
    '''
    count = 0
    for char in word:
        if len(word) < 3:
            count = len(word) * count
            return count
        elif len(word) >= 3 and len(word) < 7:
            count = 1
            count = len(word) * count
            return count
        elif len(word) >= 7 and len(word) < 10:
            count = 2
            count = len(word) * count
            return count
        elif len(word) >= 10:
            count = 3
            count = len(word) * count
            return count


def update_score(player_info, word):
    '''([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    '''
    prev_score = 0
    for m in range(len(player_info)):
        prev_score = player_info[1:2]
        return prev_score
        new_score = prev_score + word_score(word)
        return new_score
    print(new_score)    


def num_words_on_board(board, words):
    '''(list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    '''
    count = 0
    for words in range(len(board)):
        for row_index in range(len(board)):
            if words in make_str_from_row(board, row_index):
                count = count + 1
        for column_index in range(len(board)):
            if words in make_str_from_column(board, column_index):
                count = count + 1
        return count


def read_words(words_file):
    ''' (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    '''
    
##    words = open(words_file, "r")

    lines = words_file.read()
    while lines == ''.upper():
        lines = words_file.read()
        
##    for lines in words:
##        return lines
##    print(lines)

    
##    word = open("wordlist1.txt", "r")
##
##    lines = word.read()
##    for lines in word:
##        return lines
##    print(lines)

def read_board(board_file):
    ''' (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    '''
    
##    bfile = open(board_file, "r")

    blines = board_file.read()
    while blines > '':
        blines = board_file.read()
##    for blines in bfile:
##        return blines
##    print(blines)
    
        
