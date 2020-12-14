import random
import data.Constants as Constants

class Meeple:

    PROGRESS = 0

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
        return Constants.HERO_BASIC_STAT + random.randint( - Constants.HERO_BASIC_STAT_SPREAD, Constants.HERO_BASIC_STAT_SPREAD )

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
            "lifepoints": self.lifepoints,
            "strength": self.strength,
            "intellect": self.intellect,
            "speed": self.speed,
            "charisma": self.charisma
        }
    
    def loseLifepoints(self, number = 1):
        self.lifepoints -= number
        return self.lifepoints

    #skip moves
    def setSkipMoveTrue(self):
        self.skipMove = True

    def setSkipMoveFalse(self):
        self.skipMove = False

    #inventory
    def addItemToInventory(self, item):
        self.inventory.append(item)
        return self.inventory
        
    def checkItemInInventory(self, item):
        return item in self.inventory
        
    def getInventoryList(self):
        return self.inventory

    def removeItemById(self, id):
        del_item = self.inventory[id]
        self.inventory.remove(del_item)
        return del_item
    
    def removeItem(self, item):
        self.inventory.remove(item)
    
    def checkInventoryFull(self):
        return len(self.inventory) >= Constants.HERO_INV_MAX_SIZE

    #remove item and insert other item
    @staticmethod
    def increaseProgress(step, direction = True):
        if direction:
            Meeple.PROGRESS += step
        else:
            Meeple.PROGRESS -= step
        
        return Meeple.PROGRESS

    @staticmethod
    def getProgress():
        return Meeple.PROGRESS