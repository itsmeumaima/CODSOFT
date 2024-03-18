#To do list using python
from tkinter import *
from tkinter import messagebox

#Update function
def Update():
    mark=lst_box.curselection()
    data=task_enter.get()
    if mark==tuple() or data=="":
        messagebox.showerror("Enter the updated data")
    else:
        lst_box.delete(mark,mark)
        lst_box.insert(mark,data)
        task_enter.delete(0,END)    

#Maked as completed function
def Mark():
    marked=lst_box.curselection()
    temp=marked[0]
    print(temp)
    temp_mark=lst_box.get(marked)
    temp_mark=temp_mark+"✔"
    lst_box.delete(temp)
    lst_box.insert(temp,temp_mark)

#Delete the particular task
def Delete_task():
    index=lst_box.curselection()
    if index:
        lst_box.delete(index,index)
    else:
        messagebox.showerror("Select task")    

#Delete all task
def Delete_all():
    lst_box.delete(0,END)

#Add a new task
def Add_task():
    data=task_enter.get()
    if data=="":
        messagebox.showerror("Enter Task")
    else:
        lst_box.insert(END,data)
        task_enter.delete(0,END)

#GUI Window
screen=Tk()
screen.title("To-Do List")
screen.geometry("400x450")
screen.resizable(False,False)
screen.config(background="#FAEBD7")

#Main label
main_heading=Label(screen,text="To-Do List",width=13,font=("Bold + Italic Font", "30"),bg="#FAEBD7",fg="#8B7355").place(x=50,y=40)

#Task entry box
task_enter=Entry(screen,font=("Arial",16),width=12)
task_enter.place(x=40,y=140)

#Add task button
add_task=Button(screen,text="Add Task",width=10,bg="#CDAA7D",fg="white",command=Add_task)
add_task.place(x=30,y=200)

#Delete task button
delete_task=Button(screen,text="Delete Task",width=10,bg="#CDAA7D",fg="white",command=Delete_task)
delete_task.place(x=120,y=200)

#Delete all task button
delete_all=Button(screen,text="Delete all",width=10,bg="#CDAA7D",fg="white",command=Delete_all)
delete_all.place(x=30,y=250)

#button for mark as completed
mark_all=Button(screen,text="marked",width=10,bg="#CDAA7D",fg="white",command=Mark)
mark_all.place(x=120,y=250)

#Update button
update=Button(screen,text="Update",width=10,bg="#CDAA7D",fg="white",command=Update)
update.place(x=80,y=310)

lst_box=Listbox(screen,width=15,height=10,font=("Arial",16))
lst_box.place(x=200,y=115)

screen.mainloop()