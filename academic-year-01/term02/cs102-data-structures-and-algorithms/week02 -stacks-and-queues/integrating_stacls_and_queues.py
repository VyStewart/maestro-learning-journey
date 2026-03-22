### CS102 - Data structures & algorithms 
### Week 02 - Stacks and queues
### Date: March 21 - 2026

# Integrating stacks and queues
from collections import deque

queue = deque(["Alice", "Bob", "Cara"])
backpack = ["rope", "torch"]

first_out = queue.popleft()
if backpack:
    backpack.pop()
    backpack.append("gemstone")
queue.append(first_out)

print("New queue:", list(queue))
print("\nAlice backpack:", backpack)


# Example 2: Cave exploration with stacks and queues
from collections import deque

queue = deque(["Alice", "Bob", "Cara"])
backpacks = {
    "Alice" : ["rope", "torch"],
    "Bob": ["map"],
    "Cara": ["potion"]
}

person = queue.popleft()
pack = backpacks[person]
if pack:
    pack.pop()
    pack.append("gemstone")
queue.append(person)

person= queue.popleft()
pack = backpacks[person]
if pack:
    pack.pop()
    pack.append("sword")
queue.append(person)

person = queue.popleft()
pack = backpacks[person]
if pack:
    pack.pop()
    pack.append("bag of gold")
queue.append(person)

print("\nQueue:", list(queue))
print("\nUpdated backpacks:", backpacks)

# Advanced: integrating stacks and queues using for _ in range loops
from collections import deque

queue = deque(["Alice", "Bob", "Cara"])
backpacks = {
    "Alice" : ["rope", "torch"],
    "Bob": ["map"],
    "Cara": ["potion"]
}

treasures = {
    "Alice": ("bag of gemstone"),
    "Bob": ("devided sword"),
    "Cara": ("bag of gold")
}

for _ in range(3):
    person = queue.popleft()
    pack = backpacks[person]
    if pack:
        pack.pop()
        pack.append(treasures[person])
    queue.append(person)

print("\nQueue after first run:", list(queue))
print("\nUpdated backpacks:", backpacks)
