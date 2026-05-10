### Course: Python 103 - Object-Oriented Programming
### Week 09: From Simple Objects to Flexible Systems
### Lesson 01: Encapsulation - protecting objects' state
### Date: May 10 - 2026

'''In this lesson, we will learn about encapsulation,
which is the concept of owning an object's state and controlling access to it.'''

# Let's create a Thermometer class to represent a thermometer with a temperature attribute
class Thermometer:
    def __init__(self, temperature):
        self._temperature = temperature

    def set_temperature(self, new_temp):
        """
        Ensure temperature stays between 0 and 150
        """
        if new_temp < 0:
            self._temperature = 0
        elif new_temp > 150:
            self._temperature = 150
        else:
            self._temperature = new_temp

        return self._temperature

#----- Main program --------
thermo = Thermometer(25)
print(thermo.set_temperature(-20))  # Should print 0
print(thermo.set_temperature(30))    # Should print 30
print(thermo.set_temperature(200))   # Should print 150
