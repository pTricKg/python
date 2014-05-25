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
    
