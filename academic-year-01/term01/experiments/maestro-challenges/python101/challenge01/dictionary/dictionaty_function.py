### Maestro Challenge
### Course: Python101
### Date: Feb 13 - 2026

# Dictionary Function

def sumarize_scores(scores, passing_score):
    '''
    Create function sumarize_scores to get the svores and passing score
    for flexible resuable structure
    
    :param scores: Description
    :param passing_score: Description
    '''
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
    
    return summary

# test calling
scores = {
    "Alice": 85,
   "Bob": 67,
   "Carla": 92,
   "Dan": 58,
   "Eve": 76
}

passing_score = 70

report = sumarize_scores(scores, passing_score)
print("Summary Report")
print(report)