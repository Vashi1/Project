# TO perform sql operations using python
def create_table():
    cur.execute("""create table bank
                 (
                     accno int,
                     name char(30),
                     balance int,
                     mobno int(11),
                     email_id char(30)
                 )""")


def disp_all():
    cur.execute("select * from ")
    pass


def insert_record():
    accno = int(input("Enter the account number : "))
    name = input("Enter the customer name : ")
    balance = int(input("Enter the balance : "))    
    mobno = int(input("Enter the mobile number : "))
    email_id = input("Enter the email_id : ")
    cur.execute("insert into")


def search_ano():
    pass


def search_cname():
    pass


def search_bal():
    pass


def del_ano():
    pass


def del_cname():
    pass


import mysql.connector as sql
from tabulate import tabulate
myql = sql.connect(host="localhost", user="root")
cur = myql.cursor()
cur.execute("create database bank")
myql.commit()
cur.execute("use bank")
myql.commit()
print("\t\t\tMain Menu\t\t\t")
while True:
    print("1.Create table ")
    print("2.Insert record in table")
    print("3.Display all records")
    print("4.Search on basis of account number")
    print("5.Search on basis of Customer Name")
    print("6.Delete on basis of account number")
    print("7.Delete on basis of customer name")
    print("8.Search and display on basis of account balance")
    ch = input("Enter your choice : ")
    if ch == "1":
        create_table()
    elif ch == "2":
        insert_record()
    elif ch == "3":
        disp_all()
    elif ch == "4":
        search_ano()
    elif ch == "5":
        search_cname()
    elif ch == "6":
        del_ano()
    elif ch == '7':
        del_cname()
    elif ch == "8":
        search_bal()
    else:
        print("Please enter a valid input")