name = input("Enter file:")

if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)

lst = list()

counts = dict()

for lines in handle:
    if lines.startswith("From "):
        print(lines)
        # find space before time starts
##        fnd = tm.find(" ",tm.find(" ",tm.find\
##                                        (" ",tm.find\
##                                         (" ",tm.find\
##                                          (" ",tm.find(" ")\
##                                           + 1)+ 1)+ 1)+ 1)+ 1)
        fnd = lines.find(" ",lines.find(" ",lines.find\
                                        (" ",lines.find\
                                         (" ",lines.find\
                                          (" ",lines.find(" ")\
                                           + 1)+ 1)+ 1)+ 1)+ 1)
        print(fnd)
        time = lines[fnd + 1:fnd + 3]
##        lst.append(time)
##        print(lst)
        print(time)
        for count in time:
            counts[count] = counts.get(count, 0) + 1

        print(counts)
        
    
