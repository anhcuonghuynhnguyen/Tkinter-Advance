'''
focus_set() method-
    This method is used to set the focus on the desired widget
    if and only if the master window is focused.
'''

'''
focus_get() method-
    This method returns the name of the widget which currently has the focus.
'''

from tkinter import *
from tkinter.ttk import * 

main = Tk()
main.geometry("200x200")

# This method is used to get
# the name of the widget
# which currently has the focus
# by clicking Mouse Button-1
def focus(event):
    wid = main.focus_get()
    print(wid, "has focus")

entry = Entry(main)
entry.focus_set()
entry.pack(expand= True, fill= BOTH)

but = Button(main, text= "Button")
but.pack()

radio = Radiobutton(main, text= "Heloo")
radio.pack()

# Here function focus() is binded with Mouse Button-1
# so every time you click mouse, it will call the
# focus method, defined above
main.bind("<Button-1>", focus)

mainloop()