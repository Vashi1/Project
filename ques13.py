import csv
def add_info(nme, phno):
    f = open("PhoneDirectory.csv", "a")
    csvwriter = csv.writer(f)
    lis_temp = [nme, phno]
    csvwriter.writerow(lis_temp)

# Problem in display_info
def display_info():
    f = open("PhoneDirectory.csv", "r")
    reader = csv.reader(f)
    print("\t\t\tPhone Directory\t\t\t")
    for i in reader:
        data_temp, number1 = i
        print("Subscriber Name : ", data_temp, "Phone Number : ", number1, sep="\t")


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