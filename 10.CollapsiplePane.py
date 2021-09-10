# Importing tkinter and ttk modules
from tkinter import *
from tkinter.ttk import *

# Importing Collapsible Pane class that we have
# created in separate file
from text import CollapsiblePane as cp

# Making root window or parent window
root = Tk()
root.geometry('200x200')

# Creating Object of Collapsible Pane Container
# If we do not pass these strings in
# parameter the the default strings will appear
# on button that were, expand >>, collapse <<
cpane = cp(root)
cpane.grid(row = 0, column = 0)

# Button and checkbutton, these will
# appear in collapsible pane container
b1 = Button(cpane.frame, text ="GFG").grid(
			row = 1, column = 2, pady = 10)

cb1 = Checkbutton(cpane.frame, text ="GFG").grid(
				row = 2, column = 3, pady = 10)

mainloop()
