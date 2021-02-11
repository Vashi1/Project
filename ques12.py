# program to append data to Security.txt
# Write a program that asks the new user
#  about user id and pass
# word and then appends it to a file “Security.txt” provided the given user id does
#  not exists in the file. If it exists then display error 
# message, “User id already exists” and prompt the user to re enter th
# e user id. Also make sure that the password is atleast 8 character
# s long with atleast a digit and a special character out of “$,@,%” in it.
import re
def check_password_length(password):
    length = len(password)
    global password_length_check
    if length < 8:
        print("[!]Password should be atleast 8 characters long")
        print("[!]Password is ", length, " character(s) long")
        check_password_length = False
    else:
        print("[!] Password is ", length, " characters")
        print("[!] Your password length is good")
        check_password_length = True



f = open("Security.txt", "r+")
uid  = int(input("Enter the uid : "))
passwor = input("Enter the password : ")
data = f.readlines()
uifile = 0
for i in data:
   i = i.rstrip('\n') 
   if uid == int(i[0]):
            print("[!] The user_id already exists")
            break
   else:
       uifile == 1
if uifile == 1:
           check_password_length(passwor)
           if check_password_length:
                    if re.search("[0-9]", passwor):
                          if re.search("[%@$]", passwor):
                            pass
                          else:
                              print("Password must contain special characte $, % or @ ")
                    else:
                        print("Password must contain a digit")
                        
           else:
               print("Password must be 8 chars longs")
else:
    print()