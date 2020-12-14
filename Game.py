from Quest import Quest
from Item import Item
from Meeple import Meeple
import data.Constants as Constants
import random

#print(Constants.GAME_WELCOME)
#input number of player
#ask all players individually for their name and character typ

quest_1 = Quest(0)
player_1 = Meeple("Richard Löwenherz")  #get via input
Item.loadItems()
#player_1.addItemToInventory(Item(0))
#player_1.addItemToInventory(Item(0))
#player_1.addItemToInventory(Item(0))
#player_1.addItemToInventory(Item(0))
#player_1.addItemToInventory(Item(0))

def getInput(allowedInput):
    altText = "/".join([str(key["input"]) for key in allowedInput])

    player_decision = None

    while True:
        player_input = input(Constants.QUEST_INPUT_DECISION.replace("XX", altText))

        for key in allowedInput:
            if player_input == key["input"]:
                player_decision = key["output"]
                return player_decision

def rollDices(number_of_dices):
    return sum([random.randint(1, Constants.DICE_SIDES) for i in range(number_of_dices)])

def executeQuest(quest, hero):
        #1. player is confronted with text where he must make a decision yes/no
        print(quest.text_decision)

        #2. get input from player
        expectedInput = [ {"input": "ja","output": True} , {"input": "nein","output": False} ]
        player_decision = getInput(expectedInput)
        
        #3. displays text depening on the players input
        print(quest.text_confirm if player_decision else quest.text_deny)

        #4. determines category based on the users input
        determined_category = quest.quest_yes_category if player_decision else quest.quest_no_category

        #5. determines the price the player has to overcome with rolling dices
        challenge = quest.quest_yes_price if player_decision else quest.quest_no_price

        #6. look up how many dices the player can roll
        number_of_dices = getattr(hero, determined_category)
        rolling_result = rollDices(number_of_dices)
        
        #7. present rolling result to player
        print(Constants.QUEST_ROLLING_RESULT.replace("XX", str(challenge)).replace("YY", str(rolling_result)))

        #8. decision for this round
        round_result = challenge - rolling_result
        print(Constants.QUEST_SUCCESS if round_result < 0 else Constants.QUEST_FAIL)

        #9a. player failed quest and loses 1 lifepoint
        #10a. check if player has more than 0 lifepoints else -> lost game
        if (round_result >= 0):
            current_lifepoints = hero.loseLifepoints()

            if (current_lifepoints <= 0):
                print(Constants.QUEST_HERO_LIFEPOINTS_ZERO)
                return Constants.GAME_LOST
            else:
                print(Constants.QUEST_HERO_LIFEPOINTS_LEFT.replace("XX", str(current_lifepoints)))
                #return Constants.GAME_CONTINUE #cant return here unless we are dead!

        #9b. player succeeded on the quest and get an item as reward
        #9b. check if play already has item/more than 5 and ask what item he wants remove
        else:
            rnd_id = random.randint(0, Item.getSizeItemList() - 1)
            new_item = Item(rnd_id)

            print(Constants.QUEST_HERO_RECEIVED_ITEM.replace("XX", new_item.getName()).replace("YY", new_item.getStats()))

            if (hero.checkInventoryFull()):
                
                if (hero.checkItemInInventory(new_item)):
                    #inv full and item in inv => draw
                    print(Constants.QUEST_HERO_INV_FULL_1)
                    print(Constants.QUEST_HERO_ITEM_DROPPED)
                else:
                    #inv full and item not in inv => replace question
                    print(Constants.QUEST_HERO_INV_FULL_2)

                    expectedInput = [ {"input": "ja","output": True} , {"input": "nein","output": False} ]
                    player_decision = getInput(expectedInput)
                    
                    if player_decision:
                        #player wants to keep the item => select item to trash

                        #print items with number
                        print(", ".join([f"{i + 1} - {j.getName()}" for i, j in enumerate(player_1.getInventoryList())]))
                        
                        expectedInput = [{"input": str(i), "output": i} for i in range(1, Constants.HERO_INV_MAX_SIZE + 1)]

                        player_decision = getInput(expectedInput)

                        del_item = hero.removeItemById(player_decision - 1)
                        hero.addItemToInventory(new_item)

                        print(Constants.QUEST_HERO_ITEM_REPLACE.replace("XX", del_item.getName()).replace("YY", new_item.getName()))

                    else:
                        #player wants to trash the item
                        print(Constants.QUEST_HERO_ITEM_DROPPED.replace("XX", new_item.getName()))

            else:
                if (hero.checkItemInInventory(new_item)):
                    #inv not full and item in inv => draw
                    print(Constants.QUEST_HERO_ITEM_DOUBLE)

                    print(Constants.QUEST_HERO_ITEM_DROPPED.replace("XX", new_item.getName()))
                else:
                    #inv notfull and item not in inv => add
                    hero.addItemToInventory(new_item)
                    print(Constants.QUEST_HERO_INV_ITEM_ADDED.replace("XX", new_item.getName()))

executeQuest(quest_1, player_1)
#updatestats
#nextround/player