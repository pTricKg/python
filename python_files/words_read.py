# Read from file
 

fname = input("Enter file name: ")
fh = open(fname, 'r')
rd = fh.read().strip()

# upper case
print (rd.upper())

# lower case
print (rd.lower())

# seperate words into seperate strings
print (rd.split())

# mbox-short.txt
