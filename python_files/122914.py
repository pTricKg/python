count = 0
word = "Hello"
while count < 5:
    count += 1
    print(str(count)  + " " + word)
    for e in word:
        letter = e
        print(letter)
        if letter is in ["a","e","i","o","u"]:
            print("Bazinga")
    
