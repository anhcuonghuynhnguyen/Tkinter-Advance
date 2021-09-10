# https://www.geeksforgeeks.org/tracing-tkinter-variables-in-python/
# trace_add( self, mode, callbakc_name ) is used to add an observer to a variable and returns the name of the callback function whenever the value is accessed.
'''
Parameters:
    Mode: It is one of “array”, “read”, “write”, “unset”, or a list or tuple of such strings.
    callback_name: It is the name of the callback function to be registered on the tkinter variable.
'''

# trace_remove( self, mode, "callback_name" ) is used to unregister an observer. It returns the name of the callback used while registering the observer through trace_add() method initially.
'''
Parameters:
    Mode: It is one of “array”, “read”, “write”, “unset”, or a list or tuple of such strings.
    callback_name: It is the name of the callback function to be registered on the tkinter variable.
'''

# trace_info( self)  It returns the name of the callback. This is generally used to find the name of the callback that is to be deleted. This method takes no argument other than the tkinter variable itself.

# Python program to trace
# variable in tkinter


from tkinter import *

root = Tk()
# defining the callback function (observer)
def my_callback(var, index, mode):
    print( f"Traced variable {my_var.get()}")

my_var = StringVar()

my_var.trace_add('write', my_callback)


Label(root, textvariable= my_var).pack(padx= 10, pady= 10)
Entry(root, textvariable = my_var).pack(padx = 10, pady = 10)
  
but = Button(root, text= "Remove trace", command= lambda : print(my_var.trace_info()))
but.pack(side=BOTTOM)
root.mainloop()

