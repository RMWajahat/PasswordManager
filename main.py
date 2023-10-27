from tkinter import *
import string
import random

window = Tk()
window.minsize(width=400,height=400)
window.title("Password Manager")
window.config(padx=10,pady=10)


asciis = []
asciis.extend(list(string.punctuation))
asciis.extend(list(string.ascii_letters))
asciis.extend(list(string.digits))

def genPassCode():
    password=""
    for _ in range(16):
        password+=random.choice(asciis)
    PasswordInput.insert(END,password)


def saveTo():
    mail = MailInput.get()
    Password = PasswordInput.get()
    website = websiteInput.get()
    
    with open("all_pass.txt","a") as f:
        f.write(f'{website} ->  {mail}   |   {Password}\n')


back_img = PhotoImage(file="lock.png")
canvas = Canvas(width=300,height=300)
canvas.create_image(150,150,image=back_img)
canvas.grid(row=0,column=1)

website = Label(text="Platform",font=("monospace",12,"normal"))
website.grid(row=1,column=0)

websiteInput = Entry(width=35,font=("monospace",14,"normal"))
websiteInput.grid(row=1,column=1,columnspan=2)

Mail = Label(text="Username/Email",font=("monospace",12,"normal"),pady=20)
Mail.grid(row=2,column=0)

MailInput = Entry(width=35,font=("monospace",14,"normal"))
MailInput.insert(END,"rajamuhammadwajahat2003@gmail.com")
MailInput.grid(row=2,column=1,columnspan=2)

Password = Label(text="Password",font=("monospace",12,"normal"),pady=20)
Password.grid(row=3,column=0)

PasswordInput = Entry(width=40,font=("monospace",10,"normal"))
PasswordInput.grid(row=3,column=1)

genPass = Button(text="Generate Password",command=genPassCode).grid(row=3,column=2)

add = Button(text="Add",width=50,font=("monospace",10,"bold"),bg="green",command=saveTo).grid(row=4,column=1,columnspan=3)


window.mainloop()