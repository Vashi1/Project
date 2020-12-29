# To write and read contents in a text file and reverse it
for i in range(0, 15):
    f = open('Poem1.txt', 'a')
    line = input("Enter the line : ")
    f.write(line)
    f.close()

f = open("Poem1.txt", "r")
data = f.read()
print(data[::-1])
