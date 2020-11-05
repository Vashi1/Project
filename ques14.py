#WAP to show MYSQL database connectivity with python
import mysql.connector as sql
myql = sql.connect(host="localhost", user="Rakshith", password="Rakshith1@")
print(myql.is_connected())
print("Connected with MYSQL")