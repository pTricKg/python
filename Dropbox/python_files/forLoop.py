##for loop
##my_list = [1,9,3,8,5,7]
##for number in my_list:
##    print 2 * number


##start_list = [5, 3, 1, 2, 4]
##square_list = []
##
##for number in start_list:
##    square_list.append(number ** 2)
##	
##square_list.sort()
##print(square_list)
##
### Assigning a dictionary with three key-value pairs to `residents`
##residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
##
##print residents['Puffin'] # Prints Puffin's room number
##
### Your code here
##print residents['Sloth']
##print residents['Burmese Python']
##
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print (menu['Chicken Alfredo'])
##
### Your code here: Add some dish-price pairs to 'menu'
menu['Nachos Supreme'] = 9.50
menu['Elk Burrito'] = 11.50
menu['Hot Dog Casserole'] = 22.99
##
print ("There are " + str(len(menu)) + " items on the menu.")
print (menu)
##
### key - animal_name : value - location 
##zoo_animals = { 'Unicorn' : 'Cotton Candy House',
##'Sloth' : 'Rainforest Exhibit',
##'Bengal Tiger' : 'Jungle House',
##'Atlantic Puffin' : 'Arctic Exhibit',
##'Rockhopper Penguin' : 'Arctic Exhibit'}
### A dictionary (or list) declaration may break across multiple lines
##
### Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
##del zoo_animals['Unicorn']
##
### Your code here
##del zoo_animals['Sloth']
##del zoo_animals['Bengal Tiger']
##zoo_animals['Rockhopper Penguin'] = 'Cold Country'
##print zoo_animals

#del based on key // .remove() based on value attached to key
#
##inventory = {'gold' : 500,
##'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
##'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']}
##
### Adding a key 'burlap bag' and assigning a list to it
##inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
##
### Sorting the list found under the key 'pouch'
##inventory['pouch'].sort() 
### Here the dictionary access expression takes the place of a list name 
##
### Your code here
##inventory['pocket'] = ['seashell', 'strange berry', 'lint']
##inventory['backpack'].sort()
##inventory['backpack'].remove('dagger')
##inventory['gold'] = 550
##
##print(inventory)
##
###
##names = ["Adam","Alex","Mariah","Martine","Columbus"]
##
##for peeps in names:
##	print peeps
##
##Webster = {
##     "Aardvark" : "A star of a popular children's cartoon show.",
##     "Baa" : "The sound a goat makes.",
##     "Carpet": "Goes on the Floor.",
##     "Dab": "A small amount."
##    }
##
###    
##for sects in Webster:
##	print Webster["Aardvark"]
##	print Webster["Baa"]
##	print Webster["Carpet"]
##	print Webster["Dab"]
##
##A = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
##null = []
##for numb in A:
##	if (numb % 2 != 0):
##		null
##	else:
##		print numb
##
###looping through strings
##for c in "Codecademy":
##    print c
##    
### Empty lines to make the output pretty
##print
##print
##
##word = "Programming is fun!"
##
##for letter in word:
##    # Only print out the letter i
##    if letter == "i":
##        print letter
##
##
##prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
##stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
##for names in prices:
##	if names > 2:
##		print names
##	print "price :" + str()
##	print "stock :" + str()
##
