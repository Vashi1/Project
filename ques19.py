# TO perform sql operations using python
import mysql.connector as sql
user = input("Enter the mysql username : ")
password = input("Enter the mysql password")
myql = sql.connect(host="localhost", user=user, password=password)
cur = myql.cursor()
cur.execute("create database bank")
myql.commit()
cur.execute("use bank")
myql.commit()
print("\t\t\tMain Menu\t\t\t")
while True:
    print("1.Create table ")
    print("2.Insert table")
    print("3.Display all records")
    print("4.Search on basis of account number")
    print("5.Search on basis of Customer Name")
    print("6.Delete on basis of account number")
    print("7.Delete on basis of account number")
    
