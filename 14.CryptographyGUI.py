# https://www.geeksforgeeks.org/cryptography-gui-using-python/
'''
Using cryptography techniques we can generate keys for a plain text which can not be predicted easily. 
We use Cryptography to ensure the safe and secure flow of data 
from one source to another without being accessed by a malicious user.
'''
'''
Basics of Cryptography – Cryptography is used for Secure Communication.

    Encryption – The process of encoding a message or information in such a way that only authorized parties can access it.
    Decryption – The process of taking encoded or encrypted text or other data and converting it back into text.
'''
# in this we will use algorithm that is ONE-TIME-PAD

# python module for one-timepad
import onetimepad
# python module to create GUI		
from tkinter import *

		
root = Tk()
root.title("CRYPTOGRAPHY")
root.geometry("800x600")

def encryptMessage():					
	pt = e1.get()

	# inbuilt function to encrypt a message
	ct = onetimepad.encrypt(pt, 'random')
	e2.insert(0, ct)

def decryptMessage():					
	ct1 = e3.get()

	# inbuilt function to decrypt a message
	pt1 = onetimepad.decrypt(ct1, 'random')
	e4.insert(0, pt1)
	
# creating labels and positioning them on the grid
label1 = Label(root, text ='plain text')			
label1.grid(row = 10, column = 1)
label2 = Label(root, text ='encrypted text')
label2.grid(row = 11, column = 1)
l3 = Label(root, text ="cipher text")
l3.grid(row = 10, column = 10)
l4 = Label(root, text ="decrypted text")
l4.grid(row = 11, column = 10)

# creating entries and positioning them on the grid
e1 = Entry(root)
e1.grid(row = 10, column = 2)
e2 = Entry(root)
e2.grid(row = 11, column = 2)
e3 = Entry(root)
e3.grid(row = 10, column = 11)
e4 = Entry(root)
e4.grid(row = 11, column = 11)

# creating encryption button to produce the output
ent = Button(root, text = "encrypt", bg ="red", fg ="white", command = encryptMessage)
ent.grid(row = 13, column = 2)

# creating decryption button to produce the output
b2 = Button(root, text = "decrypt", bg ="green", fg ="white", command = decryptMessage)
b2.grid(row = 13, column = 11)


root.mainloop()

