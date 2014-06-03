# This pulls emails from text given and splits out domain as well

fname = input("Enter file name: ")

if len(fname) < 1 : fname = "mbox-short.txt" # this adds file if no input

fh = open(fname, 'r')
count = 0

for line in fh:
    if line.startswith("From "): #added  space to be sure not to include From:
        splt = line.split()

        print("This is email address:",splt[1]) # this is what we're looking for
        count = count + 1
        print("this is count:",count)
        slt2 = splt[1].split('@')
        domain = slt2[1]
        print("this is domain:",domain)
    else:
        continue
    

print ("There were", count, "lines in the file with From as the first word")
