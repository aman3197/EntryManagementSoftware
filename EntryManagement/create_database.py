import mysql.connector
from Config import *

#This function create the database
def cd():
    connection = mysql.connector.connect(host='localhost',
                                         user=MYSQL,
                                         password=MYSQL_password)
    cursor = connection.cursor()
    try:
        sql1="create database management;"
        #print("aman")
        cursor.execute(sql1)
        cursor.execute("use management")
        mySql_Create_Table_Query = "CREATE TABLE info( visitor_Name varchar(255),visitor_Email varchar(255),visitor_Number varchar(255),host_Name varchar(255),host_Email varchar(255),host_Number varchar(255),checkin TIMESTAMP DEFAULT CURRENT_TIMESTAMP,Check_out TIMESTAMP)"
        cursor.execute( mySql_Create_Table_Query)
    except:
        cursor.execute("use management")#if database already exist then use it. I use exception handling for that