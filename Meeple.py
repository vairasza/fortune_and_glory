import random
import data.Constants as Constants

class Meeple:

    rounds = 1
    players = []

    #herotype: 0->knight, 1->wizard, 2->archer ==> different stat boni
    def __init__(self, name, hero_type):
        self.name = name
        self.hero_type = hero_type
        self.lifepoints = Meeple.getRandomStat() + self.getHeroStats("lifepoints")
        self.strength = Meeple.getRandomStat() + self.getHeroStats("strength")
        self.intellect = Meeple.getRandomStat() + self.getHeroStats("intellect")
        self.agility = Meeple.getRandomStat() + self.getHeroStats("agility")
        self.speed = Meeple.getRandomStat() + self.getHeroStats("speed")
        self.charisma = Meeple.getRandomStat() + self.getHeroStats("charisma")
        self.inventory = []
        self.skipMove = False
        self.progress = 0
        self.roundPlayed = False

    def getHeroStats(self, stat):
        if self.hero_type == Constants.HERO_TYPE_KNIGHT:
            return Constants.KNIGHT_STATS[stat]
        elif self.hero_type == Constants.HERO_TYPE_WIZARD:
            return Constants.WIZARD_STATS[stat]
        else:
            return Constants.ARCHER_STATS[stat]
    
    def getHeroType(self):
        if self.hero_type == Constants.HERO_TYPE_ARCHER:
            return Constants.HERO_TYPE_ARCHER_LOC
        elif self.hero_type == Constants.HERO_TYPE_WIZARD:
            return Constants.HERO_TYPE_WIZARD_LOC
        else:
            return Constants.HERO_TYPE_KNIGHT_LOC

    def __str__(self):
        item_string = ''.join([f"* {item.name} ({', '.join([f'{key}: +{val}' for key, val in item.properties.items()])})\n" for item in self.inventory])

        return f"Name: {self.name}\n"\
            f"Heldentyp: {self.getHeroType()}\n"\
            f"Schritte zum Erfolg: {self.progress}\n"\
            f"Lebenspunkte: {self.lifepoints}\n"\
            f"Stärkepunkte: {self.strength}\n"\
            f"Intelligenz: {self.agility}\n"\
            f"Geschicklichkeit: {self.intellect}\n"\
            f"Geschwindigkeit: {self.speed}\n"\
            f"Charisma: {self.charisma}\n"\
            f"Im Rucksack:\n"\
            f"{item_string}"
    
    def loseLifepoints(self, number = 1):
        self.lifepoints -= number
        return self.lifepoints

    #skip moves
    def setSkipMove(self, rounds):
        self.skipMove = rounds

    #inventory
    def addItemToInventory(self, item):
        self.inventory.append(item)
        self.updateStats(item.properties, True)
        return self.inventory
        
    def checkItemInInventory(self, item):
        return item in self.inventory
        
    def getInventoryList(self):
        return self.inventory

    def removeItemById(self, id):
        del_item = self.inventory[id]
        self.inventory.remove(del_item)
        self.updateStats(del_item.properties, False)
        return del_item
    
    def removeItem(self, item):
        self.inventory.remove(item)
        self.updateStats(item.properties, False)
    
    def checkInventoryFull(self):
        return len(self.inventory) >= Constants.HERO_INV_MAX_SIZE

    def setRoundPlayed(self):
        self.roundPlayed = True

    def updateStats(self, item, bool=True):
        if bool:
            self.lifepoints += item["lifepoints"]
            self.strength += item["strength"]
            self.intellect += item["intellect"]
            self.agility += item["agility"]
            self.speed += item["speed"]
            self.charisma += item["charisma"]
        else:
            self.lifepoints -= item["lifepoints"]
            self.strength -= item["strength"]
            self.intellect -= item["intellect"]
            self.agility -= item["agility"]
            self.speed -= item["speed"]
            self.charisma -= item["charisma"]

    def checkSkipMove(self):
        return not self.skipMove

    def freeSkipMoves(self):
        self.skipMove = False

    #move to inherited archer class
    def archer_talent_roll(self):
        if self.hero_type == Constants.HERO_TYPE_ARCHER:
            print(Constants.ARCHER_TALENT_USE)

            if random.randint(1, Constants.DICE_SIDES) >= Constants.ARCHER_TALENT_REQ:
                print(Constants.ARCHER_TALENT_PROC)
                return True

        return False

    def wizard_talent_roll(self):
        if self.hero_type == Constants.HERO_TYPE_WIZARD:
            print(Constants.WIZARD_TALENT_USE)

            if random.randint(1, Constants.DICE_SIDES) >= Constants.WIZARD_TALENT_REQ:
                print(Constants.WIZARD_TALENT_PROC)
                return True

        return False
    
    def knight_talent_roll(self):
        if self.hero_type == Constants.HERO_TYPE_KNIGHT:
            print(Constants.KNIGHT_TALENT_USE)

            if random.randint(1, Constants.DICE_SIDES) >= Constants.KNIGHT_TALENT_REQ:
                print(Constants.KNIGHT_TALENT_PROC)
                return True

        return False

    def playerWinsGame(self):
        print(1)
    
    @staticmethod
    def addNewPlayer(name, hero_type):
        Meeple.players.append(Meeple(name, hero_type))

    @staticmethod
    def nextPlayer():
        for i in Meeple.players:
            if not i.roundPlayed:
                return i
        return None
    
    @staticmethod
    def removePlayer(player):
        Meeple.players.remove(player)
    
    @staticmethod
    def resetRoundPlayed():
        Meeple.rounds +=1
        for player in Meeple.players:
            player.roundPlayed = False

    @staticmethod
    def getRandomStat():
        return Constants.HERO_BASIC_STAT + random.randint( - Constants.HERO_BASIC_STAT_SPREAD, Constants.HERO_BASIC_STAT_SPREAD )