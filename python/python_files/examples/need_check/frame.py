title='creating a frame'
from tkinter import *


class App:

    def __init__(self, master):

        w = Label(master, text="Hello, world!")

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print ("hi there, everyone!")



root = Tk()

app = App(root)

root.mainloop()

# the appearance of the frame can be modified choosing a relief type and
# applying appropriate bandwidth.

##Frame(root,borderwidth=2,relief=SUNKEN).pack(side=LEFT,padx=5,pady=5)
##Label(root,text='I am a frame').pack(side=LEFT)
##
##root.title(title)
##root.mainloop()
