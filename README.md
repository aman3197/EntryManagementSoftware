# Entry management System

# Demo video:

# Problem Statement:
Given the visitors that we have in office and outside, there is a need to for an entry management software,We need an application, which can capture the name, email address, phone no of the visitor and same information also needs to be captured for the host on the front end. At the back end, once the user enters the information in the form, the backend should store all of the information with time stamp of the entry.

# Workflow:
On starting the program a Graphical User Interface window is opened which asks the Visitor to fill the details like Name,email id,phone number and host also need need to enter the same details.
On clicking the "Check-in" button, information of the visitor and host is stored in the database from which we can fetch the data whenever  required and clicking the "Check-in" button also trigger an Email and an SMS to the host informing him of the details of the visitor.
On clicking the "Go to check-out" button a new window is opened which asks the visitor to enter the Email-id. The information from the database is retrieved and the email-id entered is checked in the database. If the email-id entered matches with that in database, Visitor successfully checks out. And, if not matched then a new pop-up window is opened which tells the visitor to "Check-in first" if the email-id entered is correct and otherwise asks the visitor to provide correct email-id.
On successfully checking out. visitor recieves an email regarding the meeting with the host. The email comprises of information like Name of the host,meeting hours(check-in time and check-out time),Name of the visitor,Phone no. of the visitor and Location of the meeting.

# Installation:
1. Download the repository
2. open command prompt and navigate to the folder where repository is present
3. Execute ```python -m pip install -r requirements.txt```
>Caution::Install python3.6 and check "add path to path variables" during installation. Ensure pip is installed on your system.

# Prerequisites
1. [pip](https://pip.pypa.io/en/stable/) and python should be installed on your environment

# Technology Stack:
1. Python
2. Tkinter for GUI
3. Twilio for SMS services
4. SMTP for email services
5. MySQL for database
6. Pillow for the images


# Images of UI:

1. **Start Screen of the Application where Visitor can check in.**

![image1](https://github.com/aman3197/Innovaccer-EntryManagementSoftware/blob/master/Images/image1.png)

2. **Check-Out screen where visitor can Check-out.**

![image2](https://github.com/aman3197/Innovaccer-EntryManagementSoftware/blob/master/Images/image2.png)

3. **In this format 	Information is store in Database.**

![image13](https://github.com/aman3197/Innovaccer-EntryManagementSoftware/blob/master/Images/image13.png)

4. **Email recieved by the visitor when meeting is over.**

![image15](https://github.com/aman3197/Innovaccer-EntryManagementSoftware/blob/master/Images/image15.jpg)





5. **SMS recieved by the host when visitor Check-in.**



![image14](https://github.com/aman3197/Innovaccer-EntryManagementSoftware/blob/master/Images/image14.jpg)


