###import library
##from datetime import datetime
##now = datetime.now()
##print(now)
###print now.year
###print now.month
###print now.day
##
###cleaning up date
##day = str(now.day)
##month = str(now.month)
##year = str(now.year)
##mdy = month + "/" + day + "/" + year
##print(mdy)
##
###cleaning up time
##min = str(now.minute)
##hour = str(now.hour)
##sec = str(now.second)
##
##print hour + ":" + min + ":" + sec
##
#PygLatin

##\**print("Welcome to the English to Pig Latin translator!")
##original = input("Enter English word for translator")
##size = len(original)
##if size >= 1 and original.isalpha():
##	print(original)
##else:
##	print("empty")**\


##pyg = 'ay'
##
##original = input('Enter a word:')
##word = original.lower()
##first = original[0]
##if len(original) > 0 and original.isalpha():
##	print(original)
##	if first == str('a' or 'e' or 'i' or 'o' or 'u'):
##		print("vowel")
##		new_word = word + pyg
##		print(new_word)
##	else:
##                new_word = word[1:len(word)] + pyg
##		print("consonant")
##else:
##	print('empty')
##
##
###tip calc
##def tax(bill):
##    """Adds 8% tax to a restaurant bill."""
##    bill *= 1.08
##    print bill
##    return bill
##
##def tip(bill):
##    """Adds 15% tip to a restaurant bill."""
##    bill *= 1.15
##    print bill
##    return bill
###defining powers
##def power(base, exponent):
##    result = base**exponent
##    print "%d to the power of %d is %d." % (base, exponent, result)
##
##power(37, 4)
###defining favorite actors
##
##def favorite_actors(*args):
##    """Prints out your favorite actorS (plural!)"""
##    print "Your favorite actors are:" , args
##
##def one_good_turn(n):
##    return n + 1
##
##def deserves_another(n):
##    return one_good_turn(n) + 2
##favorite_actors("Michael Palin", "John Cleese", "Graham Chapman", "Kevin Spacey")

##def by_three(n):
##	if n == int(n / 3):
##		return n
##                print(n)
##	else:
##		return False
##                print(n)
##	print(n)
##
##by_three(9)
##
##def shut_down(s):
##	if s == s.lower("Yes"):
##		return "Shutting down..."
##	elif s == s.lower("No"):
##		return "Shutdown aborted!"
##	else:
##		return "Sorry, I didn't understand you."
##
##import math
##
##print math.sqrt(13689)
##
##def distance_from_zero(n):
##	if n == type(int) or type(float):
##		return abs(n)
##	else:
##		return "This isn't an integer or a float!"

##def hotelCost(days):
##    return 140*days
##
##def planeRideCost(city):
##    if city == "Charlotte":
##        return 183
##    if city == "Tampa":
##        return 220
##    if city == "Pittsburgh":
##        return 222
##    if city == "Los Angeles":
##        return 475
##
##def rentalCarCost(days):
##    cost = days*40
##    if days >= 7:
##        cost -= 50
##    elif days >= 3:
##        cost -= 20
##    return cost
##
##def tripCost(city, days):
##	return rentalCarCost(days) + hotelCost(days) + planeRideCost(city)
##
##def hotelCost(days):
##    return 140*days
##
##def planeRideCost(city):
##    if city == "Charlotte":
##        return 183
##    if city == "Tampa":
##        return 220
##    if city == "Pittsburgh":
##        return 222
##    if city == "Los Angeles":
##        return 475
##
##def rentalCarCost(days):
##    cost = days*40
##    if days >= 7:
##        cost -= 50
##    elif days >= 3:
##        cost -= 20
##    return cost
##
##def tripCost(city, days):
##	return rentalCarCost(days) + hotelCost(days) + planeRideCost(city) + spendingMoney()
##city = "Los Angeles"
##days = 5
##spendingMoney = 600
##print(tripCost)
##
##def tripCost(city,days,cash=0):
##    return cash+\
##    rentalCarCost(days)+\
##    hotelCost(days)+\
##    planeRideCost(city)
##
### You were planning on taking a trip to LA for 5 days
### with $600 of spending money.
##actuallySpent = 2734.23
##print(tripCost("Los Angeles",5,600))
##print(actuallySpent - tripCost("Los Angeles",5,600))

#Calculate paying back tripCost
def hotelCost(days):
    return 140*days

bill = hotelCost(5)
balance = bill
payment = 100
print(bill)

def getMin(balance, rate):
	rate = 0.02
	
	return balance * rate
print(getMin)

def addMonthlyInterest(balance):
    return balance * (1 + (0.15 / 12) ) 

def makePayment(payment,balance):
    return "You Still Owe: " + str(newBalance)

newBalance = balance - payment
#makePayment(100)

