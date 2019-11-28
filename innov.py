import PIL.ImageTk, PIL.Image
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import mysql.connector
import smtplib
import time
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
from twilio.rest import Client
from validate_email import validate_email
#from py3DNS import *

def popup1():
    messagebox.showinfo("SAVED", "Your information has been stored!")

def popup2():
    messagebox.showerror("Error","Please enter valid details!")

def popup3():
    messagebox.showinfo("Checked-Out", "You have been successfully checked out!")

connection = mysql.connector.connect(host='',
                                         user='',
                                         password='',database='management')
cursor = connection.cursor()

def vemail(mail):
    mail1 = mail.get()
    if (validate_email(mail1, verify=True)):
        formula="select * from info where visitor_Email=%s"
        cursor2 = connection.cursor()
        cursor2.execute(formula,(mail1,))
        fe = cursor2.fetchall()
        flag=1
        for i in fe:
            nam=i[0]
            eml=i[1]
            num=i[2]
            nam1=i[3]
            eml1=i[4]
            num1=i[5]
            chkin=i[6]
            chkout=i[7]
            if eml==mail1:
                flag=2
        if(flag==1):
            messagebox.showerror("Error", "Please Check-In First")
        else:
            if chkout:
                messagebox.showerror("Error", "You Have Already checked_out")
            else:
                if(validate_email(mail1,verify=True)):
                    em = smtplib.SMTP('smtp.gmail.com', 587)

                    em.starttls()

                    em.login("", "")

                    msg = "Details of the meeting is\n"

                    sql = "UPDATE info SET Check_out=NOW() WHERE visitor_Email=%s and Check_out is NULL"
                    cursor2.execute(sql,(mail1,))
                    connection.commit()

                    sql1="select visitor_Name from info where visitor_Email=%s"
                    cursor2.execute(sql1,(mail1,))
                    vist_name=""
                    for i in cursor2:
                        vist_name=str(i[0])

                    sql2 = "select visitor_Number from info where visitor_Email=%s"
                    cursor2.execute(sql2, (mail1,))
                    vist_number=""
                    for i in cursor2:
                        vist_number=str(i[0])

                    sql3 = "select host_Name from info where visitor_Email=%s"
                    cursor2.execute(sql3, (mail1,))
                    hst_name=""
                    for i in cursor2:
                        hst_name= str(i[0])

                    sql4= "select checkin from info where visitor_Email=%s"
                    cursor2.execute(sql4, (mail1,))
                    chkin=""
                    for i in cursor2:
                        chkin = str(i[0])

                    sql5 = "select Check_out from info where visitor_Email=%s"
                    cursor2.execute(sql5, (mail1,))
                    chkout=""
                    for i in cursor2:
                        chkout = str(i[0])

                    msg+="your name-->"+vist_name+"\n"+"your number-->"+vist_number+"\ncheck-in time-->"+chkin+"\ncheck out time"+chkout+"\nhost name-->"+hst_name+"\nAddress is 2nd and 9th Floor, Tower 3, Candor Techspace, Rajat Vihar, Block B, Industrial Area, Sector 62, Noida, Uttar Pradesh 201309"
                    em.sendmail("",mail1, msg)

                    em.quit()
                    popup3()
                else:
                    messagebox.showerror("Error", "Please enter correct visitor email!")
    else:
        messagebox.showerror("Error", "Please enter correct visitor email!")


def sms(vis_name,vis_num,host_num):
    # Your Account SID from twilio.com/console
    account_sid = ""
    # Your Auth Token from twilio.com/console
    auth_token = ""

    client = Client(account_sid, auth_token)
        #print(host_num)
    message = client.messages.create(
        to= str(host_num),
        from_="",
        body=vis_name+ " is coming to meet you and visitor's Contact Number is " + vis_num)

def hemail(Name,host_email,NUMBER):
        em = smtplib.SMTP('smtp.gmail.com', 587)

        em.starttls()

        em.login("" , "")

        msg = Name+" is coming to meet you and\nhis contact number is "+NUMBER
        em.sendmail("", host_email, msg)

        em.quit()
