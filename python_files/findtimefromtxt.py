name = input("Enter file:")

if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)

lst = list()

for lines in handle:
    if lines.startswith("From "):
        print(lines)
        # find space before time starts
        fnd = lines.find(" ",lines.find(" ",lines.find\
                                        (" ",lines.find\
                                         (" ",lines.find\
                                          (" ",lines.find(" ")\
                                           + 1)+ 1)+ 1)+ 1)+ 1)
        print(fnd)
        time = lines[fnd + 1:fnd + 3]
        lst.append(time)
        print(lst)
        print(time)
        counts = dict()
        for count in lst:
            counts[count] = counts.get(count, 0) + 1

        print(counts)

        tmplist = list()

        for key, val in counts.items():
            tmplist.append( (key, val) ) # append tuples

        tmplist.sort()

        for key, val in tmplist:
            print(key, val)
            
        
    
