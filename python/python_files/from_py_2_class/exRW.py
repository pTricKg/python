##''' open(filename, mode) - opens files
##    mode: 'r' - opens for reading
##          'w' - opens for writing (erases what's there)
##          'a' - opens for appending (adds to what's there)
##          '''

# Methods: readline() - read and return next line w/ new line if present.
# readline() discards header too.
# return empty string when empty.
#       close()
#       read() - read entire file at once
#       readlines() - returns list of all lines in files

#  loop for reading entire file
filename = 'C:/Users/pTricKg/Dropbox/python_files/pythonProg/filename.txt'
flanders_file = open(filename, 'r')
flanders_file.readline()
line = flanders_file.readline()
while line != ' ':
    #print(line) # prints with empty lines after each
    print(line, end='') # add end='' in print statement to remove blank lines
    line = flanders_file.readline()

# loop for reading first section
line = filename.readline()
while line != '\n':
    print(line)
    line = flanders_file.readline()

# for loop
for line in flanders_file:
    print(line, end='')

# loop to go through list of lines(readlines())
flanders_file = open(filename, 'r')
lines = flanders_file.readlines()
for line in lines:
    print(line, end='')

# Writing

# Method: write(str) = write string to file w/o appending new line

import tkinter.filedialog
tkinter.filedialog.askopenfilename()
tkinter.filedialog.asksaveasfilename()





    

    
