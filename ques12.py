# WAP to add a line number in front of everyline
# Not done
f = open("ques12.txt", "r+")
b = open("ques12new.txt", "a")
data = f.readlines()
count = 0
for i in data:
    a = [i]
    a.insert(0, count)
    for c in a:
        d = c
        print(d)
    b.write(d)
    count += 1

f.close()