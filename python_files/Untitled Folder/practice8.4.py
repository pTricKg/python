str = 'platypus'
def reverse(str):
    i = 0
    while i <= len(str):
        new = ""
        new += str[-i] + new[:-1]
        i+=1
        print(new)
