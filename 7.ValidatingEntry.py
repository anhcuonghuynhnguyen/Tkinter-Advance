'''
 There are applications that require validation of text fields 
 to prevent invalid input from the user before the form is submitted
'''

# <var> = <main>.register(<callback function)
'''
Syntax: register(function)
Parameter:

function: The function that is to be called to validate the input in the Entry widget.
Return Value: This method returns a character string that can be used to call the function.
Explanation
The register() method returns a string which is assigned to a variable ‘reg’ 
that is used to call the callback function in the later stages.
'''
# https://stackoverflow.com/questions/55184324/why-is-calling-register-required-for-tkinter-input-validation


#Call the callback function to validate the input in Entry widget
# <entry>.config( validate= "key", validatecommand= (<var>, '%P'))

'''
validate: This option is used to specify when the callback function will be called to validate the input. The “key” value specifies that validation occurs whenever any keystroke(input from keyboard) changes the widget’s contents.
validatecommand: This option is used to specify the callback function. The function is not called directly rather a variable is passed which was registered in the earlier steps. ‘%P’ is passed to denote the value that the text will have if the change is allowed.
Explanation
Validate option supports other values such as focus, focusin, focusout, all and none. The default value is “none”, which means that there is no validation.
Validatecommand option supports other values such as %d, %i, %s, %S, %v, %V and %W . The percent substitution can be added for each parameter to be passed to the Python function
The Entry widget also supports an invalidcommand option that calls a function whenever the validatecommand returns False.
These can be used based on the requirement of the user.
'''

from tkinter import *


def callback(input):
	
	if input.isdigit():
		print(input)
		return True
						
	elif input is "":
		print(input)
		return True

	else:
		print(input)
		return False
						
root = Tk()

e = Entry(root)
e.place(x = 50, y = 50)
reg = root.register(callback)

e.config(validate ="key",
		validatecommand =(reg, '% P'))

root.mainloop()
