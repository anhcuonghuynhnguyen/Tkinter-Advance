from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
root = Tk()
root.geometry('200x200')

# This function is used to display
# the pop-up message
def show(event):
    string = event.get()
    messagebox.showinfo('Message', 'You selected ' + string)

text1 = StringVar()
text2 = StringVar()

# These text are used to set initial values of CheckButton to off
text1.set('OFF')
text2.set('OFF')

chkbtn1 = Checkbutton(root, textvariable = text1, variable = text1,
                          offvalue = 'GFG Not Selected',
                          onvalue = 'GFG Selected', command= lambda : show(text1))
chkbtn1.pack(side= TOP)
chkbtn2 = Checkbutton(root, textvariable = text2, variable = text2,
                          offvalue = 'GFG Average',
                          onvalue = 'GFG Good', command= lambda : show(text2))
chkbtn2.pack(side = TOP, pady = 10)
  
root.mainloop()