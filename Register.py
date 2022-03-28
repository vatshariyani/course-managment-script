# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 02:23:37 2022

@author: Vats Hariyani
"""

# Creating Managment system with Python with MySQL database

# Creating a database with MySql
import getpass
import mysql.connector as sql 

user = input("Enter usename: ")
password = (input("Enter password: "))

conn=sql.connect(host='localhost',user = user, password = password)

if conn.is_connected():
  print("Successfully Connected")
c1=conn.cursor()
c1.execute('create database if not exists cims')
print ('Database created')

# Creating a table
import mysql.connector as sql 
conn=sql.connect(host='localhost',user = user, password = password, database='cims')
if conn.is_connected():
  print("Successfully Connected")
c1=conn.cursor()
c1.execute('create table if not exists cand_details(adm_no int primary key, candidate_name varchar(50), course_select varchar(20))')
print ('Table created')

#Creating main menu and other functionalities
import mysql.connector as sql 
conn=sql.connect(host='localhost',user=user,password=password,database='cims')
if conn.is_connected():
    print("Successfully Connected")
c1=conn.cursor()
print("                                 SSA Computer Institute Management System")
print(" ")
print("1. Enrolling For A Course")
print("2. Edit Enrollments (as admin)")
print("3. Display Details")
print("4. Exit")
choice=int(input("Enter the Choice - "))
if choice==1:
    v_admno=int(input("Enter the Admission Number: "))
    v_candidatename=input("Enter your name : ")
    v_course=input("Enter the Course: ")
    if v_course=='JAVA':
        v_course='JAVA'
    elif v_course=='Python':
        v_course='Python'
    elif v_course=='C':
        v_course='C'
    elif v_course=='BASIC':
        v_course='BASIC'
    elif v_course=='HTML':
        v_course='HTML'
    
    V_SQL_Insert = "insert into cand_details values (" + str(v_admno) + ",'" + v_candidatename +"','" + v_course + "')"
    c1.execute(V_SQL_Insert)
    print(" ")
    print("                                        You are Enrolled Mr.",v_candidatename,". Congrats!!!")
    conn.commit()
    print(" ")
    print ("                                    Your enrollment for", v_course ,"course is successful!")
if choice==2:
    uname=input("Enter Username:")
    passwd=input("Enter Password:")
    u_name='abc'
    pass_wd='123'
    if (uname==u_name) and (passwd==pass_wd):
        print("                                                      Password Accepted")
        print("1. Delete An Enrollment")
        print("2. Edit Name")
        print("3. Edit Course")
        print(" ")
        option=int(input("Which of the above options would you like to choose ?"))

        if option==1:
            change_adm_no=int(input("Enter the admission number of the candidate to be removed:"))
            V_SQL_Insert = "delete from cand_details where adm_no = " + str(change_adm_no) 
            c1.execute(V_SQL_Insert)
            print("")
            print("                                                  Successfully removed")
            conn.commit()
        if option==2:
            change_adm_no=int(input("Enter the admission number of the candidate whose name is to be changed:"))
            change_name=input("Enter the desired name:")
            V_SQL_Insert = "update cand_details set candidate_name = '" + change_name + "' where adm_no = " + str(change_adm_no) 
            c1.execute(V_SQL_Insert)
            print("")
            print("                                                  Successfully edited")
            conn.commit()
        if option==3:
            change_adm_no=int(input("Enter the admission number of the candidate whose course is to be changed:"))
            change_course=input("Enter the Course: ")
            if change_course=='JAVA':
              change_course='JAVA'
            elif change_course=='Python':
                change_course='Python'
            elif change_course=='C':
               change_course='C'
            elif change_course=='BASIC':
               change_course='BASIC'
            elif change_course=='HTML':
                change_course='HTML'
            V_SQL_Insert = "update cand_details set course_select = '" + change_course + "' where adm_no = " + str(change_adm_no) 
            c1.execute(V_SQL_Insert)
            print("")
            print("                                               Successfully modified")
            conn.commit()
        
    else:
        print("                                         Wrong Username or Password")

    
if choice==3:
        c1.execute("Select * from cand_details ")
        data=c1.fetchall()
        for row in data:
            print("                                                            Candidates Details ")
            print("                                                      Admission Number : ", row[0])
            print("                                                      Candidate Name   : ", row[1])
            print("                                                      Course Selected  : ", row[2])
            print(" ")
            print(" ")
if choice==4:
    print('                                                         Thank You')
