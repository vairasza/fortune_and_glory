from Quest import Quest
from Item import Item
from Meeple import Meeple
import data.Constants as Constants
import random
#import pygame

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
        if (round_result >= 0):
            current_lifepoints = hero.loseLifepoints()

            #10a. player has  0 lifepoints -> lost game
            if (current_lifepoints <= 0):
                print(Constants.QUEST_HERO_LIFEPOINTS_ZERO)
                
                return Constants.GAME_LOST

            #10b. player loses 1 lifepoint
            else:
                print(Constants.QUEST_HERO_LIFEPOINTS_LEFT.replace("XX", str(current_lifepoints)))
                
                return Constants.GAME_CONTINUE

        #9b. player succeeded on the quest and get an item as reward
        #9b. check if play already has item/more than 5 and ask what item he wants remove
        else:
            rnd_id = random.randint(0, Item.getSizeItemList() - 1)
            new_item = Item(rnd_id)

            print(Constants.QUEST_HERO_RECEIVED_ITEM.replace("XX", new_item.getName()).replace("YY", new_item.getStats()))

            #11a invenotry is full
            if (hero.checkInventoryFull()):
                
                #11aa invenotry is full and item is in the inventory
                if (hero.checkItemInInventory(new_item)):

                    print(Constants.QUEST_HERO_INV_FULL_1)
                    print(Constants.QUEST_HERO_ITEM_DROPPED)
                    
                    return Constants.GAME_CONTINUE

                #11ab invenotry is full and item can be replaced
                else:
                    print(Constants.QUEST_HERO_INV_FULL_2)

                    expectedInput = [ {"input": "ja","output": True} , {"input": "nein","output": False} ]
                    player_decision = getInput(expectedInput)
                    
                    #11aba invenotry is full and item can be replaced; player wants to keep the item => select item to trash
                    if player_decision:
                        #prints all items with a corresponding number
                        print(", ".join([f"{i + 1} - {j.getName()}" for i, j in enumerate(player_1.getInventoryList())]))
                        
                        expectedInput = [{"input": str(i), "output": i} for i in range(1, Constants.HERO_INV_MAX_SIZE + 1)]

                        player_decision = getInput(expectedInput)

                        del_item = hero.removeItemById(player_decision - 1)
                        hero.addItemToInventory(new_item)

                        print(Constants.QUEST_HERO_ITEM_REPLACE.replace("XX", del_item.getName()).replace("YY", new_item.getName()))
                        
                        return Constants.GAME_CONTINUE

                    #11aba invenotry is full and item can be replaced; player wants to trash the item
                    else:
                        print(Constants.QUEST_HERO_ITEM_DROPPED.replace("XX", new_item.getName()))
                        
                        return Constants.GAME_CONTINUE

            #11b invenotry is not full and item in inv => draw
            else:
                #11ba invenotry is not full and item in inv => draw
                if (hero.checkItemInInventory(new_item)):
                    print(Constants.QUEST_HERO_ITEM_DOUBLE)

                    print(Constants.QUEST_HERO_ITEM_DROPPED.replace("XX", new_item.getName()))
                    
                    return Constants.GAME_CONTINUE

                #11bb invenotry is not full and item not in inv => added
                else:
                    hero.addItemToInventory(new_item)
                    
                    print(Constants.QUEST_HERO_INV_ITEM_ADDED.replace("XX", new_item.getName()))
                    
                    return Constants.GAME_CONTINUE

#Game Starts Here
Item.loadItems()

print(Constants.GAME_WELCOME)
#input number of player
expectedInput = [{"input": str(i), "output": i} for i in range(Constants.MIN_PLAYERS, Constants.MAX_PLAYERS + 1)]
player_number = getInput(expectedInput)

#ask all players individually for their name and character typ
for i in range(player_number):
    print(f"player {i + 1}: please make some customisations")
    print("tell us your heros name")
    #hero name
    hero_name = input(Constants.QUEST_INPUT_DECISION.replace("[XX]", ""))
    #hero type
    print("knight, wizard, archer --> state benefites")
    expectedInput = [{"input": "1", "output": "knight"}, {"input": "2", "output": "wizard"}, {"input": "3", "output": "archer"}]
    hero_type = getInput(expectedInput)

    Meeple.addNewPlayer(hero_name, hero_type)


#loop rounds
while True:
    print(f"Runde {Meeple.rounds} beginnt:")

    while True:
        #loop players
        rnd_quest = Quest.getQuest() # => 4 players * 5 fields => 20 quests
        next_player = Meeple.nextPlayer()

        result = executeQuest(rnd_quest, next_player)

        if result:
            #update stats => update in executeQuest
            print(1)
        else:
            print("you lost the game and cant play anymore")

            #remove from players
            #if len(players) == 0 => end game for all show results


        Meeple.rounds +=1

    #check if players dead or wincondition
    if len(Meeple.players) == 0:
        return Constants.GAME_LOST_FOR_ALL
    #reset players played round

