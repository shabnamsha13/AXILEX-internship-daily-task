# store student records into a file
with open("students.txt", "a") as file:
    name = input("Enter Student Name: ")
    usn = input("Enter USN: ")
    course = input("Enter Course: ")

    file.write("Name: " + name + "\n")
    file.write("USN: " + usn + "\n")
    file.write("Course: " + course + "\n")
    file.write("----------------------\n")

print("Student record stored successfully.")
