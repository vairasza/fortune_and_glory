import random
import data.Constants as Constants

class Meeple:

    rounds = 1
    players = []

    #herotype: 0->knight, 1->wizard, 2->archer ==> different stat boni
    def __init__(self, name, hero_type="knight"):
        self.name = name
        self.hero_type = hero_type
        self.lifepoints = Meeple.getRandomStat()
        self.strength = Meeple.getRandomStat()
        self.intellect = Meeple.getRandomStat()
        self.speed = Meeple.getRandomStat()
        self.charisma = Meeple.getRandomStat()
        self.inventory = []
        self.skipMove = False
        self.progress = 0
        self.roundPlayed = False

    @staticmethod
    def addNewPlayer(name, hero_type):
        Meeple.players.append(Meeple(name, hero_type))

    @staticmethod
    def nextPlayer():
        for i in Meeple.players:
            if not i.roundPlayed:
                return i
    
    @staticmethod
    def removePlayer(player):
        Meeple.players.remove(player)
    
    @staticmethod
    def resetRoundPlayed():
        for player in Meeple.players:
            player.roundPlayed = False

    @staticmethod
    def getRandomStat():
        return Constants.HERO_BASIC_STAT + random.randint( - Constants.HERO_BASIC_STAT_SPREAD, Constants.HERO_BASIC_STAT_SPREAD )

    def __str__(self):
        item_string = ''.join([f"* {item.name} ({', '.join([f'{key}: +{val}' for key, val in item.properties.items()])})\n" for item in self.inventory])

        return f"Name: {self.name}\n"\
            f"Schritte zum Erfolg: {self.progress}\n"\
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
    def setSkipMove(self, rounds):
        self.skipMove = rounds

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

    def setRoundPlayed(self):
        self.roundPlayed = True

    def updateStats(self):
        print(1)

    def checkSkipMove(self):
        print(1)

    def freeSkipMoves(self):
        print(1)

    #move to inherited archer class
    def archer_talent_roll(self):
        #check herotype
        return random.randint(1, Constants.DICE_SIDES) >= 4

    def wizard_talent_roll(self):
        #check herotype
        return random.randint(1, Constants.DICE_SIDES) >= 5
    
    def knight_talent_roll(self):
        #check herotype
        return random.randint(1, Constants.DICE_SIDES) >= 4