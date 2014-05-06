my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()

## practicing
my_file = open("output.txt","r+") # r+ will read and write to file

# "w" as second param/arg will write only
# "r" as second param/arg will read only
# "r+" as second param/arg will read and write
# "a" will append new data to file

# iterates through my list exponentiating i for each from 1 to 11
# then, opens list for read and write
# then, closes to complete
my_list = [i**2 for i in range(1,11)]

my_list = open("output.txt", "r+")

# Add your code below!
for i in my_list:
    my_list.write(str(my_list) + "\n")
    
my_list.close()

# printing result
my_file = open("output.txt","r")

print my_file.read()
my_file.readline()
my_file.close()

# another example for why to close file for python
# Open the file for reading
read_file = open("text.txt", "r")

# Use a second file handler to open the file for writing
write_file = open("text.txt", "w")
# Write to the file
write_file.write("Not closing files is VERY BAD.")

write_file.close()

# Try to read from the file
print read_file.read()
read_file.close()

## using python read and write methods
'''__enter__() and __exit__(). The details aren't important,
but what is important is that when a file object's __exit__() method is invoked, it automatically closes the file.
How do we invoke this method? With with and as.'''

'''with open("file", "mode") as variable:
    # Read or write to the file'''

with open("text.txt", "w") as textfile:
	textfile.write("Success!")

# checking if file is closed and closing if false
with open("text.txt", "w") as textfile:
	textfile.write("Your momma's got a glass eye with a fish in it!")
	
if textfile.closed == False:
    textfile.close()
print textfile.closed
