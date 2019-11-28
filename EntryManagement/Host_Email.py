import smtplib
from Check_in import *
from Config import *

# This function send an email to the Host contain information of the visitor
def hemail(Name, host_email, NUMBER):
    em = smtplib.SMTP('smtp.gmail.com', 587)

    em.starttls()

    em.login(GMAIL, Password)

    msg = Name + " is coming to meet you and\nhis contact number is " + NUMBER
    em.sendmail(GMAIL, host_email, msg)

    em.quit()