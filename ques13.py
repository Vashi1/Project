import csv


def add_info(nme, phno):
    f = open("PhoneDirectory.csv", "a")
    csvwriter = csv.writer(f)
    lis_temp = [nme, phno]
    csvwriter.writerow(lis_temp)

# Problem in display_info
def display_info():
    f = open("PhoneDirectory.csv", "r")
    print("\t\t\tPhone Directory\t\t\t")
    for i in f:
        data_temp = [i]
        print(data_temp)
        #print("Subscriber Name : ", data_temp[0], "Phone Number : ", data_temp[1], sep="\t")


while True:
    name = input("Enter the subscriber name : ")
    ph_no = int(input("Enter the phone number : " ))
    add_info(name, ph_no)
    ch = input("Do you want to continue(y/n) : ")
    if ch == "y":
        pass
    elif ch == "n":
        display_info()
        break
    else:
        print("Please enter a valid input!!")