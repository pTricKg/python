def computepay(h,r):
    h = int(h)
    r = float(r)
    if h > 40:
        ot = (h - 40) * (r * 1.5) + (40 * r)
        return ot
    else:
        pay = h * r
        return pay

hrs = int(input("Enter Hours:"))
rate = float(input("Enter pay rate:"))

print ("Pay per week",computepay(hrs,rate))

def annualpay(h,r):
    annum = computepay(h,r) * 52
    return annum

print ("Pay per year", annualpay(hrs,rate))
