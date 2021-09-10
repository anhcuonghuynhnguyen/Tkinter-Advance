'''
The tkinter.ttk module serves as an improvement to the already existing tk module.
The Ttk module is equipped with 18 widgets, 12 of which existed in the Tkinter module such as Button, Checkbutton, PanedWindow, Radiobutton, Entry, Frame, Label, LabelFrame, Menubutton, 
Scale, Scrollbar, and Spinbox.
The newly added widgets are Combobox, Notebook, Sizegrip, Progressbar, Separator, and Treeview. 
The Notebook widget of ttk module is put into use to create a tabbed widget. 
The ttk.Notebook widget manages a collection of windows and displays one at a time. Each child window is associated with a tab. 
The user can select one tab at a time to view the content of the window.
'''

# Syntax: Notebook( main root, **option)
'''
master: parent window (root).
options: The options accepted by the Notebook() method are height, padding and width.
'''

# adding the tab
# Syntax: add(child, **options)
'''
child: tab1 and tab2 are the child widget of tabControl.
options: The options supported by add() method are sticky, state, 
                padding, text, image, compound, underline
It is used to add new tabs to the Notebook widget.
'''

import tkinter as tk					
from tkinter import ttk


root = tk.Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Tab 1')
tabControl.add(tab2, text ='Tab 2')
tabControl.pack(expand = 1, fill ="both")

ttk.Label(tab1,
		text ="Welcome to GeeksForGeeks").grid(column = 0,
							row = 0,
							padx = 30,
							pady = 30)
ttk.Label(tab2,
		text ="Lets dive into the world of computers").grid(column = 0,
									row = 0,
									padx = 30,
									pady = 30)

root.mainloop()

