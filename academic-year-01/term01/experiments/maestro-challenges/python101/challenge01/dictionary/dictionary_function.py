### Maestro Challenge
### Course: Python101
### Date: Feb 13 - 2026

# Dictionary Function

def summarize_scores(scores, passing_score=70):
    '''
    Summarize student scores into passing and failing groups
    
    :param scores: dictionary maps students to their scores
    :param passing_score: a minimum score required to consider passing
    :return: Dictionary contains passing score, pass/fail counts, and students names.
    '''
    passed_students = []
    failed_students = []
    
    if not isinstance(scores, dict):
        raise TypeError("scores must be provied as dictionary")
    
    for name, value in scores.items():  
        if not isinstance(value, int):
            raise TypeError("score must be a number interger")
        
        if not isinstance(passing_score, int):
            raise TypeError("passing score must be interger")
        
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

report = summarize_scores(scores)
print("Summary Report")
print(report)