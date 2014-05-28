alphabet = "abcdefghijklmnopqrstuvxyz"

for letter in alphabet:
    print(letter)
    indice = alphabet.find(letter)
    print(indice)

    indx_list = [indice]

    print(indx_list)
    while len(indx_list) < len(alphabet):
        indx_list[indice] + 1# = indx_list.insert(indice, indice + 1)
        print(indx_list)
    break

    
    

### finding domain
data = #some email

# get position of @
atpos = data.find('@')

# get space after domain ending
sppos = data.find('',atpos)

# find domain from index after @ and up to space
host = data[atpos + 1:sspos]


# finding part of string with find and index
text = "X-DSPAM-Confidence:    0.8475"

begin = text.find('0')
end = text.find('5')

extracted = text[begin:end + 1]
convert = float(extracted)

print convert
