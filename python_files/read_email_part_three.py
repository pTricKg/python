name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name, 'r')
mydict = {}
count = 0

for line in handle:
    if line.startswith("From "): #added  space to be sure not to include From:
        splt = line.split()

        print("This is email address:",splt[1]) # this is what we're looking for
        eml = splt[1]
        print(eml)
        count = count + 1
        print("this is count:",count)
        #mydict = mydict[splt[1]]
        mydict[splt[1]] = 1
        print(mydict)
        
        for eml in mydict:
            mydict[splt[1]] = mydict[splt[1]] + 1
        print(mydict)
    else:
        continue
print(count,mydict)

