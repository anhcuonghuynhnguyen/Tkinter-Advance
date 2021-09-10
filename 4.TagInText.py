'''
Tags are used to associate names to regions of text which makes easy the task of modifying the display settings of specific text areas. 
Tags are also used to bind event callbacks to specific ranges of text.

    Following are the available methods for handling tabs −
'''
"""
tag_add(tagname, startindex[,endindex] ...)
    This method tags either the position defined by startindex, or a range delimited by the positions startindex and endindex.

tag_config
    You can use this method to configure the tag properties, which include, justify(center, left, or right), tabs(this property has the same functionality of the Text widget tabs's property), 
    and underline(used to underline the tagged text).

tag_delete(tagname)
    This method is used to delete and remove a given tag.

tag_remove(tagname [,startindex[.endindex]] ...)
    After applying this method, the given tag is removed from the provided area without deleting the actual tag definition.
"""
from tkinter import *

root = Tk()
text = Text(root)
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack()
def config():
    text.tag_add("here", "1.0", "1.4")
    text.tag_add("start", "1.8", "1.13")
    text.tag_config("here", background = "yellow", foreground = "blue")
    text.tag_remove("start", "1.0", "1.11")
    text.tag_config("start", background = "black", foreground = "green")

but = Button(root, text= "Config Text", command= config)
but.pack(side= BOTTOM)
root.mainloop()