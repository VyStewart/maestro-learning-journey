### CS101 - Week 06
### Software Engineering Principles
### Lesson 07: Turing long scrips into sharp functions
### Date: Jan 06 2026

# Example
name = input("Enter your name: ")
age_text = input("Enter your age: ")
age = int(age_text)

print("------SUMMARY--------")
print("Name:", name)
print("Age:", age)

if age < 13:
    group = "child"
else:
    if age < 20:
        group = "teen"
    else:
        if age < 65:
            group = "adult"
        else:
            group = "senior"

print("Age group:", group)

favorite_color = input("Enter your favorite color: ")
print("Nice, " + name + ", I like " + favorite_color + " too!")

years_to_100 = 100 - age
print(name, "will turn 100 in", years_to_100, "years.")

print("Goodbye", name + "!")

# Add function to the code 

def print_summary(name, age, group):
   print(
       f"\n------SUMMARY-------"
       f"\nName: {name}"
       f"\nAge: {age}"
       f"\nGroup: {group}"
   )

def get_user_info():
       name = input("Enter your name: ")
       age = int(input("Enter your age: "))
       return name, age                

def get_age_group(age):
    if age < 13:
        return "child"
    elif age < 20:
        return "teen"
    elif age < 65:
        return "adult"   
    else:
        return "senior"

name, age = get_user_info()
group =  get_age_group(age)
print_summary(name, age, group)

favorite_color = input("Enter your favorite color: ")
print(f"Nice, {name}! I like {favorite_color} too.")

years_to_100 = 100 - age
print(name, "will turn 100 in", years_to_100, "years.")

print(f"Good bye, {name}!")