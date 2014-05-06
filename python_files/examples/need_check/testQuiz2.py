##p = True
##q = True
##
##print(not (p or not q))
##
##p = True
##q = False
##
##print(not (p or not q))
##
##p = False
##q = True
##
##print(not (p or not q))
##
##p = False
##q = False
##
##print(not (p or not q))

#computes ten's digit-should evaluate to 2
##n = 123.4
##
##print((n / 10) % 10)
##print(((n - n % 10) /10) % 10) # correct
##print((n // 10) % 10) # correct

#preference to random.randrang() since handle numberical ranges like rest of python
##import random
##
##print(random.randint(0,10))
##print(random.randrange(0,10))

##def f(x):
##   return -5 * (x ** 5) + 69 * (x ** 2) - 47
##
##print(f(0))
##print(f(1))
##print(f(2))
##print(f(3))


##When investing money, an important concept to know is compound interest.
##The equation FV = PV (1+rate)periods . This relates the following four quantities.
##
##The present value (PV) of your money is how much money you have now.
##The future value (FV) of your money is how much money you will have in the future.
##The interest rate per period (rate) is how much interest you earn as a percentage.
##The period is length of time between interest payments.
##The number of periods (periods) is how many periods in the future this calculation is for.
##Finish the following code, run it, and submit the printed number.
##Provide at least four digits of precision after the decimal point.

##def future_value(present_value, annual_rate, periods_per_year, years):
##    rate_per_period = annual_rate / periods_per_year
##    periods = periods_per_year * years
##    
##    return present_value * (1 + rate_per_period) ** periods
##
##print("$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3))
##Before submitting your answers, test your function on the following.

##import math
##
##def area_of_polygon(n, s):
##    return ((1/4) * n * (s ** 2)) / (math.tan(math.pi/n))
##
##print(area_of_polygon(5,7))
##print(area_of_polygon(7,3))
import math

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt((point_x ** 2) + (point_y ** 2))
    scale = distance / dist_to_origin
    print (point_x * scale, point_y * scale)
    
project_to_distance(2,7,4)
