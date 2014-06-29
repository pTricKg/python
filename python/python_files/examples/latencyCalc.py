#1 byte = 8 bits
#light switch = 1 bit
# 2GB = 2**30 * 2 * 8
#latency = time to retrieve a value(2GB DRAM = 12 nanoseconds)
#CostPerBit___Latency___Latency-Distance
#$ 0.50        1 second    _______km(distance traveled--Light Switch
#$ 0.001       <0.4ns       _______m ---CPU Register
#$ 0.58n$       12ns        _______m ---DRAM
#$_____n$       7ms         _______km ---HDrive
# Speed of Light = 300k km/s

#Calculate Latency
##print(1 * 300000)
##print(.4**-9 * 300000 * 1000)
##print((12**9) * 300000 * 1000)

#300000
#.12
#3.6m
#print(.4 ** -9)
#print((0.4 ** -9) * 300000 / 1000)

#1.0 TB
# 8*2^40 bits ~ 8.8 trillion bits
# latency = 7milliseconds/1/1000th second
#0..1n$/2098km
##print(8*(2^40))
##print(8x2^40)

#loops on lists
#while<test>:
#   <block>
##def print_all_elements(p):
##    i = 0
##    while (i < len(p)):
##        print(p[i])
##        i = i + 1
##print_all_elements(32)

#for <name> in <list>:
#    <Block>
# elements = e

def sum_list(p):
    result = 0 #acts a recorder i believe
    for e in p:
        result = result + e
    return result
        

print(sum_list([1, 7, 4]))
