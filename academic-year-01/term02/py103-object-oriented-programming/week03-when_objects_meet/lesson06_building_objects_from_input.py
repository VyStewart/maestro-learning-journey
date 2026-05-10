### Course: Python 103 - Object-Oriented Programming
### Week 09: When Objects Meet
### Lesson 06: Building Objects from Input
### Date: May 09 - 2026

'''In this lesson, we will learn how to build objects from user input.'''

# Let's create a simple Workout class to represent a workout session.
class Workout:
    def __init__(self, name, reps, category):
        '''Initialize the workout with a name and number of reps/seconds.'''
        self.name = name
        self.reps = reps
        self.category = category

# Collections for workout (empty list)
workouts = []

# == Input loop ==
while True:
    name = input("Enter workout name (or 'done' to finish): ")
    if name == "done":
        break

    reps_text = input("Enter number of the reps/seconds: ")
    reps = int(reps_text)
    
    category = input("Enter workout category: ")

    new_workout = Workout(name, reps, category)
    workouts.append(new_workout)

# == Sumary output ==
print("You did", len(workouts), "workouts today:")
counter = 1
for w in workouts:
    print(counter, ".", w.name, "-", w.reps, "-", "(",w.category,")")
    counter += 1
