from Tkinter import *
root = Tk()

""" This program gives keyboard input keycode as well as frame coordinates """

def key(event):
    print "Keycode:", event.keycode, "State:", event.state

def callback(event):
    frame.focus_set()
    print "clicked at", event.x, event.y

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
