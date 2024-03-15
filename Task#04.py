from tkinter import *
from PIL import Image, ImageTk
import random

#Initialization of score
comp_score=0
user_score=0
comp_value = ["Rock", "Paper", "Scissor"]

#function for restart the game
def reset():
    global comp_score
    global user_score
    comp_score=0
    user_score=0
    l4.config(text="Play your move")
    l3.config(text=user_score)
    l6.config(text=comp_score)
    l7.config(text="You")
    l9.config(text="Computer")

#When user chose rock
def Rock():
    global comp_score
    global user_score
    comp = random.choice(comp_value)
    if comp == "Paper":
        result = "Computer Win!"
        l4.config(background="red")#for changing the background color of label
        comp_score=comp_score+1
    elif comp == "Scissor":
        result = "You Win!"
        l4.config(background="green")#for changing the background color of label
        user_score=user_score+1
    else:
        result = "Game Draw"
    l4.config(text=result)
    l3.config(text=user_score)
    l6.config(text=comp_score)
    l7.config(text="Rock")
    l9.config(text=comp)
    
#When user chose paper
def Paper():
    global comp_score
    global user_score
    comp = random.choice(comp_value)
    if comp == "Scissor":
        result = "Computer Win!"
        l4.config(background="red")#for changing the background color of label
        comp_score=comp_score+1
    elif comp == "Rock":
        result = "You Win!"
        l4.config(background="green")#for changing the background color of label
        user_score=user_score+1
    else:
        result = "Game Draw"
    l4.config(text=result)
    l3.config(text=user_score)
    l6.config(text=comp_score)
    l7.config(text="Paper")
    l9.config(text=comp)

#when user chose scissor
def Scissor():
    global comp_score
    global user_score
    comp = random.choice(comp_value)
    if comp == "Rock":
        result = "Computer Win!"
        l4.config(background="red")#for changing the background color of label
        comp_score=comp_score+1
    elif comp == "Paper":
        result = "You Win!"
        l4.config(background="green")#for changing the background color of label
        user_score=user_score+1
    else:
        result = "Game Draw"

    l4.config(text=result)
    l3.config(text=user_score)
    l6.config(text=comp_score)
    l7.config(text="Scissor")
    l9.config(text=comp)

m = Tk()
m.title("Rock paper scissor game")
m.geometry("500x600")
m.config(background="#E0FFFF")
m.resizable(False, False)

# Labels
l1=Label(m, text="Rock-Paper-Scissor Game", font=("Bold", 18), fg="#BBFFFF", bg="#191970").place(x=100, y=30)
l2=Label(m, text="You",bg="#E0FFFF", fg="#68228B", font=("bold", 18)).place(x=130, y=250)
l3=Label(m, text="0", bg="#E0FFFF",fg="#68228B", font=("Bold", 18))
l3.place(x=150, y=300)
l5=Label(m, text="Computer",bg="#E0FFFF", fg="#68228B", font=("bold", 18)).place(x=230, y=250)
l6=Label(m, text="0",bg="#E0FFFF", fg="#68228B", font=("Bold", 18))
l6.place(x=250, y=300)

# Images
img_1 = PhotoImage(file=r"E:\JavaScript\rock_paper\rock.png").subsample(16, 14)
img_2 = PhotoImage(file=r"E:\JavaScript\rock_paper\paper.png").subsample(16, 14)
img_3 = PhotoImage(file=r"E:\JavaScript\rock_paper\scissors.png").subsample(16, 14)

# Buttons
b1=Button(m, image=img_1, command=Rock).place(x=50, y=100)
b3=Button(m, image=img_2, command=Paper).place(x=200, y=100)
b5=Button(m, image=img_3, command=Scissor).place(x=350, y=100)

#User and computer choices
l7=Label(m,text="You",bg="#E0FFFF",fg="#68228B",font=("bold",18))
l7.place(x=120,y=370)
l8=Label(m,text="V",bg="#E0FFFF",fg="#68228B",font=("bold",18)).place(x=230,y=370)
l9=Label(m,text="Computer",bg="#E0FFFF",fg="#68228B",font=("bold",18))
l9.place(x=280,y=370)
# Result Entry
l4 = Label(m,text="Play your move",bg="#E0FFFF", fg="#68228B", font=("bold", 18))
l4.place(x=170, y=450)

# Reset Button
Button(m, text="Reset Game", font=("bold", 17), fg="#BBFFFF", bg="#191970",command=reset).place(x=170, y=500)

m.mainloop()

