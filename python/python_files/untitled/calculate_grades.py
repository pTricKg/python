grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
average = 0
grade = 0
std_d = 0
def print_grades(grades):
    for grade in grades:
        print (grade)

def grades_sum(grades):
    total = ['']
    for grade in grades: ##range(len(grades)):
        total = sum(grades)
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / len(grades)
    return average

def grades_variance(grades, average):
    variance = 0
    grade_dif = (average - grade) ** 2
    variance = (variance + grade_dif) / len(grades)
    return variance

'''compute its difference from the average: average - grade
    Square this difference to get rid of
    negative differences: (average - grade) ** 2
    Compute a rolling sum of the squared differences
    ( i.e., add it to the current value of a variable called variance)
    the final variance is the sum of squared differences divided
    by the number of grades. '''

def grades_std_deviation(variance):
    std_d = grades_variance(grades, grades_average(grades)) ** (1/2)
    return std_d
