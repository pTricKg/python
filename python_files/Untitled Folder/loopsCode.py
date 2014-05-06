##Loops
choice = raw_input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")
count = 0

while True:
    print count
    count += 1
    if count >= 10:
        break

##guessing game 1
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    count += 1
    if num == 5:
        print "Sorry, you lose!"
        break
else:
    print "You win!"


##guessing game 2
from random import randrange

random_number = randrange(1, 10)

count = 0
# Start your game!
while count <= 3:
    guess = int(raw_input("Enter a guess: "))
    count = count + 1
    if guess == random_number:
        print "You Win!"
        break
else:
    print "You lose."

##appending list loop
hobbies = []

# Add your code below!
for x in range(3):
    hobby = raw_input("Name your favorite hobby?")
    hobbies.append(hobby)
    print hobbies

##printing strings loop
thing = "spam!"

for c in thing:
    print c

word = "eggs!"

# Your code here!
for x in word:
    print x

##Loop for swapping char in str
s = "A bird in the hand..."

# Add your for loop
for c in s:
    if c == 'a' or c == 'A':
        print 'X',
    else:
        print c ,

##Loop for printing out lists
s = "A bird in the hand..."

# Add your for loop
for c in s:
    if c == 'a' or c == 'A':
        print 'X',
    else:
        print c ,
