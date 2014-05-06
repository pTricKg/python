# lists

# variable = [ expression1, expression2, expression3]

grades = [80, 90, 70]

>>> grades[0]
80
>>> grades[1]
90
>>> grades[2]
70
>>> grades[1:2]
[90]
>>> grades[0:2]
[80, 90]
>>> 90 in grades
True
>>> 60 in grades
False
>>> len(grades)
3
>>> min(grades)
70
>>> max(grades)
90
>>> sum(grades)
240


subjects = ['bio', 'cs', 'math', 'history']

>>> min(subjects)
'bio'

>>> max(subjects)
'math'

street_address = [10, 'Main Street']

for grade in grades:
    print(grade)

80
90
70

for item in subjects:
    print(item)

bio
cs
math
history

s = ""
names = ["Alice", "Bob", "Carol"]
for name in names:
    s = s + name


colors = []
prompt = 'Enter another one of your favorite colors (hit return to end)
color = input(prompt)

while color != '':
    colors.append(color)
    color = input(prompt)

colors.extend(['pink', 'green'])

colors.pop() #removes last item in list and returns

colors.remove()

if colors.count('color') > 0:
    colors.remove('color')

if 'color' in colors:
    colors.remove('color')

colors.extend([list])

colors.sort()

colors.reverse()

colors.insert(place in list, 'color')

color.index('color')

if 'color' in colors:
    where = colors.index('color')
    colors.pop('color')




