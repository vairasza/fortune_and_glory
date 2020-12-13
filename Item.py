import json
import data.Constants as Constants

class Item:

    item_table = []

    def __init__(self, id):
        if len(Item.item_table) == 0: Item.loadItems()

        self.__dict__.update(Item.item_table[id])
    
    @staticmethod
    def loadItems():
        Item.item_table = json.load(open(Constants.FN_ITEM_DATA))

    def getName(self):
        return self.name
    
    @staticmethod
    def getSizeItemList():
        return len(Item.item_table)