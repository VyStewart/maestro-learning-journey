### Maestro Challenge
### Topic: Finding Duplicates in a List
### Date: April 17 - 2026

'''
Given a list of numbers, find and return a list of duplicates.
'''  

def find_duplicates(nums):
    "Return a list of duplicates from the input list."
    seen = []
    duplicates = []
    
    for num in nums:
        if num in seen:
            if num not in duplicates:
                duplicates.append(num)
        else:
            seen.append(num)
            
    return duplicates, seen

duplicates, seen = find_duplicates([1, 2, 3, 4, 2, 5, 1, 11, 18, 6, 9, 3, 4])
print("Duplicates numbers:", duplicates)            # Output: Duplicates: [2, 1]
print("Seen numbers:", seen)                        # Output: Seen numbers [1, 2, 3, 4, 5, 11, 18, 6, 9]