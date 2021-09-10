'''
Tkinter supports some variables which are used to manipulate the values of Tkinter widgets. These variables work like normal variables. 
set() and get() methods are used to set and retrieve the values of these variables. 
The values of these variables can be set using set() method or by using constructor of these variables.
There are 4 tkinter variables. 
    BooleanVar()
    StringVar()
    IntVar()
    DoubleVar()
'''

from tkinter import *
# Tkinter variables
# initialization using constructor
master = Tk()
# Tkinter variables
# Giving user defined names to each variables
# so that variables can be modified easily
intvar = IntVar(master, name ="int")
strvar = StringVar(master, name ="str")
boolvar = BooleanVar(master, name ="bool")
doublevar = DoubleVar(master, name ="float")
# Setting values of variables
# using setvar() method and set() method
master.setvar( name= "int", value= 2)
strvar.set( value= "Python")
master.setvar( name= "bool", value= True)
doublevar.set( value= 1.666)

# getting values of each variables using getvar() method and get() method
print("Value of IntVar()", intvar.get())
print("Value of StringVar()", master.getvar(name= "str"))
print("Value of BooleanVar()", boolvar.get())
print("Value of DoubleVar()", master.getvar(name ="float"))

mainloop()