##hrs = input("Enter hours worked: ")
##h = float(hrs)
##
##if h > 40:
##    rpay = h * 10.5
##    #print(rpay)
##    othrs = h - 40
##    ot = rpay + (othrs * (10.5 * .5))
##    print(ot)
##else:
##    rpay = h * 10.5
##    print(rpay)




try:
    score = float(input("Enter your score: "))
    print(type(score))
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")
    else:
        print("Invalid input")
except:
    print("Invalid input")
