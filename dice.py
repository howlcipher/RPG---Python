import random


class stat_dice:
    #function that call's itself when created
    # object    attributes
    def __init__(self):
        self.sides = int
        self.min = int
    #creates 5 dice rolls and places them into a list
    def stat_roll(self):
        stats = []
        x = range(8, 18)
        i = 0
        while i < 5:
            z = random.choice(x)
            stats.append(z)
            i += 1
        return stats


class dice:
    #function that call's itself when created
    # object    attributes
    def __init__(self, sides):
        self.sides = sides
    
    def roll(self):
        x = range(self.sides)
        z = random.choice(x)
        return z
