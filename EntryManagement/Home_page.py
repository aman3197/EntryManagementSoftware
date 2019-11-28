import PIL.ImageTk, PIL.Image
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from Check_in import *
from Check_out_Page import *

#This is the home page of My Application
def gui():
    inno=Tk()
    inno.geometry("561x700+10+20") # set the size of the your screen
    s1= Label(inno, text="Enter visitor details", fg='red',bg='#f7f7f7',font=('Arial 15 bold')) # This function Display the text on my home page
    s1.place(x=135,y=15) # Place the text At this location of your screen
    lbl = Label(inno, text="Name",bg='#f7f7f7',font=('Arial 12'))
    lbl.place(x=135, y=50)
    e1=Entry(inno, bd=5,width=40) # Takes the input from user
    e1.place(x=185, y=50)
    lbl1 = Label(inno, text="Email",bg='#f7f7f7',font=('Arial 12'))
    lbl1.place(x=135, y=80)
    e2 = Entry(inno, bd=5,width=40)
    e2.place(x=185, y=80)
    lbl2 = Label(inno, text="Number",bg='#f7f7f7',font=('Arial 12'))
    lbl2.place(x=124, y=110)
    e3 = Entry(inno, bd=5,width=40)
    e3.place(x=185, y=110)
    s2 = Label(inno, text="Enter host details", fg='red',bg='#f7f7f7', font=('Arial 15 bold'))
    s2.place(x=135, y=145)

    lbl3 = Label(inno, text="Name",bg='#f7f7f7',font=('Arial 12'))
    lbl3.place(x=135, y=180)
    e4 = Entry(inno, bd=5,width=40)
    e4.place(x=185, y=180)
    lbl4 = Label(inno, text="Email",bg='#f7f7f7',font=('Arial 12'))
    lbl4.place(x=135, y=210)
    e5 = Entry(inno, bd=5,width=40)
    e5.place(x=185, y=210)
    lbl5 = Label(inno, text="Number",bg='#f7f7f7',font=('Arial 12'))
    lbl5.place(x=124, y=240)
    e6 = Entry(inno, bd=5,width=40)
    e6.place(x=185, y=240)
    photo = PhotoImage(file=r"C:\Users\hp\.PyCharm2019.2\green.png") # getting the image located at this path
    photoimage = photo.subsample(15, 15)
    btn=Button(inno, text="check-In",image = photoimage,compound = LEFT,command=lambda: check_in_window(e1,e2,e3,e4,e5,e6)) # This function display the button on my home page
    btn.place(x=150, y=278)
    photo1= PhotoImage(file=r"C:\Users\hp\.PyCharm2019.2\go.png")
    photoimage1 = photo1.subsample(7, 7)
    btn1 = Button(inno, text="Go for check-Out",image = photoimage1,compound = LEFT,command=Check_out_window)
    btn1.place(x=280, y=278)
    path=r"C:\Users\hp\Downloads\photo4.png"
    img = PIL.ImageTk.PhotoImage(PIL.Image.open(path))# this functions add Image  to my home page
    panel = Label(inno, image=img)
    panel.place(x=0,y=340)
    inno.configure(background="#f7f7f7")
    inno.title('entry managment system') # Title of your home page screen
    inno.mainloop()