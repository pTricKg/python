# Calculate Earnings

#def wage():
inp = float(input("What is your hourly rate: "))
inp2 = float(input("How many hours are you working: "))

wkly = inp * inp2
print("This is your earnings for hours given:",round(wkly,2))
mnthly = (wkly * 52) / 12
print("This is your monthly earnings:",round(mnthly,2))
annum = wkly * 52
print("This is your annual earnings:",round(annum,2))

#def wage()
