### Maestro Challenge
### Course: Python101
### Date: Feb 10 - 2026

'''
based on dictionary of names and their test scores:
- count how many students passed (score 70+)
- count how many failed (below 70)
- prints a summary dictionary
'''

scores = {
    "Alice": 85,
    "Bob": 67,
    "Carlar": 92,
    "Dan": 58,
    "Eve": 76
}

passed_count = 0
failed_count = 0


for value in scores.values():
    if value >= 70:
        passed_count += 1
            
    else:
        failed_count += 1
               
summary = {
    "pass": passed_count,
    "fail": failed_count
}

print(
    "Summary:", summary,
)
