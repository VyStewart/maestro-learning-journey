### Lesson: Common methods
### Date: 12-18-2025


## Append(value): Add a single item to the end of existing list
# Example 1:
numbers = [1, 2, 3]

numbers.append(10)
print(numbers)              # [1, 2, 3, 10]

# Eaxmple: append a single item (a list)
animals = ["cat", "dog", "bunny"]

animals.append(["parrot", "hamster"])
print(animals)                  # ["cat", "dog", "bunny", ["parrot", "hamster"]]

## Insert(index, value): use an index to add a value at the axact position
# Example:
nums = [10, 20, 30]

nums.insert(1, 99)
print(nums)                 # [10, 99, 20, 30]

# Example: append() and insert()
pets = ["cat", "hamster"]

pets.append("parrot")
pets.insert(1, "dog")

print(pets)                 # ["cat", "dog", "hamster", "parrot"]

## Removing items from a lit
# remove(value): delete by value and return None
# pop(index): delete by postion and aslo return the removed intem

# Example: remove()
nums = [1, 2, 3, 2]

nums.remove(2)
print(nums)             # [1, 3, 2]
# remove() scans from left to right and when it finds the first item and then stops

# Example: pop()
nums = [10, 20, 30]

removed = nums.pop(1)
print(nums)             # [10, 30]
print(removed)          # 20

## Extend(): unpack add many items at one 
nums = [10, 30, 45, 60]

nums.extend([32, 93])
print(nums)             # [10, 30, 45, 60, 32, 93]

# Integrated challenge 
nums = [10, 20, 30]

print("Use append to 40")
nums.append(40)
print(nums)

print("Use insert to put 15 at index 1")
nums.insert(1, 15)
print(nums)

print("Use remove to remove the value 30")
nums.remove(30)
print(nums)

print("Use pop to remove the first element aand store it")
popped = nums.pop(0)
print(nums)
print("Popped:", popped)

print("Use extend to add 2 numbers at one")
nums.extend([50, 60])
print(nums)

# Real-life Scenario — Boss-level Challenge
# Managing a simple to-do list

todos = ["wash dishes", "do homework", "call Josh"]

print("Add 'pay bills' to the end of the list")
# Using append()
todos.append("pay bills")
print(todos)

print("Add 'buy groceries' to the beginning of the list")
# Using insert()
todos.insert(0, "buy groceries")
print(todos)

print("Remove 'do homework' after completing it")
# Using remove()
todos.remove("do homework")
print(todos)

print("After calling Josh, remove the task from the list")
# Using pop()
done_task = todos.pop(2)
print(todos)
print("Completed task:", done_task)

print("Add two more tasks to the list")
# Using extend()
todos.extend(["workout", "reading book"])
print(todos)
