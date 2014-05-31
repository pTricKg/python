# Calculate Earnings

##def wage():
inp = int(input("What is your hourly rate: "))
inp2 = int(input("How many hours are you working: "))

wkly = inp * inp2
print("This is your earnings for hours given:",wkly)
mnthly = (wkly * 52) / 12
print("This is your monthly earnings:",mnthly)
annum = wkly * 52
print("This is your annual earnings:",annum)

#def wage()
