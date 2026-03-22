### CS102 - Data structures & algorithms 
### Week 02 - Stacks and queues
### Date: March 21 - 2026

# Queue operations: enqueue and dequeue
queue = []
queue.append("Alice")
queue.append("Bob")
queue.append("Charlie")
queue.append("Josh")
print(queue)

served = queue.pop(0)
print("\nServed:", served)
print("\nQueue now:", queue)

# Queue operation: safe pattern for dequeueing
queue = []
queue.append("A")
queue.append("B")
queue.append("C")
if queue:
    served1 = queue.pop(0)
    served2 = queue.pop(0)
    print(f"\nServed: {served1} and {served2}")
else:
    print("\nQueue is empty, nothing to serve.")

print("\nFinal queue:", queue)

# Implementing queues wiht deques from the collections module
from collections import deque

ice_cream_line = deque()
ice_cream_line.append("Damien")
ice_cream_line.append("Marcus")
ice_cream_line.append("Josh")
ice_cream_line.append("Sunshine")

served1 = ice_cream_line.popleft()
print("\nServed:", served1)

served2 = ice_cream_line.popleft()
print("\nServed:", served2)

served3 = ice_cream_line.popleft()
print("\nServed:", served3)
print("\nCurrent Line:", list(ice_cream_line))

served4 = ice_cream_line.popleft()
print("\nServed:", served4)

print("\nFinal Line:", list(ice_cream_line))
