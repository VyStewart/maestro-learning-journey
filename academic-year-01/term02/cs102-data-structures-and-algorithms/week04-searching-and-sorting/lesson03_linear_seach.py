### CS102 - Data structures & algorithms 
### Week 04 - Searching and sorting
### Date: March 23 - 2026

# Searching matters: linear search with small and un sorted data
'''
Linear search is a simple algorithm that checks each element in a list 
one by one until it finds the target or reaches the end of the list. 
It is easy to implement and works well for small or unsorted data, 
but it can be inefficient for large lists because it may require checking every element.
'''

def linear_search(lst, target):
    index = - 1
    found = False
    for i in range(len(lst)):
        if lst[i] == target:
            index = i
            found = True 
            break
    return index

print(linear_search([10, 20, 30, 40], 30))  # should print 2
print(linear_search([10, 20, 30, 40], 50))  # should print -1