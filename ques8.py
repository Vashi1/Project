# to delete duplicate elements 
def remove_duplicate(lis):
    final_list = []
    for num in lis:
        if num not in final_list:
            final_list.append(num)
    return final_list
a = eval(input("Enter the list : "))
data = remove_duplicate(a)
if data == a:
    print("No duplicates exist!")
else:
    print("The original list was : ")
    print(a)
    print("The new list after deleting duplicate elements is : ")
    print(data)
