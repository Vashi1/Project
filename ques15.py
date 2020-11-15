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

