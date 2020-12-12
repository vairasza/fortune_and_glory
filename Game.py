from Quest import Quest
from Item import Item
from Meeple import Meeple

quest_1 = Quest(0)
#print(quest_1.text_decision)

item_1 = Item(0)
#print(item_1.getName())

player_1 = Meeple("Richard Löwenherz")  #get via input
player_1.addObjToInventory(Item(0))
player_1.addObjToInventory(Item(2))
print(player_1)