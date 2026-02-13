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
passed_student = []
failed_student = []

for name, value in scores.items():
    if value >= 70:
        passed_count += 1
        passed_student.append(name)
            
    else:
        failed_count += 1
        failed_student.append(name)
               
summary = {
    "pass": passed_count,
    "fail": failed_count
}

print(
    "Summary:", summary,
    "\nPassed Student:", passed_student,
    "\nFailed Student:", failed_student  
)

summary = {
        "pass": {
            "count": passed_count,
            "students": passed_student
        },
        "fail": {
            "count": failed_count,
            "students": failed_student
        }
}

print("Summary:", summary)