count = 0

def square(x):
    global count
    count += 1
    return x**2

print (square(square(square(square(3)))))

# global vs local examples

# num1 is a global variable

num1 = 1
print num1

# num2 is a local variable

def fun():
    num1 = 2
    num2 = num1 + 1
    print num2
    
fun()


# the scope of global num1 is the whole program, num 1 remains defined
print num1

# the scope of the variable num2 is fun(), num2 is now undefined
# print num2


# why use local variables?
# give a descriptive name to a quantity
# avoid computing something multiple times

def fahren_to_kelvin(fahren):
    celsius = 5 / 9 * (fahren - 32)
    zero_celsius_in_kelvin = 273.15
    return celsius + zero_celsius_in_kelvin

print fahren_to_kelvin(212)





# the risk/reward of using global variables

# risk - consider the software system for an airliner
#		critical piece - flight control system
#		non-critical piece - in-flight entertainment system

# both systems might use a variable called "dial"
# we don't want possibility that change the volume on your audio
# causes the plane's flaps to change!



# example
num = 4

def fun1():
    global num
    num = 5
    
def fun2():
    global num
    num = 6

# note that num changes after each call with no obvious explanation    
print num
fun1()
print num
fun2()
print num

# global variables are an easy way for event handlers
# to communicate game information.

# safer method - but they required more sophisticated
# object-programming techniques

# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui

message = "Welcome!"

# Handler for mouse click
def click():
    global message
    message = "Good job!"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 36, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200,)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)
frame.set_canvas_background("#FF0000")



# Start the frame animation
frame.start()

# SimpleGUI
# Frame


# Frames are the basic outline of the user interface. Frames
#	are created using the syntax below. Remember to import
#	simplegui first.
# Note: Since CodeSkulptor can currently support only one 
#	frame, you will need to comment out the frame-creation
#	lines as you go.

import simplegui

#frame = simplegui.create_frame("New Frame", 200, 300)

# Here are the parts of the frame:
window_name = "New Frame"
canvas_width = 200
canvas_height = 300

#frame = simplegui.create_frame(window_name, canvas_width, canvas_height)

# Another example with new values
window_name = "New Name"
canvas_width = 600
canvas_height = 100

#frame = simplegui.create_frame(window_name, canvas_width, canvas_height)

# There is also an optional fourth parameter for the frame
window_name = "New Frame"
canvas_width = 400
canvas_height = 300
control_width = 400

#frame = simplegui.create_frame(window_name, canvas_width, canvas_height)
#frame = simplegui.create_frame(window_name, canvas_width, canvas_height, control_width)

# Note that the first value is the width, while the second
#	value is the height. THIS IS IMPORTANT :)

#frame = simplegui.create_frame("Test", 400, 200)
#frame = simplegui.create_frame("Test", 200, 400)

# For the next example, please uncomment the following frame

#frame = simplegui.create_frame("Test", 300, 200)

# You can also change the color of the canvas.

#frame.set_canvas_background("Red")
#frame.set_canvas_background("Blue")
#frame.set_canvas_background("White")

# There are more color strings that you can use. Check the 
#	documentation for more info.

# The final part of the frame is starting it. The following
#	method must be called for the canvas to be drawn correctly.
#	Try commenting it out to see what changes.

frame.start()




