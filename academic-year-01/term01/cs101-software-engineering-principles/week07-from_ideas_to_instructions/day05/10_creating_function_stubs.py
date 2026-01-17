### CS101:  Software Engineering Principles
### Week07: From ideas to instruction
## Lesson 10: Creating function stubs for structure
### Date: Jan 17 - 2026

# Example using function with return-based stub
def convert_minutes_to_hours(study):
    """
    Convert study time from minutes to hours

    Minutes: Time to study in minutes
    Returns the same time conveverted to hours 
    """
    return 0.0

time = convert_minutes_to_hours(75)
print(time)

# Example using function with pass-based stub
def summarize_daily_study(total_minutes):
    """
    Summarize the daiy study time
    """
    pass

daily_study = summarize_daily_study(90)
print(daily_study)

# Stub tripple-check: define-->call-->trace with print
def plan_breaks_for_study(total_minutes):
    """
    Plan for taking break during study session
    """
    return 0

session_length = 90
breaks = plan_breaks_for_study(session_length)
print(session_length)
print(breaks)

