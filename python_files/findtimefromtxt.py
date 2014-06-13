name = input("Enter file:")

if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)

lst = list()

for lines in handle:
    if lines.startswith("From "):
        
        # find space before time starts
        fnd = lines.find(" ",lines.find(" ",lines.find\
                                        (" ",lines.find\
                                         (" ",lines.find\
                                          (" ",lines.find(" ")\
                                           + 1)+ 1)+ 1)+ 1)+ 1)
        
        time = lines[fnd + 1:fnd + 3]
        lst.append(time)
        
        counts = dict()
        for count in lst:
            counts[count] = counts.get(count, 0) + 1

tmplist = list()

for key, val in counts.items():
    tmplist.append( (key, val) ) # append tuples

tmplist.sort()

for key, val in tmplist:
    print(key, val)

    
        
        
    
