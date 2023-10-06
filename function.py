from main import *
import csv

class admin:
    def addstudents():
        while True:
            print("----------------")
            print("Adding student, fill the details")
            name = input("Name of student >>>")
            while True:
                try :    
                    age = int(input("Age of student >>>"))
                    if age<=20 and age>=5:
                        break
                    else :
                        print("invalid option")
                except Exception as e:
                    print("invalid option, try again")
            while True:
                try :    
                    Class = int(input("Class of student >>>"))
                    if Class<=12 and Class>=1:
                        break
                    else :
                        print("invalid option")
                except Exception as e:
                    print("invalid option, try again")
            stream = input("Stream of student (only for class 11 and 12, if not type N/A)>>>")
            fathername = input("Name of father >>>")
            mothername = input("Name of mother >>>")
            address = input("Address of student >>>")
            postal = input("postal code >>>")
            vals = (name,age,Class,stream,fathername,mothername,address,postal)
            try :    
                command_handler.execute(" INSERT INTO students(name,age,class,stream,father,mother,address,postal) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",vals)
                db.commit()
                print(f"{name} is now added into the database")
            except Exception as e:
                print(e)
                print(f"{name} couldn't add")
            ask = input("Want to continue (Y/N):")
            if ask.lower == "y":
                print(" ")
            elif ask.lower == "n":
                break
            else :
                print("Invalid input")

    def addteacher():
        while True:
            print("----------------")
            print("Adding teacher, fill the details")
            name = input("Name of teacher>>>")
            while True:
                try :    
                    age = int(input("Age of teacher >>>"))
                    if age<=57 and age>=25:
                        break
                    else :
                        print("invalid option")
                except Exception as e:
                    print("invalid option, try again")
            subject= input("subject of teacher >>>")
            address = input("Address of student >>>")
            number = input("phone number >>>")
            vals = (name,age,subject,address,number)
            try :
                command_handler.execute("INSERT INTO teacher(name,age,subject,address,number) VALUES(%s,%s,%s,%s,%s)", vals)
                db.commit()
                print(f"{name} teacher added")
            except Exception as e:
                print(e)
                print(f"{name} couldn't add")
            ask = input("Want to continue (Y/N):")
            if ask.lower == "y":
                print(" ")
            elif ask.lower == "n":
                break
            else :
                print("Invalid input")
    def deleteteacher():
        while True:
            print("-------------")
            print("fill up the detail;")
            name = input("Teacher Name :")
            subject= input("subject of teacher >>>")
            vlas = (name,subject)
            try :
                command_handler.execute("DELETE FROM teachers WHERE name = %s AND subject = %s", vals)
                db.commit()
                print(f"{name} data is removed")
            except Exception as e:
                print(e)
                print("couldn't delete teacher")
            ask = input("Want to continue (Y/N):")
            if ask.lower == "y":
                print(" ")
            elif ask.lower == "n":
                break
            else :
                print("Invalid input")
    def deletestudent():
        while True:
            print("---------------")
            print("fill up the detail;")
            name = input("Student Name :")
            while True:
                try :    
                    age = int(input("Age of student >>>"))
                    if age<=20 and age>=5:
                        break
                    else :
                        print("invalid option")
                except Exception as e:
                    print("invalid option, try again")
            while True:
                try :    
                    Class = int(input("Class of student >>>"))
                    if Class<=12 and Class>=1:
                        break
                    else :
                        print("invalid option")
                except Exception as e:
                    print("invalid option, try again")
            try :
                vals = (name,age,Class)
                command_handler.execute("DELETE FROM student WHERE name = %s AND age = %s AND class = %s",vals)
                db.commit()
                print(f"{name} removed from data")
            except Exception as e:
                print(e)
                print(f"{name} couldn't delete")
            ask = input("Want to continue (Y/N):")
            if ask.lower == "y":
                print(" ")
            elif ask.lower == "n":
                break
            else :
                print("Invalid input")

class teacher:
    def studentrecord():
        while True:
            print("-------------")
            while True:
                try :    
                    Class = int(input("Class of student >>>"))
                    if Class<=12 and Class>=1:
                        break
                    else :
                        print("invalid option")
                except Exception as e:
                    print("invalid option, try again")
            try :
                command_handler.execute("SELECT name,age,class,stream FROM students WHERE class = %s",Class)
                records = command_handler.fetchall
                for x in records:
                    print(x)
            except Exception as e:
                print(e)
                print(f"Couldn't fetch data of students from {Class}")
            ask = input("Want to continue (Y/N):")
            if ask.lower == "y":
                print(" ")
            elif ask.lower == "n":
                break
            else :
                print("Invalid input")
    def marks():
        try :
            while True:
                print("------------")
                while True:
                    Class = int(input("Class of student >>>"))
                    if Class<=12 and Class>=1:
                        break
                    else :
                        print("invalid option")
                filename = str(Class+"marks.csv")
                with open(filename,"a+") as f:
                    fields = ["name","English","Phsyics","Maths","Chemistry","Computer Science"]
                    csvwriter = csv.writer(f)
                    csvwriter.writerow(fields)
                    command_handler.execute("SELECT name FROM students WHERE class = %s",Class)
                    records = command_handler.fetchall
                    for record in records:
                        record = str(record).replace("'","")
                        record = str(record).replace("'","")
                        record = str(record).replace("(","")
                        record = str(record).replace(")","")
                        #Marks
                        while True:
                            engmark=int("English marks :")
                            if engmark >=0 and engmark <=100:
                                break
                            else :
                                print("invalid marks")
                        while True:
                            phymark=int("Physics marks :")
                            if phymark >=0 and phymark <=100:
                                break
                            else :
                                print("invalid marks")
                        while True:
                            mathmark=int("Maths marks :")
                            if mathmark >=0 and mathmark <=100:
                                break
                            else :
                                print("invalid marks")
                        while True:
                            chemark=int("Chemistry marks :")
                            if chemmark >=0 and chemmark <=100:
                                break
                            else :
                                print("invalid marks")
                        data=[i,engmark,phymark,mathmark,chemark]
                        csvwriter.writerows(data)
                print("marks added")
                ask = input("Want to continue (Y/N):")
                if ask.lower == "y":
                    print(" ")
                elif ask.lower == "n":
                    break
                else :
                    print("Invalid input")              
        except Exception as e:
            print(e)           
         