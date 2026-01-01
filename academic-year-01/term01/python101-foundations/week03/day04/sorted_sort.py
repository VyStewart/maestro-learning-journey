### Lesson: Ordering lists sorted() vs sort()
### Date: 12-18-2025

## In order to sort a list:
# .sort(): change the same list (in place/order)
#sorted(): makes a new sorted list, orginal stays the same.

# Example
# .sort
numbers = [5, 2, 9, 11]
print(f"Before sort: {numbers}")            # [5, 2, 9, 11]

numbers.sort()
print(f"After sort: {numbers}")             # [2, 5, 9, 11]

# sorted()
scores = [30, 10, 50, 20]
sorted_scores = sorted(scores)

print("Original scores:", scores)           # [30, 10, 50, 20]
print(f"Sorted scores: {sorted_scores}")    # [10, 20, 30, 50]

names = ["Charlie", "Alice", "Bob", "Luna", "Joshua"]
sorted_names = sorted(names)

print("Original nmanes:", names)                # ["Charlie, "Alice", "Bob","Luna", "Joshua"]
print(f"Name after sorted: {sorted_names}")     # ["Alice", "Bob", "Charlie", "Joshua", "luna"]

## Custom order with key= to tell Python what to sort by
# Example: 
# Sort words by their length using len
words = ["banana", "fig", "apple", "kiwi"]
words_by_length = sorted(words, key=len)

print("Original_words:", words)                     # ["bnana", "fig", "apple", "kiwi"]
print(f"Sorted by length: {words_by_length}")       # ["fig", "kiwi", "apple", "banana"]

# When the key values are equa (same length), normal string comparison(alphabetical) decides the order
words = ["pear", "plum", "kiwi", "fig"]

sorted_words = sorted(words, key=len)
print("Words after sorted:", sorted_words)         # ["fig", "pear", "plum", "kiwi"]

# Sort by descending order with reserve=True, still using key=len
fruits = ["pear", "plum", "kiwi", "fig"]

sorted_fruits_desc = sorted(fruits, key=len, reverse=True)
print("Fruits sorted by length(descending:)", sorted_fruits_desc)
# Fruits sorted by length(descending): ["pear", "plum", "kiwi", "fig"]

# Exercise — Sorting Lists
cities = ["Dallas", "LA", "Seattle", "Rome", "NY", "Austin", "Houston"]

print("Sort the list alphabetically (in place)")
# Using .sort()
cities.sort()
print(cities)

print("Create a new list sorted by name length (shortest to longest)")
# Using sorted() with key=len
sorted_cities = sorted(cities, key=len)
print(f"Cities after sorting by length: {sorted_cities}")

print("Create a new list sorted by name length (longest to shortest)")
# Using sorted() with key=len and reverse=True
sorted_cities_desc = sorted(cities, key=len, reverse=True)
print(
    f"Cities sorted from longest to shortest name: {sorted_cities_desc}"
)



