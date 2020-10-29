# Binary Search
def binarysearch(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid -1
        else:
            return mid
    return -1

lit = []
while True:
    numb = int(input("Enter the number : "))
    lit.append(numb)
    choice = input("Do you want to continue(y/n):")
    if choice.lower() == "y":
        pass
    elif choice.lower() == "n":
        break
    else:
        print("Please enter a valid input!")
x = int(input("Enter the element to search : "))    
flag = binarysearch(lit, x)
if flag == -1:
    print("The element ", x, "was not present in the list")
else:
    print("The element ", x, "was present in the list at index", flag)