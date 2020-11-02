# to count word occurances
f = open('poem.txt', 'r')
a = input("Enter the word : ")
count = 0
data = f.readlines()
for i in data:
    for b in i.split():
        if b == a:
            count += 1
print("The number of times the word occured is", count)