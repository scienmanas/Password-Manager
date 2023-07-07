from tkinter import *
from tkinter import messagebox
from labels import Labels
from GenerateButton import Generate
from password_generator import PasswordGenerator
import pyperclip
import json

password = PasswordGenerator()

def SearchTheList():
    with open(r"Python_Course\Day 29\Password Manager with Tkinter\Passwords.json",mode='r') as file:
        data = json.load(file)
        found = False
        for site in data:
            if(site == WebsiteEntry.get()):
                credentials = data.get(site)
                messagebox.showinfo(title="Credentials as requested",message=f"The Credentials for the site: {site} are: '\n''\n'Email/Username: {credentials.get('Email')}'\n'Password: {credentials.get('Password')} ")
                pyperclip.copy(str(credentials.get('Password')))
                found = True
                break
        if not found:
                messagebox.showerror(title="Oops..",message="Data Not Found")

def WriteData(data):
    with open(r"Python_Course\Day 29\Password Manager with Tkinter\Passwords.json",mode='r') as file:
        new_data = json.load(file)
        new_data.update(data)
    with open(r"Python_Course\Day 29\Password Manager with Tkinter\Passwords.json",mode='w') as file:
        json.dump(new_data,file,indent=4)

def AddButtonPressed():
    data = {}
    data = {
        WebsiteEntry.get():
        {
            "Email" : EmailEntry.get() , 
            "Password" : PasswordEntry.get() 
        }
    }
    if len(str(WebsiteEntry.get())) == 0 or len(str(EmailEntry.get())) == 0 or len(str(PasswordEntry.get())) == 0:
        messagebox.showinfo(title="Oops!",message="Please make sure you don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title="Are you sure?", message=f"Website: {str(WebsiteEntry.get())}'\n'Email/Username: {str(EmailEntry.get())}'\n'Password: {str(PasswordEntry.get())}")
        if is_ok:
            WriteData(data)
            pyperclip.copy(str(PasswordEntry.get()))
            WebsiteEntry.delete(0,END)
            PasswordEntry.delete(0,END)

def PassButtonPressed():
    PasswordEntry.delete(0,END)
    PasswordEntry.insert(0,password.generate())

window = Tk()
window.title("Password Manager")
window.config(padx=10,pady=20)


logo = Canvas(width=400,height=400)
logo.grid(row = 1, column=2)
logo_image = PhotoImage(file=r"Python_Course\Day 29\Password Manager with Tkinter\logo.png")
logo.create_image(200,200, image = logo_image)

# Labels

Website = Labels(text="Website: ",row=2,column=1)
Email = Labels(text="Email/Username", row=3,column=1)
Password = Labels(text="Password",row=4,column=1)

# Buttons

PasswordButton = Generate(value="Generate Password",width=15,row=4,column=3)
PasswordButton.config(command=PassButtonPressed)


AddButton = Generate(value="Add",width=72,row=5,column=2,columnspan=2)
AddButton.config(command=AddButtonPressed)

Search = Generate(value="Search",row=2,column=3,width=14)
Search.config(command=SearchTheList)

# Entry

WebsiteEntry = Entry()
WebsiteEntry.grid(row=2,column=2)
WebsiteEntry.config(width=66)
WebsiteEntry.focus()


EmailEntry = Entry()
EmailEntry.grid(row=3,column=2,columnspan=2)
EmailEntry.config(width=85)
EmailEntry.insert(END, "ch21b026@iittp.ac.in")

PasswordEntry = Entry()
PasswordEntry.config(width=66)
PasswordEntry.grid(row = 4, column = 2)


window.mainloop()