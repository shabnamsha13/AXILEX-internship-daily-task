#add update and delete elements
student = {
    "Name": "SHABNAM",
    "USN": "4UB2MC087",
    "Course": "MCA",
    "Sem": 3
}

print("Original Dictionary:")
print(student)

# Adding a new element
student["College"] = "UBDT College"
print("\nAfter Adding College:")
print(student)

# Updating an element
student["Sem"] = 4
print("\nAfter Updating Semester:")
print(student)

# Deleting an element
del student["Course"]
print("\nAfter Deleting Course:")
print(student)



