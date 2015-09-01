word = input("Give me a word and i'll give you x's for all vowels >")
##for i in word:
##    if i == "e":
##        i = "y"
##        word = word[i]
##        print(i)
##        
##    print(word)

count = 0
while count < len(word):
    
    for i in word:
        if i == "a":
            word = word.replace(i,"x")
        elif i == "e":
            word = word.replace(i,"x")
        elif i == "i":
            word = word.replace(i,"x")
        elif i == "o":
            word = word.replace(i,"x")
        elif i == "u":
            word = word.replace(i,"x")
        elif count == 1:
            n = i.upper()
            print(i)
            word = word.replace(i, n)
        elif count == len(word) - 2:
            n = i.upper()
            print(i)
            word = word.replace(i, n)
    
        count += 1
        print(count)    
            
print(word)

## or "i" or "o" or "a" or "u"
