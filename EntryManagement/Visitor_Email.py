from Check_out_Page import *
import mysql.connector
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
from twilio.rest import Client
from validate_email import validate_email
from create_database import *
import smtplib
from Config import *

connection = mysql.connector.connect(host='localhost',
                                         user=MYSQL,
                                         password=MYSQL_password,database='management')
def popup3():# shows pop up window when some task is happened
    messagebox.showinfo("Checked-Out", "You have been successfully checked out!")

def vemail(mail):# This Function send an email to the visitor when he/she check-out
    mail1 = mail.get()# get function is used to get the information enter by the visitor
    if (validate_email(mail1, verify=True)):# This function check email enter is correct or not
        formula="select * from info where visitor_Email=%s"
        cursor2 = connection.cursor()
        cursor2.execute(formula,(mail1,))
        fe = cursor2.fetchall()# this function fetch all the details from database
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
            messagebox.showerror("Error", "Please Check-In First")# shows pop window displaying this error
        else:
            if chkout:
                messagebox.showerror("Error", "You Have Already checked_out")
            else:
                if(validate_email(mail1,verify=True)):
                    em = smtplib.SMTP('smtp.gmail.com', 587)

                    em.starttls()

                    em.login(GMAIL,Password)

                    msg = "Details of the meeting is\n"

                    sql = "UPDATE info SET Check_out=NOW() WHERE visitor_Email=%s and Check_out is NULL"# simple queries of the MySQL
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
                    em.sendmail(GMAIL,mail1, msg) # Send An email to the visitor Which Contain message msg Which is the details of the meeting

                    em.quit()
                    popup3()
                else:
                    messagebox.showerror("Error", "Please enter correct visitor email!")
    else:
        messagebox.showerror("Error", "Please enter correct visitor email!")