### CS102 - Data structures & algorithms 
### Week 04 - Searching and sorting
### Date: March 29 - 2026

# Insertion sort
'''
Insertion sort is a simple sorting algorithm that builds the sorted list one item at a time.
It works by repeatedly taking the next unsorted item and inserting it into the correct position 
in the already sorted portion of the list.
'''

# Implementation of insertion sort
nums = [12, 11, 13, 5, 6]

for i in range(1, len(nums)):          # outer loop: pick element at index i
    key = nums[i]                      # value we’re inserting
    j = i - 1                          # start checking from the element on the left

    while j >= 0 and nums[j] > key:    # while left element is bigger than key
        nums[j + 1] = nums[j]          # shift it right
        j -= 1                         # move left

    nums[j + 1] = key                  # insert key into the hole

print(nums)

# insertion sort with function

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # shift right
            j -= 1

        arr[j + 1] = key  # insert key

    return arr

test1 =  insertion_sort([2, 3, 93, 11, 18, 80, 24, 26])
print(test1)
