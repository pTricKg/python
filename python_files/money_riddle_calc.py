# This is calculation riddle:

print("""
If i were to give you 2 cents for 30 days but
each day after the first give you twice as much as the day before,
how much money will you have after that final day?

Think about it for a moment.

You'll be surprised!
""")

input("Press enter when ready to see result\n")

day = 0
month = 30
cash = 0.01

while day < month:
    day += 1
    cash = cash * 2
    print("This is current day:",day)
    print("This is current value:",cash,"\n")
    for days in range(30):
        days = days * 2

print("\n\nAfter 30 days you will have",cash,"in cold cash")
