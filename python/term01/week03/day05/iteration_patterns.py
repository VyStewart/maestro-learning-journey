### Lesson-Dictionaries ii: iteration patters
### Date: 12-20-2025

## Keys loop and using keys loop to loop over indicies and then using them to get the values.
# key loop: for x in my_dict:

favorite_colors = {
    "Alice": "blue",
    "Bob": "green",
    "Charlie": "red",
    "Soleil": "yellow",
    "Maya": "green"
}

for person in favorite_colors:
    print(person)   
    
print()
# Using key loop and then using the key to get the value
for person in favorite_colors:
    color = favorite_colors[person]
    print(person, "likes", color)
    
print()   
## values loop with .values():
# for y in my_dict.values():

for color in favorite_colors.values():
    print("Favorite color:", color)

print()   
## key-value pair loop with. items() unpacks each pair and get the key(name) and the value(color)
# for x, y in my_dict.items():

for person, color in favorite_colors.items():
    print(person, "'s favorite color is:", color)

print()    
# Using key-pair loop to find out how many people like same color

blue_count = 0

for person, color in favorite_colors.items():
    if color == "blue":
        blue_count += 1

print(blue_count)

green_count = 0

print()
for person, color in favorite_colors.items():
    if color == "green":
        green_count += 1
        print(person, "likes", color)
        
print("Number of people like green:", green_count)

print()       
# Boss-level Challenge — Student Score Analysis

student_scores = {
    "Alice": 95,
    "Bob": 82,
    "Charlie": 67,
    "Diana": 74,
    "Evan": 59,
    "Fiona": 88,
    "Soleil": 90,
    "Joshua": 98,
}

print("Name and score for each student:")
# Using key-value loop
for name, score in student_scores.items():
    print(name, "'s score is:", score)

print("\nCount how many students passed and failed the exam:")
passed = 0
failed = 0

for score in student_scores.values():
    if score >= 70:
        passed += 1
    else:
        failed += 1

print(f"Number of students who passed: {passed}")
print(f"Number of students who failed: {failed}")

print("\nStudents who scored 90 or above:")
excellent = 0

for name, score in student_scores.items():
    if score >= 90:
        excellent += 1
        print(name, "'s score is:", score)

print(f"Number of students with excellent scores: {excellent}")
