# TO perform sql operations using python
import tabulate
def create_table():
    cur.execute("""create table bank1
                 (
                     accno int,
                     name char(30),
                     balance int,
                     mobno int(11),
                     email_id char(30)
                 )""")


def disp_all():
    cur.execute("select * from bank1")
    table = cur.fetchall()
    headers = ["accno", "name", "balance", "mobno", "emailid"]
    print(tabulate(table, headers, tablefmt="grid" ))
    pass


def insert_record():
    accno = int(input("Enter the account number : "))
    name = input("Enter the customer name : ")
    balance = int(input("Enter the balance : "))    
    mobno = int(input("Enter the mobile number : "))
    email_id = input("Enter the email_id : ")
    cur.execute("insert into bank1 values({}, '{}', {}, {}, '{}')".format(accno, name, balance, mobno, email_id))
    myql.commit()


def search_ano():
    accn = int(input("Enter the accno : "))
    cur.execute("select * from bank1 where accno = {}".format(accn))
    data = cur.fetchall()
    if data == []:
        print("no such record exists")
    else:
        print(tabulate(data, headers=["accno", "name", "balance", "mobno", "emailid"], tablefmt="grid"))

def del_bal():
    bal = input("Enter the balance : ")
    cur.execute('delete from bank1 where balance = {}'.format(bal))
    myql.commit()

def search_cname():
    name1 = input("Enter the customer name : ")
    cur.execute("select * from bank1 where name = '{}'".format(name1))
    data2 = cur.fetchall()
    if data2 == []:
        print("No such record exists")
    else:
        print(tabulate(data2, headers=["accno", "name", "balance", "mobno", "emailid"], tablefmt="grid"))
        


def search_bal():
    bal = int(input("Enter the balance : "))
    cur.execute("select * from bank1 where balance = {}".format(bal))
    data3 = cur.fetchall()
    if data3 == []:
        print("No such record exists")
    else:
        print(tabulate(data3, headers=["accno", "name", "balance", "mobno", "emailid"], tablefmt="grid"))


def del_ano():
    accn = int(input("Enter the accno : "))
    cur.execute("delete from bank1 where accno = {}".format(accn))
    myql.commit()    


def del_cname():
    cname = input("Enter the cname : ")
    cur.execute("delete from bank1 where name = '{}'".format(cname))
    myql.commit()    


import mysql.connector as sql
from tabulate import tabulate
myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@")
cur = myql.cursor()
cur.execute("create database if not exists bank")
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
    print("8.Delete on basis of balance")
    print("9.Search and display on basis of account balance")
    print("10.Quit")
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
    elif ch == '8':
        del_bal()
    elif ch == "9":
        search_bal()
    elif ch == '10':
        break
    else:
        print("Please enter a valid input")