import json
import data.Constants as Constants

class Item:

    item_table = []

    def __init__(self, id):
        #if len(Item.item_table) == 0: Item.loadItems()

        self.__dict__.update(Item.item_table[id])

    def __str__(self):
        name = self.name
        stats = ', '.join([f'{key}: +{val}' for key, val in self.properties.items()])

        return name + stats
    
    def getName(self):
        return self.name
    
    def getStats(self):
        return ', '.join([f'{key}: +{val}' for key, val in self.properties.items()])
    
    @staticmethod
    def loadItems():
        Item.item_table = json.load(open(Constants.FN_ITEM_DATA))
    
    @staticmethod
    def getSizeItemList():
        return len(Item.item_table)