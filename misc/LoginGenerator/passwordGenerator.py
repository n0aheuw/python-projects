# importting modules
import tkinter
import pyperclip
import random

# initializing the tkinter
root =  tkinter.Tk()
root.title("Password Generator")
root.geometry("400x200")    # Setting GUI height and width

#str variable for password generated
passstr = tkinter.StringVar()
#int variable to store password length
passlen = tkinter.IntVar()
# setting the length of the password to zero initially
passlen.set(0)

# function to generate the password
def generate():
    # storing the possible keys for password
    
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']

    # declaring empty password string
    password = ""
    
    # loop generating password to assigned length
    for i in range(passlen.get()):
        password = password + random.choice(pass1)

    # setting the password to the entry widget
    passstr.set(password)

# function to copy the password to the clipboard
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

# creating title widget
tkinter.Label(root, text="Password Generator Application", font="calibri 20 bold").pack()

tkinter.Label(root, text="Enter password length").pack(pady=3) #widget title for password entry box
tkinter.Entry(root, textvariable=passlen).pack(pady=3) #takes input for required password length
tkinter.Button(root, text="Generate Password", command=generate).pack(pady=7) # button to call the generate function

tkinter.Entry(root, textvariable=passstr).pack(pady=3) # entry widget to show the generated password
tkinter.Button(root, text="Copy to clipboard", command=copytoclipboard).pack() # button to call the copytoclipboard function

root.mainloop() # infinite loop used to run the application in it's ready state 