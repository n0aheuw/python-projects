# importting modules
import tkinter
import pyperclip
from random_username.generate import generate_username
import random

# initializing the tkinter
root =  tkinter.Tk()
root.title("Username Generator")
root.geometry("400x200")    # Setting GUI height and width

#str variable for username generated
userstr = tkinter.StringVar()

# function to copy the password to the clipboard
def copytoclipboard():
    random_user = userstr.get()
    random_user = random_user.replace("'", "").replace(")", "").replace("(", "").replace(",", "")
    pyperclip.copy(random_user)

# creating title widget
tkinter.Label(root, text="Username Generator Application", font="calibri 20 bold").pack()

tkinter.Entry(root, textvariable=userstr).pack(pady=3) # entry widget to show the generated username
tkinter.Button(root, text="Generate Username", command=lambda: userstr.set(generate_username(1))).pack(pady=7) # button to call the generate function
tkinter.Button(root, text="Copy to clipboard", command=copytoclipboard).pack() # button to call the copytoclipboard function

root.mainloop() # infinite loop used to run the application in it's ready state 
