'''
The selectmode option of a listbox widget can be single, browse, multiple or extended.

    single – Selects one line of text.
    browse – It is a default option where the user can select one line of text.
    multiple – Selects multiple lines of text without dragging from first line of option to last line.
    extended – User can select and drag adjacent multiple lines of text.
'''
from tkinter import *

main = Tk()
main.title("Mutiple Selection")
main.geometry("200x200")

label = Label(main,
              text = "Select the languages below :  ",
              font = ("Times New Roman", 10), 
              padx = 10, pady = 10)
label.pack()

yscrollbar = Scrollbar(main, orient= "vertical")
yscrollbar.pack(fill= Y, side= RIGHT)

lstbox = Listbox(main, selectmode= "multiple", yscrollcommand= yscrollbar.set)
lstbox.pack(expand= YES, fill= BOTH)

x =["C", "C++", "C#", "Java", "Python",
    "R", "Go", "Ruby", "JavaScript", "Swift",
    "SQL", "Perl", "XML"]

for item in range(len(x)):
    lstbox.insert(END, x[item])
    # coloring allternative lines of listbox
    lstbox.itemconfigure(item,
                                        bg= 'light yellow' if item % 2 == 0 else 'cyan')

yscrollbar.configure(command= lstbox.yview)
mainloop()