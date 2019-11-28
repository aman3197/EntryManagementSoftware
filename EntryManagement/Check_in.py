from Home_page import *
import mysql.connector
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
from validate_email import validate_email
from SMS import *
from Host_Email import *
from create_database import *
from Config import *

connection = mysql.connector.connect(host='localhost',
                                         user=MYSQL,
                                         password=MYSQL_password,database='management')
def popup1():
    messagebox.showinfo("SAVED", "Your information has been stored!")

def check_in_window(e1,e2,e3,e4,e5,e6):# This function start when check-in button is clicked
    if e1.get() and e2.get() and e3.get() and e4.get() and e5.get() and e6.get():# If you forget to enter any one detail on home page it will display an error
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
            if(validate_email(s2,verify=True)):# This Function checks whether visitor email-id enter is correct or not
                s3=e3.get()
                s3="+91"+s3# Concate The number with +91
                try:
                    carrier._is_mobile(number_type(phonenumbers.parse(s3)))# This Function checks whether the visitor Phone number enter is valid or not
                    s4 = e4.get()
                    s5 = e5.get()
                    if(validate_email(s5,verify=True)):# This Function checks whether host email-id enter is correct or not
                        s6 = e6.get()
                        s6="+91"+s6
                        try:
                            carrier._is_mobile(number_type(phonenumbers.parse(s6)))# This Function checks whether the host Phone number enter is valid or not
                            hemail(s1, s5, s3)
                            sms(s1, s3, s6)
                            sql2 = "INSERT INTO info(visitor_Name,visitor_Email,visitor_Number,host_Name,host_Email,host_Number) VALUES(%s,%s,%s,%s,%s,%s)"
                            var = (s1, s2, s3, s4, s5, s6)
                            cursor1.execute(sql2,(var))
                            connection.commit()
                            popup1()
                        except:# These errors are displayed when any details enter is wrong.
                            messagebox.showerror("Error", "Please enter correct Host Number!")
                    else:
                        messagebox.showerror("Error", "Please enter correct Host Email!")
                except:
                    messagebox.showerror("Error", "Please enter correct visitor Number!")
            else:
                messagebox.showerror("Error", "Please enter correct visitor email!")
    else:
        messagebox.showerror("Error", "Please fill the details")