### Lesson: List iii - mastering list iteration
### Date: 12-18-2025

## loop over indices
# Example
# index-based loop

animals = ["cat", "dog", "hamster", "parrot"]

length = len(animals)
for index in range(0, length):
    print(index, animals[index])

# Result:
    # 0 cat
    # 1 dog
    # 2 hamster
    # 3 parrot
    
# shorter/ pro version

animals = ["cat", "dog", "hamster", "parrot"]

length = len(animals)
for index in range(len(animals)):
    print(index, animals[index])
    
# Practice
# value-based pattern

numbers = [3, 7, 4, 9]

for number in numbers:
    print( number * 2)
    
# Challenge

numbers = [3, 7, 4, 9]

max_index = 0
for index in range(len(numbers)):
    if numbers[index] > numbers[max_index]:
        max_index = index

print("Index of largest number:", max_index)
print("Largest number:", numbers[max_index])

# Practice
# Mixed value- based loop and index-based loop

# Value-based: print each number
numbers = [3, 7, 7, 2, 7]

print("All numbers:")
for number in numbers:
    print(number)

# Index-based: print index and value
print("Index and numbers:")
for index in range(len(numbers)):
    print("Index:", index, "Number:", numbers[index])

# Index-based: print  indexes where the number 7 is
print("Index where number 7 is:")
for index in range(len(numbers)):
    if numbers[index] == 7:
        print(index)

# Challenge — Score Analysis

scores = [88, 73, 95, 60, 95, 82]

print("-------------------------")
print("All scores:")
for score in scores:
    print(score)

print("-------------------------")
print("Score details:")
for index in range(len(scores)):
    print(
        "Index:", index,
        "Score:", scores[index],
        "Final score:", scores[index] + 5
    )

print("-------------------------")
print("Indexes with top scores:")

# Find index of the first highest score
top_index = 0
for index in range(len(scores)):
    if scores[index] > scores[top_index]:
        top_index = index

top_score_value = scores[top_index]
print("Top score:", top_score_value)

# Find all indexes with the top score
top_indexes = []
for index in range(len(scores)):
    if scores[index] == top_score_value:
        top_indexes.append(index)

print("Indexes of all top scores:", top_indexes)

    