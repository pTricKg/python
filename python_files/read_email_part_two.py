fname = input("Enter file name: ")
#if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname, 'r')
count = 0

for line in fh:
    if not line.startswith("From"):
        continue
    count = count + 1
    print("this is count:",count)
    spc = line.find(" ")
    print(line[spc:])

print ("There were", count, "lines in the file with From as the first word")
