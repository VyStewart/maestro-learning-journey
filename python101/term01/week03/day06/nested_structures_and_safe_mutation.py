### Lesson-Nested Structure and Safe Mutation
### Date: 12-21-2025

## Stepping into nested lists on level at a time
# Example

matrix = [
    [10, 11, 12],
    [20, 21, 22],
    [30, 31, 32],
]

row = matrix[2]
value = matrix[2][0]

print(row)                          # [30, 31, 32]
print(value)                        # 30
print(matrix)                       # [[10, 11, 12][20, 21, 22][30, 31, 32]]       

print("\n")   
print(matrix[1])                    # [20, 21, 22]
print(matrix[1][2])                 # 22
print(matrix[2][0])                 # 30

## Nested dictionary
# Example

school = {
    "class7": {
        "teacher": "Ms.Lee",
        "students": ["Anna", "Ben", "Carlos"]
    }
}

students = school["class7"]["students"]
first_student = students[0]

print("\n")
print(school)
print(school["class7"])
print(school["class7"]["teacher"])

print("\n")
print(students)
print(first_student)
print(school["class7"]["students"][2])

## Safe reading with dic.get() prevents crash when a key mising 

print("\n")
print(school.get("class7"))
print(school.get("class8"))
print(school.get( "N/A"))

## Adding a new student to school

print("\nbefore:", school)
student = school["class7"]["students"]
students.append("Diana")
print("\nAfter:", school)

students.append("Evan")
print("\n", school)

# Add a new student safely with .get()

students = school.get("class7", {}).get("students", [])
print("\n", students)

students.append("Soleil")
print("\n", students)
print("\n", school)

# Safe read of class7

class7 = school.get("class7")
if class7 is not None:
    students = class7.get("students", [])
    students.append("Joshua")
    print("\nAfter safe add:", school)
else:
    print("\nClass7 not found")
    
# Nested Dictionary Challenge — School Example

school = {
    "class7": {
        "teacher": "Ms Lee",
        "students": ["Anna", "Ben"]
    },
    "class8": {
        "teacher": "Mr Kim",
        "students": ["Mia"]
    }
}

print(school)
print("\nClass 7:", school.get("class7"))
print("\nClass 8:", school.get("class8"))

# Safely access student lists
students_class7 = school.get("class7", {}).get("students", [])
students_class8 = school.get("class8", {}).get("students", [])

# Add new students
students_class7.append("Carlos")
students_class8.append("Nina")

print("\nSchool after adding students:")
print(school)
