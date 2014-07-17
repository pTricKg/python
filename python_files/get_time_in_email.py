name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name, 'r')
mydict = {}
count = 0

for line in handle:
    # pull lines that start with From with space after
    if line.startswith("From "): # added  space to be sure not to include From:
        # split that line
        splt = line.split()

        time = splt[5]
        timesplt = time.split(':')
        
        tm = timesplt[0]
        
        count = count + 1
        
##        if tm not in mydict:
##            mydict[tm] = 1
##            
##        # then if it is, increment that by one
##        else:
##            mydict[tm] = mydict[tm] + 1
##            print(mydict)

        # or same as if else above:
        mydict[tm] = mydict.get(tm,0) + 1
        
    else:
        continue
lst = list()
##mcount = None
##mtime = None
for tm, count in mydict.items():
    lst.append((tm, count))
##    if mcount is None or count > mcount:
##        mcount = count
##        mtime = tm
##    lst.append(tm)
##    if tm in mydict:
##        count += 1
##    else:
##        count = count
##        
lst.sort()
##    print(lst)
##    print(lst, count)

    
# print(mydict)

# print(lst)

for tm, count in lst:
    print(tm, count)


    

