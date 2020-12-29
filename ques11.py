# To add line number in front of every line
f = open("line.txt", "r")
numb = 1
data = f.readlines()
for a in data:
    print(numb, a, sep = " ")
    numb += 1
f.close()