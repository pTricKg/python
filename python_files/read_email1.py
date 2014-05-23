fname = input("Enter file name: ")
fh = open(fname, 'r')
count = 0                           # remember that this needs to outside of loop
                                    # doesn't work otherwise
flts_totl = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue                    # continue returns to loop
    
    count = count + 1               # counting iterations
    flt0 = line.find(" ")
    print (flt0)
    flt = line[19:]                 # extract float still in str format
    print (flt, count)              # checking
    flts = float(flt)               # making float from str
    print (type(flts))              # checking again for float type
    flts_totl = flts_totl + flts    # incrementally adding for average
    print (flts_totl)               # checking    
    avg = flts_totl / count         # getting average
    print (avg)                     # checking one last time

print ("Done")
print ("Average spam confidence:", avg)


