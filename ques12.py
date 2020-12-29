# program to append data to Security.txt
f = open("Security.txt", "r+")
uid  = int(input("Enter the uid : "))
password = input("Enter the password : ")
data = f.readlines()
for i in data:
    print(i)
    print(i[0])
    if i[0] == uid:
        print("User id already exists")