import random

class Meeple:

    '''
    name: argument
    stats: lifepoints, strength, int, speed, charisma: value is randomly selecte btw 2-6
    backpack: -> list of objects (limit - N=5)
    bool: skip moves
    static PROGRESS: successful moves players have made
    '''

    PROGRESS = 0
    BASIC_STAT = 4
    BASIC_STAT_SPREAD = 2
    INV_MAX_SIZE = 5

    #herotype: 0->knight, 1->wizard, 2->archer ==> different stat boni
    def __init__(self, name, hero_type=0):
        self.name = name
        self.lifepoints = Meeple.getRandomStat()
        self.strength = Meeple.getRandomStat()
        self.intellect = Meeple.getRandomStat()
        self.speed = Meeple.getRandomStat()
        self.charisma = Meeple.getRandomStat()
        self.inventory = []
        self.skipMove = False

    @staticmethod
    def getRandomStat():
        return Meeple.BASIC_STAT + random.randint( - Meeple.BASIC_STAT_SPREAD, Meeple.BASIC_STAT_SPREAD )

    def __str__(self):
        item_string = ''.join([f"* {item.name} ({', '.join([f'{key}: +{val}' for key, val in item.properties.items()])})\n" for item in self.inventory])

        return f"Name: {self.name}\n"\
            f"Schritte zum Erfolg: {Meeple.PROGRESS}\n"\
            f"Lebenspunkte: {self.lifepoints}\n"\
            f"Stärkepunkte: {self.strength}\n"\
            f"Intelligenz: {self.intellect}\n"\
            f"Geschwindigkeit: {self.speed}\n"\
            f"Charisma: {self.charisma}\n"\
            f"Im Rucksack:\n"\
            f"{item_string}"

    def getName(self):
        return self.name

    def getStats(self):
        return {
            "strength": self.strength,
            "intellect": self.intellect,
            "speed": self.speed,
            "charisma": self.charisma
        }

    def setSkipMoveTrue(self):
        self.skipMove = True

    def setSkipMoveFalse(self):
        self.skipMove = False

    def addObjToInventory(self, item):
        if len(self.inventory) == Meeple.INV_MAX_SIZE:
            return None
        else:
            self.inventory.append(item)
            return self.inventory
        
    def getFromInventory(self, item = None):
        if (item is not None):
            i = self.inventory.index(item)
            return self.inventory[i]
        else:
            return self.inventory

    #remove item and insert other item

    def increasePROGRESS(step, direction = True):
        if direction:
            Meeple.PROGRESS += step
        else:
            Meeple.PROGRESS -= step
        
        return Meeple.PROGRESS
    
    def getPROGRESS():
        return Meeple.PROGRESS