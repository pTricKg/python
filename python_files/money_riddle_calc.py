# This calculates 'math riddle'
# from The Happening.
# Question was 'How much money would
# you have if I gave you a penny
# everyday for a month but multiplied
# that value by 2 everyday

day = 1 
month = 30
cash = 0.01

while day < month:
    day = day + 1
    cash = cash * 2
    print("This is current day:",day)
    print("This is current value:",cash)

print("Now you have", cash, "dollars!!")

# Or

for days in range(30):
    day = day + 1
    cash = cash * 2
    print("This is current day from for loop:",day)
    print("This is current value from for loop:",cash)
# divided by two to get same result as while loop due to extra day payout
print("Now you have", cash / 2, "dollars!! Calculated from for in loop")
    
    
