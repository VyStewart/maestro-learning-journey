### Course: Python 103 - Object-Oriented Programming
### Week 09: When Objects Meet
### Lesson 06: Building Objects from Input
### Date: May 10 - 2026

'''In this lesson, we will learn how to build objects from user input.'''
class Thermometer:
    '''A simple thermometer class that represents a thermometer 
    with a temperature attribute.'''
    def __init__(self, temperature):
        # Let's add some input validation to ensure the temperature is within a reasonable range.
        assert isinstance(temperature, (int, float)), "Temperature must be an int or float"
        
        self.temperature = temperature
        
        # Let's clamp the temperature to a reasonable range (e.g., -50 to 150 degrees Celsius).
        if self.temperature < -50:
            self.temperature = -50
        
        if self.temperature > 150:
            self.temperature = 150
            
# Let's test our Thermometer class with some extreme values.
t1 = Thermometer(-999)
t2 = Thermometer(20)
t3 = Thermometer(999)

print(t1.temperature)
print(t2.temperature)
print(t3.temperature)