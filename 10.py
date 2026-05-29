stack = []

while True:
    print("\n1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = int(input("Enter element: "))
        stack.append(item)
        print("Inserted")

    elif choice == 2:
        if len(stack) == 0:
            print("Stack Underflow")
        else:
            print("Deleted:", stack.pop())

    elif choice == 3:
        if len(stack) == 0:
            print("Stack Empty")
        else:
            print("Top Element:", stack[-1])

    elif choice == 4:
        print("Stack Elements:", stack)

    elif choice == 5:
        break

    else:
        print("Invalid Choice")