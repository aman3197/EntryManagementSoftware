import PIL.ImageTk, PIL.Image
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from Visitor_Email import *

def Check_out_window():# This is the function of my check-out window fronted
    r = Tk()
    r.title('entry managment system')
    r.geometry("500x150+700+40")
    s1 = Label(r, text="Enter visitor Email-id", fg='red',bg='#f7f7f7', font=('Arial 15 bold'))
    s1.place(x=115, y=10)
    lbl = Label(r, text="Email", bg='#f7f7f7',font=('Arial 12'))
    lbl.place(x=115, y=50)
    e1 = Entry(r, bd=5,width=40)
    e1.place(x=165, y=50)
    btn = Button(r, text="Check-Out",fg='blue',bg='#f7f7f7',command=lambda:vemail(e1),font=('12'))
    btn.place(x=120, y=90)
    btn1 = Button(r, text="Cancel",fg='blue',bg='#f7f7f7',command=r.destroy,font=('12'))
    btn1.place(x=240, y=90)
    r.configure(background="#f7f7f7")# This function set the background colour of the screen