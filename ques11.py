import os
# To add line number in front of every line
f = open("line.txt", "r")
f1 = open("line1.txt", "w+")
numb = 1
data = f.readlines()
for i in range(0, len(data) - 1):
    a = list(data[i])
    a.insert(numb,0)
    f1.write(str(a))
    numb += 1