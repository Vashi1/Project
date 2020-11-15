# Program to read 4 digit number and calculate the sum of square of first 2 digits 
numb = int(input("Enter the number : "))
sum_sq = 0
a = numb % 100
b = numb // 100
sum_sq = a ** 2 + b ** 2
print(sum_sq)
