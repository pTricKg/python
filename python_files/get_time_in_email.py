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

        mydict[tm] = mydict.get(tm,0) + 1
        
    else:
        continue
lst = list()

for tm, count in mydict.items():
    lst.append((tm, count))

lst.sort()

for tm, count in lst:
    print(tm, count)


    

