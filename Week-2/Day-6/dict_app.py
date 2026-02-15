# dictionary application
data = {
    "101": "Asha",
    "102": "Ravi",
    "103": "Kiran"
}
roll = input("Enter Roll Number to Search: ")
if roll in data:
    print("Student Name:", data[roll])
else:
    print("Record Not Found")
