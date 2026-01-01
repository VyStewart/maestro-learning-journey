### Lesson: Dictionaries i - keys and values
### Date: 12-20-2025

## A dictionary stores key - value pairs
# Example
favorite_colors = {
    "Hannah": "violet",
    "Alex": "purple",
    "Soleil": "yellow"
}

print(f" Favorite Colors:){favorite_colors}")

favorite_colors["Jordan"] = "green"
favorite_colors["Hannah"] = "blue"

print(f" Favorite Colors after updated: {favorite_colors}")

## keys nust be immutable 
# valid keys: string, int
# bad keys: invalid keys (a list, a dictionary)
# Example
good_key = {
    "Name": "Alice",
    10: "ten"
}

print(good_key["Name"])
print(good_key[10])

# All-in-one Challenge — Dictionary Practice

student = {
    "Name": "Vy",
    "Age": 21,
    "Course": "Python"
}

# Access a value by key
print(student["Name"])

# Add a new key-value pair
student["Grade"] = "A"

# Update an existing value
student["Course"] = "Advanced Python"

# Print the full dictionary
print(student)

# Access individual values
print(student["Name"])
print(student["Age"])
print(student["Course"])
print(student["Grade"])
