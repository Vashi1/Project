#WAP to perform all stack operations
def isempty(stck):
    if stck == []:
        return True
    else:
        return False


def pop(stck):
    if isempty(stck):
        print("Underflow")
    else:
        elem = stck.pop()
        print(elem, "was deleted")


def push(stck, e):
    stck.append(e)
    print("Element ", e, " was added in the list")
    

def display(stck):
    if isempty(stck):
        print("Stack is Empty!")
    else:
        for i in range(len(stck) - 1, -1, -1):
            print(stck[i])


stack = []
while True:
    print("\t\t\t\tSTACK OPERATION\t\t\t\t")
    print("1.PUSH")
    print("2.POP")
    print("3.DISPLAY")
    print("4.Quit")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        ele = int(input("Enter the element : "))
        push(stack, ele)
    elif ch == 2:
        pop(stack)
    elif ch == 3:
        display(stack)
    elif ch == 4:
        print("bye!")
        break
    else:
        print("Invalid Input!")

