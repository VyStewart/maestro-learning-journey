### Maestro Challenge
### Course: Python101
### Date: Feb 10 - 2026

# Dictionary Advanced version

scores = {
    "Alice": 85,
    "Bob": 67,
    "Carlar": 92,
    "Dan": 58,
    "Eve": 76
}

passing_score = 70
passed_students = []
failed_students = []

for name, value in scores.items():
    if value >= passing_score:
        passed_students.append(name)
        
    else:
        failed_students.append(name)
        
summary = {
    "passing_score": passing_score,
    
    "pass": {
        "count": len(passed_students),
        "students": passed_students
        },
    
    "fail": {
        "count": len(failed_students),
        "students": failed_students
    }
}

print("Summary Report")
print(summary)