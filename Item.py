import json
import data.Constants as Constants
import random

class Item:

    item_table = []

    def __init__(self, item_obj):
        self.item_id = item_obj["item_id"]
        self.rarity = item_obj["rarity"]
        self.name = item_obj["name"]
        self.properties = item_obj["properties"]

    def __str__(self):
        name = self.name
        stats = ', '.join([f'{key}: +{val}' for key, val in self.properties.items()])

        return name + " " +stats
    
    def __lt__(self, other):
        return self.rarity < other.rarity
    
    def getStats(self):
        return ', '.join([f'{key}: +{val}' for key, val in self.properties.items()])
    
    @staticmethod
    def loadItems():
        i_table = json.load(open(Constants.FN_ITEM_DATA))

        Item.item_table = [Item(i) for i in i_table]
        
        #sort by rarity so we get the bad items first
        Item.item_table.sort()
        Item.length = len(Item.item_table)
    
    @staticmethod
    def rewardItem():
        return random.choice(Item.item_table)