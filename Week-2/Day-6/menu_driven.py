# menu driven program
while True:
    print("\n1. Square")
    print("2. Cube")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        num = int(input("Enter number: "))
        print("Square =", num * num)
    elif choice == '2':
        num = int(input("Enter number: "))
        print("Cube =", num * num * num)
    elif choice == '3':
        print("Exiting Program")
        break
    else:
        print("Invalid Choice")
