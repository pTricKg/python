word = "supercalafragilous"

index = 0

# print each letter: first to last
while index < len(word):
    new_word = word[index]
    print (new_word)
    index = index + 1

# print each letter: last to first
while index < len(word):
    new_word1 = word[index - 1]
    print (new_word1)
    index = index - 1
    # IndexError

# using for in even better
for i in word:
    print (i)

# prints word backwards while ~
while index < len(word):
    word1 = word[::-1]
    print (word1)
    index = index + 1

##while index < len(word):
    word1 = word[index:-1:1]
    print (word1)
    index = index + 1
    # output 
##supercalafragilou
##upercalafragilou
##percalafragilou
##ercalafragilou
##rcalafragilou
##calafragilou
##alafragilou
##lafragilou
##afragilou
##fragilou
##ragilou
##agilou
##gilou
##ilou
##lou
##ou
##u 
    


    
