# Bitwise

# playing with bits in python
# base 2 (normal counting is base 10)
one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

print twelve

# or to find a binary representation of number
# following prints out binary for 1 - 5
print bin(1)
print bin(2)
print bin(3)
print bin(4)
print bin(5)

# or to find base 8 or 16
oct()
hex()

# print using int() second parameter
print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
print int("11001001",2)

''' prints following
    1
    2
    7
    4
    5
    201 '''

# shifting bits left and right
shift_right = 0b1100 >> 2
shift_left = 0b1 << 2

0b1100 >> 2
0b1 << 2

print( bin(shift_right)) # output = 0b11
print( bin(shift_left)) # output = 0b100

# using and operator (&)
print (bin(0b1110 & 0b101))

''' the & operator can only result in a number
that is less than or equal to the smaller of the two values. 

     a:   00101010   42
     b:   00001111   15       
===================
 a & b:   00001010   10 '''

# using or operator (|)
print bin(0b1110 | 0b101)

'''| operator can only create results that are greater than or
equal to the larger of the two integer inputs.
    a:  00101010  42
    b:  00001111  15       
================
a | b:  00101111  47'''

# using XOR (^) operator
print bin(0b1110 ^ 0b101) # output 0b1011

'''urned on if either of the corresponding bits of the two numbers are 1,
but not both.

    a:  00101010   42
    b:  00001111   15       
================
a ^ b:  00100101   37
Keep in mind that if a bit is off in both numbers, it stays off
in the result. Note that XOR-ing a number with itself will
always result in 0.
'''

# using NOT (~) operator
print ~1 # output -2
print ~2 # output -3
print ~3 # output -4
print ~42 # output -43
print ~123 # output -124

'''quivalent to adding one to the number
and then making it negative.
'''

# using bit mask

# checks if fourth bit is on or off
def check_bit4(intgr):
    mask = 0b1000 # set mask to 4 bit from right with 1
    desired = intgr & mask # sets desired to masking 4 bit
    if desired > 0: # check if desired is turned on
        return "on"
    else:
        return "off"

'''check_bit4(0b1) # ==> "off"
check_bit4(0b11011) # ==> "on"
check_bit4(0b1010) # ==> "on" '''

# turn bits on with |
a = 0b10111011
mask = 0b100
desired = a | mask

print bin(desired) # output 0b10111111

# flip bits with ^ XOR
a = 0b11101110
mask = 0b11111111
desired = a ^ mask

print (bin(desired)) # 0b10001

# function to flip bit left
def flip_bit(number, n):
    a = number
    mask = (0b1 << (n - 1))  # have to subtract one from n to match first bit 
    desired = a ^ mask
    return bin(desired)
    
print (flip_bit(0b111,2))
