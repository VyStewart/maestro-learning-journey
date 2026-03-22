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