### CS101 - Week 06
### Software Engineering Principles
### Lesson 14: Validating inputs before they break thing
### Date: Jan 11 2026

# Using guard cluases
def cookies_per_person(total_cookies, people):
    return total_cookies / people

print(cookies_per_person(12, 3))
print(cookies_per_person(12, 0))   # uh oh
print(cookies_per_person("12", 3)) # uh oh

# Add guard clauses
def cookies_per_person(total_cookies, people):
    if not isinstance(people, int):
        return None
    if people <= 0:
        return None

    if not isinstance(total_cookies, (int, float)):
        return None
    if total_cookies <= 0:
        return None

    return total_cookies / people

print(cookies_per_person(12, 3))
print(cookies_per_person(12, 0))
print(cookies_per_person(12, -1))
print(cookies_per_person(12, 2.5))
print(cookies_per_person(12, "3"))
print(cookies_per_person(-5, 3))
print(cookies_per_person("12", 3))

# Practice
sample_inputs = ["10", "5", "3"]

def safe_average(str_numbers):
    total = 0
    count = 0
    for s in str_numbers:
        if not s.isdigit():
            return None   
        value = int(s)
        if value <= 0:
            return None
        total += value
        count += 1
    if count == 0:
        return None
    return total / count
    print("raw values:", s)

safe_average(sample_inputs)
print(safe_average(["10", "5", "3"]))      # should not return None
print(safe_average(["10", "0", "3"]))      # should return None
print(safe_average(["10", "-5", "3"]))     # will also be None (because of "-")
print(safe_average(["10", "x", "3"]))      # None