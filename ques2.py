# Write a program to find whether an inputted number is perfect or not
numb = int(input("Enter the number : "))
flag = 0
half = numb // 2 + 1
for i in range(1, half):
    if (i ** 2) == numb:
        flag = 1

if flag == 0:
    print(numb, "is not a perfect number")
elif flag == 1:
    print(numb , "is a perfect number")
