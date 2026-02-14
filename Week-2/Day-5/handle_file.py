try:
    file = open("student.txt", "r")
    data = file.read()
    print(data)
    file.close()

except FileNotFoundError:
    print("File not found. Check the file name.")

