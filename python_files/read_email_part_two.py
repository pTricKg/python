fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname, 'r')
count = 0

for line in fh:
    if line.startswith("From "): #added  space to be sure not to include From:
        splt = line.split()
##        spc = line.find(" ")
##        spc2 = line.find(" ", spc)
##        #print(line[spc:" "])
##        print(line[spc:])
        #print(splt)
        print(splt[1]) # this is what we're looking for
        count = count + 1
        print("this is count:",count)
    else:
        continue
    

print ("There were", count, "lines in the file with From as the first word")
