# To check whether a sting is palindrome or not
string = input("Enter the string : ")
a = ""
for i in range(len(string) - 1, -1, -1):
    a = a + string[i]
if a == string:
    print("The string ", string, "is a palindrome")
else:
    print("The string ", string , "is not a palindrome")
