### CS102 - Data structures & algorithms 
### Week 04 - Searching and sorting
### Date: March 23 - 2026

# Why searcing matters : searhing in loop and searching in dictionaries
books_list = ["Dune", "It", "Emma", "Dracula", "Sapiens"]
target = "Dracula"

checks = 0
found = False

# Searching in a list with a loop
for title in books_list:
    checks += 1
    if title == target:
        found = True
        break

print(f"Checks: {checks}")
print(f"Found: {found}")

# Searching in a dictionary
books_dict = {
    "Dune": "Frank Herbert",
    "It": "Stephen King",
    "Emma": "Jane Austen",
    "Dracula": "Bram Stoker",
    "Sapiens": "Yuval Noah Harari"
}

checks_dict = 1
result = books_dict.get(target, None)

print(f"Checks: {checks_dict}")
print(f"Found: {result is not None}")