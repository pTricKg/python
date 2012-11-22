# Dictionaries

fruit_to_color = {
    'banana' : 'yellow',
    'cherry' : 'red',
    'orange' : 'orange',
    'pear' : 'green',
    'peach' : 'orange',
    'plum' : 'purple',
    'pomegranate' : 'red',
    'strawberry' : 'red'
    
    }

for fruit in fruit_to_color: 
    print(fruit, fruit_to_color[fruit])# prints key and associated value

# invert fruit_to_color
color_to_fruit = {}
for fruit in fruit_to_color:
    color = fruit_to_color[fruit]
    # if color is not already a key in accumulator
    # add color: [fruit] as entry
    if not (color in color_to_fruit):
        color_to_fruit[color] = [fruit]
    # otherwise, append fruit to existing list
    else:
        color_to_fruit[color].append(fruit)
        
##    color_to_fruit[color] = fruit
