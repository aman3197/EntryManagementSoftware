# Entry management System

**Problem Statement:**
Given the visitors that we have in office and outside, there is a need to for an entry management software,We need an application, which can capture the name, email address, phone no of the visitor and same information also needs to be captured for the host on the front end. At the back end, once the user enters the information in the form, the backend should store all of the information with time stamp of the entry.

**Workflow:**
Once user run the program, new window is opened which is asking the admin to fill  details like Name,email,phone Number. and host also need need to enter the same details. once the check in button is clicked information of the visitor and host is store in database from which we can fetch data if required and check in button also trigger an Email and an SMS to the host informing him of the details of the visitor. and now we can click on go to check out  this button bring us to the new window which is asking to enter the visitor Email-id and if wrong email id is provided it shows error which i have shown in video. once the visitor provide the correct email it is successfully check out. and check out button also trigger an Email to the visitor containing the details of the meeting. 

**Approach:**
This application uses Tkinter for creating the graphical user interface(GUI). Tkinter is the GUI programming toolkit for python. in order to use it in your program you have to import it using statement ( from tkinter import * ). i have used MySQL for database.

Sending Emails has been with the help of Simple Mail Transfer Protocol (SMTP). SMS sending done wth help of twillio.

**Installation:**
1. Download the repository
2. open command prompt and navigate to the folder where repository is present
3. Execute ```python -m pip install -r requirements.txt```
>Caution::Install python3.6 and check "add path to path variables" during installation. Ensure pip is installed on your system.
	
**Technology Stack:**
1. Python
2. Tkinter for GUI
3. Twilio for SMS services
4. SMTP for email services
5. MySQL for database
6. Pillow for the images

**Setup**:


**Demo video:**

**Images of UI**:
