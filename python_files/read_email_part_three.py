name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name, 'r')
mydict = {}
count = 0

for line in handle:
    # pull lines that start with From with space after
    if line.startswith("From "): #added  space to be sure not to include From:
        #split that line
        splt = line.split()

        # pull out index 1 of split string
        print("This is email address:",splt[1]) # this is what we're looking for
        # set that to variable
        eml = splt[1]
        print(eml)
        # increment counter
        count = count + 1
        print("this is count:",count)
        #mydict = mydict[splt[1]]
        
        print(mydict)
        print(eml in mydict)
        # previous mistake was adding to dictionary without
        # first checking if it is there or not
        if eml not in mydict:
            mydict[eml] = 1
        # then if it is, increment that by one
        else:
            mydict[eml] = mydict[eml] + 1
            print(mydict)
                   
    else:
        continue


print("Final count:",count,"Final dictionary:",mydict)
