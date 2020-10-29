list1 = eval(input("Enter the first list:"))
list2 = eval(input("Enter the second list:"))
dic = {}
if len(list1) != len(list2):
    print("Please enter equal number of elements in both the lists!")
else:
    for i in range(0, len(list2)):
        dic1 = {list1[i] : list2[i]}
        dic.update(dic1)
    print("Dict = ", dic)