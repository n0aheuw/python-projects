# importting modules
import tkinter
import pyperclip
from random_username.generate import generate_username
import random 

#Assigns Global Font Use in Frames
global FONT
FONT = "calibri 20 bold"

class main(tkinter.Tk):  
    
    def __init__(self, *args, **kwargs):  
          
        tkinter.Tk.__init__(self, *args, **kwargs)     #Class to create the different windows tkaen from https://www.javatpoint.com/tkinter-application-to-switch-between-different-page-frames-in-python
        container = tkinter.Frame(self)                #Further class generation was influenced by the same website look there for more infromation.
        self.title("User Credentials Generator")
        self.geometry("700x350")
        
        container.pack(side="top", fill="both", expand = True)  
  
        container.grid_rowconfigure(0, weight=1)  
        container.grid_columnconfigure(0, weight=1)  
  
        self.frames = {}  
  
        for F in (StartPage, Password, Username):  
  
            frame = F(container, self)  
  
            self.frames[F] = frame  
  
            frame.grid(row=0, column=0, sticky="nsew")  
  
        self.show_frame(StartPage)  
  
    def show_frame(self, cont):  
  
        frame = self.frames[cont]  
        frame.tkraise()  
  
          
class StartPage(tkinter.Frame):  
  
    def __init__(self, parent, controller):  
        tkinter.Frame.__init__(self,parent)
        
        tkinter.Label(self, text="Home Page", font=FONT).pack(anchor = tkinter.CENTER)
  
        button = tkinter.Button(self, text="Password",  
                            command=lambda: controller.show_frame(Password))  
        button.pack(padx=5, pady=3, anchor=tkinter.CENTER)   
  
        button2 = tkinter.Button(self, text="Username",  
                            command=lambda: controller.show_frame(Username))  
        button2.pack(padx=5, pady=3, anchor=tkinter.CENTER) 
  
  
class Password(tkinter.Frame):  
  
    def __init__(self, parent, controller):  
        tkinter.Frame.__init__(self, parent)
        
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
        tkinter.Label(self, text="Password Generator", font=FONT).pack()

        tkinter.Label(self, text="Enter password length").pack(pady=3) #widget title for password entry box
        tkinter.Entry(self, textvariable=passlen).pack(pady=3) #takes input for required password length
        tkinter.Button(self, text="Generate Password", command=generate).pack(pady=7) # button to call the generate function

        tkinter.Entry(self, textvariable=passstr).pack(pady=3) # entry widget to show the generated password
        tkinter.Button(self, text="Copy to clipboard", command=copytoclipboard).pack() # button to call the copytoclipboard function  
        
        button1 = tkinter.Button(self, text="Back to Home",  
                            command=lambda: controller.show_frame(StartPage))  
        button1.pack(padx=5, pady=5, anchor=tkinter.SE)
  
        button2 = tkinter.Button(self, text="Username",  
                            command=lambda: controller.show_frame(Username))  
        button2.pack(padx=5, pady=5, anchor=tkinter.SE)
  
  
class Username(tkinter.Frame):  
    
    def __init__(self, parent, controller):  
        tkinter.Frame.__init__(self, parent)
        
        #str variable for storing generated username    
        userstr = tkinter.StringVar() 
        
        # function to copy the password to the clipboard
        def copytoclipboard():
            random_user = userstr.get()
            random_user = random_user.replace("'", "").replace(")", "").replace("(", "").replace(",", "")
            pyperclip.copy(random_user)

        # creating title widget
        tkinter.Label(self, text="Username Generator", font=FONT).pack()

        tkinter.Entry(self, textvariable=userstr).pack(pady=3) # entry widget to show the generated username
        tkinter.Button(self, text="Generate Username", command=lambda: userstr.set(generate_username(1))).pack(pady=7) # button to call the generate function
        tkinter.Button(self, text="Copy to clipboard", command=copytoclipboard).pack() # button to call the copytoclipboard function 
  
        button1 = tkinter.Button(self, text="Back to Home",  
                            command=lambda: controller.show_frame(StartPage))  
        button1.pack(padx=5, pady=5, anchor=tkinter.SE)
  
        button2 = tkinter.Button(self, text="Password",  
                            command=lambda: controller.show_frame(Password))  
        button2.pack(padx=5, pady=5, anchor=tkinter.SE)  
          
  
root = main()  
root.mainloop()