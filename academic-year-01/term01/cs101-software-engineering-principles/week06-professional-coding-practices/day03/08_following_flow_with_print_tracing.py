### CS101 - Week 06
### Software Engineering Principles
### Lesson 08: Following Program Flow With Print Tracing
### Date: Jan 07 2026

# tracing function entry and exit

def greet(name):
    print(f"[DEBUG] Enter greet with name={name}")
    print("Hello,", name, "!")
    print("[DEBUG] Exit greet")
    
greet("Vy")

# tracing to an if/else

def classify_age(age):
    print(f"[DEBUG] Enter classify_age={age}")
    if age < 18:
        print("[DEBUG] Taking minor branch")
        print("Minor")
    else:
        print("[DEBUG] Taking adult branch")
        print("Adult")

classify_age(15)
classify_age(30)

# tracing to a for loop
def count_up_to(n):
    print(f"[DEBUG] Enter count_up_to with n={n}")
    for i in range(1, n + 1):
        print(f"[DEBUG] Loop iteration i={i}")
        print(i)
    print("[DEBUG] Finished loop in count_up_to")

count_up_to(3)


