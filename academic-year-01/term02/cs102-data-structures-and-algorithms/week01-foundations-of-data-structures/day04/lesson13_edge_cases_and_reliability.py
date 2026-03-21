### CS102 - Data structures & algorithms 
### Week 01 - Foundations of data structures
### Date: March 21 - 2026
### lesson 13: Edge cases and reliability

# Example 1: guard against out of range access with length check

def top_three(scores):
    if len(scores) >= 3:
        first = scores[0]
        second = scores[1]
        third = scores[2]
        return [first, second, third]
    else: 
        return []
    
test = [100, 97, 94]
print(f'Top three scores is: {top_three(test)}')

# Example 2: guard against out of range access with try-except

def safe_get(items, index):
    try:
        return items[index]
    except IndexError:
        return None
    
result1 = (["banana", "apple", "grape"])
result2 = (["Josh,", "Marcus", "Damien"])
print(safe_get(result1, 2))
print(safe_get(result2, 5))

print(safe_get([19, 20, 40, 50], 2))
print(safe_get([5, 20, 45], 3))
       
