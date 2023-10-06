import mysql.connector as mysql
from function import *

try :
    db = mysql.connect(host="localhost",user="root",password="",database="school")
    command_handler = db.cursor(buffered=True)
    print("Database is connected.")
except Exception as e:
    print(e)
    print("Database could not connected")
    
#if database and table is created then run this.
def Main():
    print("--------------------")
    print("Login")
    print("1. teacher")
    print("2. admin")
    opt = input(" choose >>>")
    if opt == "1":
       teachersession()
    elif opt == "2":
        admin_session()
    else :
        print("Invalid option")
def admin_session():
    while True:
        print("--------------------")
        print("welcome admin")
        print("1. Register new student")
        print("2. Register new teacher")
        print("3. Delete existing student")
        print("4. Delete existing teacher")
        print("5. Log out")
        opt = input(" choose >>>")
        if opt == "1":
            admin.addstudents()
        elif opt == "2":
            admn.addteacher()
        elif opt == "3":
            admin.deletestudent()
        elif opt == "4":
            admin.deleteteacher()
        elif opt == "5":
            print("good bye, admin")
def teacher_session():
    while True:
        print("--------------------")
        print("welcome teacher")
        print("1. record of students")
        print("2. marks")
        opt = input("choose >>>")
        if opt == "1":
            teacher.studentrecord()
        elif opt == "2":
            teacher.marks()
        elif opt == "3":
            break
        else :
            print('Invalid option')
if __name__ == "__main__":
    Main()
            