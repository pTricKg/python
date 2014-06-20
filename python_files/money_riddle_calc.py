# This is calculation riddle:
"""
If i were to give you two cents everyday for a month and
each day give you twice as much as the day before, how much
money will you have after that month?

"""

day = 1
month = 30
cash = 0.01

while day < month:
    day += 1
    cash = cash * 2
    print("This is current day:",day)
    print("This is current value:",cash)
    for days in range(30):
        days = days * 2

print("\n\nAfter one month you will have",cash,"in cold cash")
