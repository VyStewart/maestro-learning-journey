### Maestro Challenge
### Topic: Object to Object Interaction
### Date: April 19 - 2026

"""
Simple adventure game simulation with a Player and multiple Quests.

- Each Quest object stores its own title.
- A single Player object stores a name and can start different quests.
- The Player interacts with each Quest by calling start_quest(quest),
  which reads quest.title and the player's own name.
- Demonstrates that each object keeps its own data while objects
  interact through method calls and attributes.
"""

class Player:
    """A class representing a player who can start quests."""
    def __init__(self, name):
        self.name = name

    def start_quest(self, quest):
        """Starts a quest by reading the quest's title and player's name."""
        print(f"{self.name} is starting the quest: {quest.title}.")

class Quest:
    def __init__(self, title):
        self.title = title

    def describe(self):
        print(f"{self.title} has three steps to follow.")

player = Player("Joshua")
quest1 = Quest("Dragon Slayer")
quest2 = Quest("Enchanted Forest")    

# Player starts quest1
player.start_quest(quest1)
quest1.describe()               

# Player starts quest2
print("---" * 20)                 # Add a newline for better separation 
player.start_quest(quest2)
quest2.describe()
