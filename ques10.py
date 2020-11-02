# To write and read contents in a text file and reverse it
for i in range(0, 15):
    f = open('poem.txt', 'a')
    line = input("Enter the line : ")
    f.write(line)
    f.close()

f = open("poem.txt", "r")
data = f.read()
print(data[::-1])
