import dice

#add more classes for other jobs like warrior and mage

#dice created
d = dice.stat_dice()


#Character class
class Character():
    def __init__(self):
        #user input for name and job
        self.name = input("Please type a name: ")
        self.job = input("Please select a job class: ")

        #stats recieve a random number 8 - 20 and then put in a list and placed in the appropriate stat
        stats = d.stat_roll()
        stats.sort(reverse=True)

        self.Strength = stats[0] + 2
        self.Dexterity = stats[2] + 1
        self.Constitution = stats[1] + 2
        self.Wisdom = stats[3]
        self.Intelligence = stats[4]


    # #displays Character
    # def __str__(self):
    #     return "Character Name: %s\nJob: %s\n-----\nStats:\nStrength: %s\nDexterity: %s\nConstitution: %s\nWisdom: %s\nIntelligence: %s" % (
    #         self.name, self.job, self.Strength, self.Dexterity,
    #         self.Constitution, self.Wisdom, self.Intelligence)
def display_character(self):
    return"Character Name: %s\nJob: %s\n-----\nStats:\nStrength: %s\nDexterity: %s\nConstitution: %s\nWisdom: %s\nIntelligence: %s" %(self.name, self.job, self.Strength, self.Dexterity, self.Constitution,
        self.Wisdom, self.Intelligence)
