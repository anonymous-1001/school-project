import mysql.connector as mysql
try :
    db = mysql.connect(host="localhost",user="root",password="")
    command_handler = db.cursor()
    command_handler.execute("CREATE DATABASE college")
    print("Database is created. creating Tables")
except Exception as e:
    print(e)
    print("Database could not created")

try:
    db1 = mysql.connect(host="localhost", user="root", password="", database="college")
    command_handler = db1.cursor()
    command_handler.execute("CREATE TABLE students(ID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(35), age INT(20), class INT(12), stream VARCHAR(255), father VARCHAR(255), mother VARCHAR(255), address VARCHAR(255), postal VARCHAR(255)")
    command_handler.execute("CREATE TABLE teachers(ID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(35), age INT(20), subject VARCHAR(255), address VARCHAR(255), number VARCHAR(255)")
    db.commit()
    print("Table created created")
except Exception as e:
    print(e)
    print("Table could not be created")