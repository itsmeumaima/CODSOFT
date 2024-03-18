# Password generator
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import string

#Clear function
def clear():
    password_entry.delete(0,END)

#Generate password function
def generate():
    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)
    all=upper+lower+digits+punctuation
    length=int(s.get())
    password=random.sample(all,length)
    password_entry.insert(0,password)

#Copy the password function
def copy():
    random_password=password_entry.get()
    pyperclip.copy(random_password)

#Main window
root=Tk()
root.title("Password Generator")
root.geometry("350x350")
root.resizable(False,False)
root.config(background="#191970")

#Labels
heading=Label(root,text="Password Generator",font=("Bold",18),bg="#191970",fg="white").place(x=60,y=30)

len_heading=Label(root,text="Password Length",font=("arial",15),bg="#191970",fg="white").place(x=100,y=80)

#Spinbox
s=Spinbox(root,from_=2,to_=16,font=("bold",16),width=10,wrap=True)
s.place(x=110,y=115)

#Buttons
generate_button=Button(root,text="Generate",font=("bold",16),width=8,fg="#191970",bg="#9290C3",command=generate)
generate_button.place(x=130,y=180)

clear_button=Button(root,text="Clear",width=6,font=("bold",16),fg="#191970",bg="#9290C3",command=clear)
clear_button.place(x=180,y=300)

copy_button=Button(root,text="Copy",width=6,font=("bold",16),fg="#191970",bg="#9290C3",command=copy)
copy_button.place(x=80,y=300)

#Entry
password_entry=Entry(root,font=("bold",16))
password_entry.place(x=60,y=250)


root.mainloop()