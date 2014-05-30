fname = input("Enter file name: ")
fh = open(fname, 'r')
lst = list()
for line in fh:
    print("\nThis is line:",line)
    line = line.split()
    print("This is line after split:",line)
    for word in line:
        if word in lst:
            continue
        else:
            lst.append(word) #this seems to do the trick
    print("this is list:",lst)
final = sorted(lst)
print("this is list sorted:",final)
    #this is putting a list inside a list: not wanted result
##    lst.append(line)
##    print(lst)
    
