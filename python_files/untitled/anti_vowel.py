def anti_vowel(x):
    for char in x:
##        x.lower()
        for char in "aeiouAEIOU":
            x = x.replace(char, '')         
        return x
    return x

print(anti_vowel("HeY lOoK Words!"))

print(anti_vowel("Patrick Gorman"))
