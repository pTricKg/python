#!/usr/bin/python

##from Tkinter import *
##top = Tkinter.Tk()
### Code to add widgets will go here...
##frame = Frame(top)
##top.mainloop()

from Tkinter import *

## window basics
root = Tk()
root.title("myWindow") ## naming window
root.minsize(300, 400) ## sizing control
root.maxsize(400, 500)
##frame = Frame(root)
##frame.pack()

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        ## shuts down
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT, pady=100)

        ## hello
        self.button = Button(frame, text="Hello", fg="blue", command=self.hi)
        self.button.pack(side=LEFT, pady=100)


    def hi(frame):
        var = StringVar() # print inside window
        label = Message(root, textvariable=var)
        var.set("Hellooo, there!")
        label.pack()
##        print("Hellooooo, there!")

##l1 = Label(root, text = "Throw yours")
##l1.pack(side = LEFT)
##e1 = Entry(root, bd =5)
##e1.pack(side = RIGHT)

##bottomframe = Frame(root)
##bottomframe.pack( side = BOTTOM )
##
##redbutton = Button(frame, text="Red", fg="red")
##redbutton.pack( side = LEFT)
##
##greenbutton = Button(frame, text="Brown", fg="brown")
##greenbutton.pack( side = LEFT )
##
##bluebutton = Button(frame, text="Blue", fg="blue")
##bluebutton.pack( side = LEFT )
##
##blackbutton = Button(bottomframe, text="Black", fg="black")
##blackbutton.pack( side = BOTTOM)
app = App(root)
root.mainloop()
