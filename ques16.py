#WAP queue operations
def isempty(queue):
    if queue == []:
        return True
    else:
        return False


def display(queue):
    if isempty(queue):
        print("The queue is empty!")
    else : 
        if len(queue) == 1:
            print(queue[0] , " <-- front/rear")
        elif len(queue) == 2:
            print(queue[0], "<-- front")
            print(queue[1], "<-- rear")
        else:
            print(queue[0], " <-- front")
            for i in range(1, len(queue) - 1):
                print(queue[i])
            print(queue[-1], "<-- rear")


def insert(queue, ele):
    queue.append(ele)
    print("The element was added!")


def delete(queue):
    if isempty(queue):
        print("Underflow")
    else:
        element = queue.pop(0)
        print("The element ", element, "was deleted")


que = []
print("\t\t\tQUEUE OPERATIONS")
while True:
    print("1.Insert element")
    print("2.Delete element")
    print("3.Display element")
    print("4.Quit")
    ch = input("Enter your choice: ")
    if ch == "1":
        el = int(input("Enter the element : "))
        insert(que, el)
    elif ch == "2":
        delete(que)
    elif ch == "3":
        display(que)
    elif ch == "4":
        print("Bye!")
        break
    else:
        print("Please enter a valid input!")