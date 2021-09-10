from tkinter import *

# Function for checking the
# key pressed and updating
# the listbox
lst = ['Tkinter', 'Pandas', 'Kivy', 'Python', 'Viet Nam']

def check(event):
    var = entr.get()
    if var == "" :
        data = lst
    else:
        data = []
        for item in lst:
            if var.lower() in item.lower():
                data.append(item)
    update(data)

def update(a):
    lstbox.delete( 0, "end")

    for item in a:
        lstbox.insert( END, item)


root = Tk()
entr = Entry(root)
lstbox = Listbox(root)

entr.pack()
lstbox.pack()
update(lst)

entr.bind("<KeyRelease>", check)

mainloop()
