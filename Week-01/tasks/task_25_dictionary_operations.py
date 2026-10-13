# Creating a dictionary
student = {
    "name": "Ali",
    "course": "AI/ML",
    "marks": 92
}
print("Student dictionary:", student)

# Accessing values
print("Name:", student["name"])
print("Grade:", student.get("grade", "Not Assigned"))

# Adding and modifying elements
student["grade"] = "A"
student["marks"] = 95
print("Updated student:", student)

# Dictionary methods
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

# Removing an item
student.pop("grade")
print("After pop('grade'):", student)
