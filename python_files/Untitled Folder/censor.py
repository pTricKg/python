def censor(text,word):
    new = text.split() # splits each string from whole
    print(new) # test
    for i in range(0,len(new)):
        if new[i] == word: # check if word equals new 
            new[i] = "*" * len(word) # sets new to asterisk for each char
    new_text = " ".join(new) # puts text back together
    print(new_text)
    return new_text

censor("this hack is wack hack","wack")
