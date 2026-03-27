### CS102 - Data structures & algorithms 
### Week 04 - Searching and sorting
### Date: March 26 - 2026

# Binary search with large sorted collections
"""
Binary search is an efficient algorithm for finding a target value within a sorted collection. 
It works by repeatedly dividing the search interval in half. If the target value is less than the middle
element, the search continues in the left half; if it is greater, the search continues in the right half.
This process continues until the target value is found or the search interval is empty.
"""

def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
test1 = binary_search([2, 3, 5, 8, 15, 19, 24], 15 )
test2 = binary_search([1, 3, 5, 8, 10, 36, 38, 40, 45], 38)

print(test1)  # should print 4
print(test2)  # should print 6

