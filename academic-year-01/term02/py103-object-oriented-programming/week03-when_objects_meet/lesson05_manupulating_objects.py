### Course: Python 103 - Object-Oriented Programming
### Week 09: When Objects Meet
### Lesson 05: manipulating Objects in programs
### Date: May 06 - 2026

'''In this lesson, we will learn how to manipulate objects in our programs
by calling their methods and changing their attributes.'''

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 10

    def feed(self):
        self.hunger -= 2

pets = [
    Pet("Luna"),
    Pet("Milo"),
    Pet("Lucky")
]

'''Let's feed all the pets and check their hunger levels.'''
for pet in pets:
    pet.feed()
    
'''Now let's print the name and hunger level of each pet.'''
for pet in pets:
    print(pet.name, pet.hunger)

'''Let's calculate the total and average hunger levels.'''
total_hunger = 0
for pet in pets:
    total_hunger += pet.hunger
    
'''Average hunger:'''
average_hunger = total_hunger / len(pets)
print("Average hunger:", average_hunger)

# another example of manipulating objects:
class Robot:
    def __init__(self, name, battery_level):
        self.name = name
        self.battery_level = battery_level

    def charge(self):
        self.battery_level += 10

robots = [
    Robot("Theo", 80),
    Robot("Marcus", 60),
    Robot("Damien", 70)
]

'''Let's charge all the robots and check their battery levels.'''
for robot in robots:
    robot.charge()
    print(robot.name, robot.battery_level)

'''Let's calculate the total and average battery levels.'''
total_battery_level = 0
for robot in robots:
    total_battery_level += robot.battery_level
    
'''Average battery level:'''
average_battery_level = total_battery_level // len(robots)
print("Average battery level", average_battery_level)