def ch(e1,e2,e3,e4,e5,e6):
    if e1.get() and e2.get() and e3.get() and e4.get() and e5.get() and e6.get():
        cursor1=connection.cursor()
        s1 = e1.get()
        s2 = e2.get()
        formula = "select * from info where visitor_Email=%s"
        cursor1.execute(formula, (s2,))
        fe = cursor1.fetchall()
        flag=1
        #fe = cursor1.fetchall()
        for i in fe:
            nam = i[0]
            eml = i[1]
            if (s2==eml):
                if not i[7]:
                    flag=2
                    break
            nam1 = i[3]
            em11 = i[4]
            num1 = i[5]
            chkin = i[6]
        if flag==2:
            messagebox.showerror("Error", " You have already been checked-In")
        else:
            if(validate_email(s2,verify=True)):
                s3=e3.get()
                s3="+91"+s3
                try:
                    carrier._is_mobile(number_type(phonenumbers.parse(s3)))
                    s4 = e4.get()
                    s5 = e5.get()
                    if(validate_email(s5,verify=True)):
                        s6 = e6.get()
                        s6="+91"+s6
                        try:
                            carrier._is_mobile(number_type(phonenumbers.parse(s6)))
                            hemail(s1, s5, s3)
                            sms(s1, s3, s6)
                            sql2 = "INSERT INTO info(visitor_Name,visitor_Email,visitor_Number,host_Name,host_Email,host_Number) VALUES(%s,%s,%s,%s,%s,%s)"
                            var = (s1, s2, s3, s4, s5, s6)
                            cursor1.execute(sql2,(var))
                            connection.commit()
                            popup1()
                        except:
                            messagebox.showerror("Error", "Please enter correct Host Number!")
                    else:
                        messagebox.showerror("Error", "Please enter correct Host Email!")
                except:
                    messagebox.showerror("Error", "Please enter correct visitor Number!")
            else:
                messagebox.showerror("Error", "Please enter correct visitor email!")
    else:
        messagebox.showerror("Error", "Please fill the details")
def cq():
    try:
        sql1="create database management"

        cursor.execute(sql1)
        cursor.execute("use management")
        mySql_Create_Table_Query = "CREATE TABLE info( visitor_Name varchar(255),visitor_Email varchar(255),visitor_Number varchar(255),host_Name varchar(255),host_Email varchar(255),host_Number varchar(255),checkin TIMESTAMP DEFAULT CURRENT_TIMESTAMP,Check_out TIMESTAMP)"
        cursor.execute( mySql_Create_Table_Query)
    except:
        cursor.execute("use management")


def new_window():
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
    r.configure(background="#f7f7f7")

def gui():
    inno=Tk()
    inno.geometry("561x700+10+20")
    s1= Label(inno, text="Enter visitor details", fg='red',bg='#f7f7f7',font=('Arial 15 bold'))
    s1.place(x=135,y=15)
    lbl = Label(inno, text="Name",bg='#f7f7f7',font=('Arial 12'))
    lbl.place(x=135, y=50)
    e1=Entry(inno, bd=5,width=40)
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
    photo = PhotoImage(file=r"C:\Users\hp\.PyCharm2019.2\green.png")
    photoimage = photo.subsample(15, 15)
    btn=Button(inno, text="check-In",image = photoimage,compound = LEFT,command=lambda: ch(e1,e2,e3,e4,e5,e6))
    btn.place(x=150, y=278)
    photo1= PhotoImage(file=r"C:\Users\hp\.PyCharm2019.2\go.png")
    photoimage1 = photo1.subsample(7, 7)
    btn1 = Button(inno, text="Go for check-Out",image = photoimage1,compound = LEFT,command=new_window)
    btn1.place(x=280, y=278)
    path=r"C:\Users\hp\Downloads\photo4.png"
    img = PIL.ImageTk.PhotoImage(PIL.Image.open(path))
    panel = Label(inno, image=img)
    panel.place(x=0,y=340)
    inno.configure(background="#f7f7f7")
    inno.title('entry managment system')
    inno.mainloop()
cq()
gui()
