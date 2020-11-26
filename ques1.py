# Program to read 4 digit number and calculate the sum of square of first 2 digits 
numb = input("Enter the number : ")
# Check length
if len(numb) == 4:
    sum_sq = 0
    numb = int(numb)
    a = numb % 100
    b = numb // 100
    sum_sq = a ** 2 + b ** 2
    print(sum_sq)
else:
    print("Please enter a 4 digit number")