

def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''

    return len(dna)



def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''

    if len(dna1) > len(dna2):
        return True
    else:
        return False
    




def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    
    count = 0
    for char in dna:
        if char in nucleotide:
            count = count + 1
    return count
    


def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''
    
    if dna2 in dna1:
        return True
    else:
        return False

def is_valid_sequence(dna):
    '''(str) -> bool

    Return True if and only if the DNA sequence is valid.

    >>> is_valid_sequence('ABDGT')
    False
    >>> is_valid_sequence('ACGTA')
    True
    '''
    count = ''
    for char in dna:
        if char not in 'ATCG':
            count = count + char
            return False
    return True
            
       
            
# ATCG
#  A and T , C and G.

def insert_sequence(dna1, dna2, dna_index):
    '''(str, str, str) -> str

    Return DNA sequence obtained by inserting dna2 in dna1 at given dna_index.

    >>> insert_sequence('AGCTG', 'CG', 4)
    'AGCTCGG'
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    '''

    return dna1[:dna_index] + dna2 + dna1[dna_index:]
    

def get_complement(nucleotide):
    '''(str) -> str

    Return the nucleotide's complement.

    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    '''
    for char in nucleotide:
        
        if nucleotide == 'A':
            return 'T'
        elif nucleotide == 'T':
            return 'A'
        elif nucleotide == 'C':
            return 'G'
        elif nucleotide == 'G':
            return 'C'

def get_complementary_sequence(dna):
    '''(str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence.

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('CGAT')
    'GCTA'
    '''
    count = ''
    for char in dna:
        count = count + get_complement(char)
        
    return count
    
##    count = ''
##    for char in dna:
##        count = count + char
##        return get_complement(count)
##    return count

    
    

