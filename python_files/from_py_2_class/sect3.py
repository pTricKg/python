##import math
##
##def area_hero(side1, side2, side3):
##    '''(number, number, number) -> float
##
##    Return the area of a triangle with sides of length
##    side1, side2, and side3
##
##    >>>area_hero(3, 4, 5)
##    6.0
##    >>>area_hero(10.5, 6, 9.3)
##    27.731
##    '''
##
##    semi = semiperimeter(side1, side2, side3)
##    area = math.sqrt(semi * (semi - side1) * (semi - side2) * (semi - side3))
##    return area
##
##def report_status(scheduled_time, estimated_time):
##    '''(number, number) -> str
##
##    Return the flight status (on time, early, delayed)
##    for a flight that was scheduled to arrive at
##    scheduled_time, but is now estimated to arrive
##    at estimated_time.
##
##    Pre-condition: 0 <= sheduled_time < 24 and
##    0.0 <= estimated_time <24
##    
##    >>>report_status(14.3, 14.3)
##    'on time'
##    >>>report_status(12.5, 11.5)
##    'early'
##    >>>report_status(9.0, 9.5)
##    'delayed'
##    '''
##
##    if scheduled_time == estimated_time:
##        return 'on time'
##    elif scheduled_time > estimated_time:
##        return 'early'
##    else:
##        return 'delayed'
##
##def is_even(num):
##    '''(int) -> bool
##
##    Return whether num is even.
##
##    >>>is_even(4)
##    True
##    >>>is_even(77)
##    False
##    '''
##
##    return num % 2 == 0
##    if num % 2 == 0:
##        return True
##    else:
##        return False

##def traffic_report(light):
##    if light == 'red':
##        return 'stop'
##    elif light == 'yellow':
##        return 'slow'
##    elif light == 'green':
##        return 'go'
##
##print(traffic_report('orange'))

##def grade_report(grade):
##    if grade >= 80:
##        return 'excellent'
##    elif grade >= 50:
##        return 'pass'
##
##grade_report(50)
##grade_report(70)
##grade_report(80)
##grade_report(40)

##pages = 0
##book_count = 0
##
##if pages1 >= 100:
##    pages = pages + pages1
##    book_count = book_count + 1
##    if pages2 >= 100:
##        pages = pages + pages2
##        book_count = book_count + 1
##
##if book_count > 0:
##    print(pages / book_count)
##
##
##pages = 0
##book_count = 0
##
##if pages1 >= 100:
##    pages = pages + pages1
##    book_count = book_count + 1
##if pages2 >= 100:
##    pages = pages + pages2
##    book_count = book_count + 1
##
##if book_count > 0:
##    print(pages / book_count)
##
##pages = 0
##book_count = 0
##
##if pages1 >= 100:
##    pages = pages + pages1
##    book_count = book_count + 1
##else:
##    pages = pages + pages2
##    book_count = book_count + 1
##
##if book_count > 0:
##    print(pages / book_count)

pages = 0
book_count = 0

if pages1 >= 100:
    pages = pages + pages1
    book_count = book_count + 1
elif pages2 >= 100:
    pages = pages + pages2
    book_count = book_count + 1

if book_count > 0:
    print(pages / book_count)
