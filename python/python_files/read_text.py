fname = input("Enter file name: ")
fh = open(fname, 'r')
lst = list()
for line in fh:
    print("\nThis is line:",line)
    line = line.split()
    print("This is line after split:",line)
    if line[0] in lst:
        continue
    else:
        lst.append(line)
        print("\nThis is list:",lst)
        
#print (line.rstrip())
