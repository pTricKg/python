day = 1
month = 30
cash = 0.01

while day < month:
    cash = cash * 2
    print("This is current day:",day)
    print("This is current value:",cash)
    for days in range(30):
        days = days * 2
    print(days)
