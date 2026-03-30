### CS102 - Data structures & algorithms 
### Week 04 - Searching and sorting
### Date: March 29 - 2026

# Bubble sort
'''
Bubble sort is a simple sorting algorithm that repeatedly steps through the list, 
compares adjacent elements and swaps them if they are in the wrong order.
The process is repeated until the list is sorted. 
The algorithm gets its name because smaller elements "bubble" to the top of the list.
the biggest elements "sink" to the bottom of the list (the end of the list, the last position).
The time complexity of bubble sort is O(n^2) in the worst and average cases, 
and O(n) in the best case when the list is already sorted.
'''

# Implementation of bubble sort
a = [64, 34, 25, 12, 22, 11, 90]

# outer loop: repeat passes
for pas_num in range(len(a) - 1):
    # inner loop: go through neighbors
    for i in range(len(a) - 1):
        # if left neighbor is bigger than right neighbor, swap
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]

print(a)

# bubble sort with function

def bubble_sort(lst):
    for pas_num in range(len(lst) - 1):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

test1 = bubble_sort([89, 39, 45, 98, 12, 33, 22, 93, 80])
print(test1)
