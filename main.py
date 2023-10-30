from tkinter import *
from tkinter import messagebox
import string
import random
import json
import os.path as FileEmpty

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
    PasswordInput.delete(0,END)
    for _ in range(16):
        password+=random.choice(asciis)
    PasswordInput.insert(END,password)


def Search_data():
    web = websiteInput.get().capitalize()
    if len(web)!=0:
        with open("pass_manager.json","r") as f:
            data = json.load(f)
            try:
                data = data[web]
            except KeyError:
                messagebox.showerror(title="Exception",message=f"No data found for {web}")
            else:
                messagebox.showinfo(title=f"{web}",message=f'Email: {data["email"]}\nPassword: {data["password"]}')
                    
    else:
        messagebox.showerror(title="Empty field error",message="Please input website name!")


def saveTo():
    mail = MailInput.get().lower()
    Password = PasswordInput.get()
    website = websiteInput.get().capitalize()
    
    if len(mail)!=0 and len(Password)!=0 and  len(website)!=0:
        isOk = messagebox.askokcancel(title=f"Managing Password for {website.capitalize()}",message=f"Confirm Your Data\nMail: {mail}\nWebsite: {website}\nPassword{Password}")
        
        
        new_JSON_data={
            website:{
                "email":mail,
                "password": Password,
            },
        }
        
        
        if isOk:
            
            with open("pass_manager.json","r") as f:
                if FileEmpty.getsize("pass_manager.json")!=0:
                    data = json.load(f)
                    data.update(new_JSON_data)
                    with open("pass_manager.json","w") as dataFile:
                        json.dump(data,dataFile,indent=4)
                else:
                    with open("pass_manager.json","w") as dataFile:
                        json.dump(new_JSON_data,dataFile,indent=4)
                
            MailInput.delete(0,END)
            PasswordInput.delete(0,END)
            websiteInput.delete(0,END)
    else:
        messagebox.showerror(title="Empty field error", message="Input all fields to continue")


back_img = PhotoImage(file="lock.png")
canvas = Canvas(width=300,height=300)
canvas.create_image(150,150,image=back_img)
canvas.grid(row=0,column=1)

website = Label(text="Platform",font=("monospace",12,"normal"))
website.grid(row=1,column=0)

websiteInput = Entry(width=35,font=("monospace",14,"normal"))
websiteInput.grid(row=1,column=1,columnspan=2)
search = Button(text="Search",width=10,font=("monospace",10,"bold"),padx=2,bg="orange",command=Search_data).grid(row=1,column=2)

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