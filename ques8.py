# to delete duplicate elements 
def repeat(x):
    size = len(x)
    repeated = []
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


lis = eval(input("Enter the list : "))
data = repeat(lis)
if data == []:
    print("No duplicate element exists")
elif data != []:
    while True:
        ele = int(input("Enter the element to be deleted : "))
        if ele in data:
            de = lis.remove(ele)
            ch = input("Do you want to continue(y/n) : ")
            print(lis, " <= list")
            if ch == "y":
                pass
            elif ch == "n":
                break
        else:
            print("The element cannot be deleted")

    