import random

class Spielfigur:

    '''
    name: argument
    stats: lifepoints, strength, int, speed, charisma: value is randomly selecte btw 2-6
    backpack: -> list of objects (limit - N=5)
    bool: skip moves
    static progress: successful moves players have made
    '''

    progress = 0
    basic_stat = 4
    spread = 2
    inventory_max_size = 5

    def __init__(self, name):
        self.name = name
        self.lifepoints = Spielfigur.basic_stat + random.randint( - Spielfigur.spread, Spielfigur.spread )
        self.strength = Spielfigur.basic_stat + random.randint( - Spielfigur.spread, Spielfigur.spread )
        self.intellect = Spielfigur.basic_stat + random.randint( - Spielfigur.spread, Spielfigur.spread )
        self.speed = Spielfigur.basic_stat + random.randint( - Spielfigur.spread, Spielfigur.spread )
        self.charisma = Spielfigur.basic_stat + random.randint( - Spielfigur.spread, Spielfigur.spread )
        self.inventory = []
        self.skipMove = False

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
        if len(self.inventory) == Spielfigur.inventory_max_size:
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

    def increaseProgress(step, direction = True):
        if direction:
            Spielfigur.progress += step
        else:
            Spielfigur.progress -= step
        
        return Spielfigur.progress
    
    def getProgress():
        return Spielfigur.progress