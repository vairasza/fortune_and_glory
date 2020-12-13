from Quest import Quest
from Item import Item
from Meeple import Meeple
import data.Constants as Constants
import random

quest_1 = Quest(0)
player_1 = Meeple("Richard Löwenherz")  #get via input
Item.loadItems()

def rollDices(number_of_dices):
    return sum([random.randint(1, Constants.DICE_SIDES) for i in range(number_of_dices)])

def executeQuest(quest, hero):
        #1. player is confronted with text where he must make a decision yes/no
        print(quest.text_decision)

        #2. get input from player
        player_decision = True

        while True:
            player_input = input(Constants.QUEST_INPUT_DECISION)

            if (player_input in ["ja", "j"]):
                player_decision = True
                break
            if (player_input in ["nein", "n"]):
                player_decision = False
                break
        
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
                print(Constants.QUEST_HERO_LIFEPOINTS_LEFT.replace("XX", current_lifepoints))
                #return Constants.GAME_CONTINUE #cant return here unless we are dead!

        #9b. player succeeded on the quest and get an item as reward
        #9b. check if play already has item/more than 5 and ask what item he wants remove
        else:
            print(Item.getSizeItemList())
            rnd_id = random.randint(0, Item.getSizeItemList() - 1)
            new_item = Item(rnd_id)

            print(Constants.QUEST_HERO_RECEIVED_ITEM.replace("XX", new_item.getName()).replace("YY", new_item.getStats()))

            if (hero.checkInventoryFull()):
                
                if (hero.checkItemInInventory(new_item)):
                    #inv full and item in inv => draw
                    print(Constants.QUEST_HERO_INV_FULL_1)
                    print(Constants.QUEST_HERO_ITEM_DROPPED)
                    #done
                else:
                    #inv full and item not in inv => replace question
                    print(Constants.QUEST_HERO_INV_FULL_2)

                    player_decision = True

                    while True:
                        player_input = input(Constants.QUEST_INPUT_DECISION)

                        if (player_input in ["ja", "j"]):
                            player_decision = True
                            break
                        if (player_input in ["nein", "n"]):
                            player_decision = False
                            break
                    
                    if player_decision:
                    #len_inv = hero.getInventoryCurrentSize()

                    print(" | ".join([f"{i + 1} - {val}" for i, val in range(len_inv )]))

                        while True:  
                            player_input = input(Constants.QUEST_INPUT_ITEMS.replace("XX", str([i + 1 for i in range(len_inv)])))

                            if player_input.isnumeric() and player_input > 0 and player_input < len_inv + 2:
                                del_item = hero.getItemById(int(player_input))

                                hero.addItemToInventory(new_item)
                                print(Constants.QUEST_HERO_ITEM_REPLACE.replace("XX", del_item.name).replace("YY", new_item.getName()))

                                break

            else:
                if (hero.checkItemInInventory(new_item)):
                    #inv not full and item in inv => draw
                    print(Constants.QUEST_HERO_ITEM_DOUBLE)

                    print(Constants.QUEST_HERO_ITEM_DROPPED)
                    #done
                else:
                    #inv notfull and item not in inv => add
                    hero.addItemToInventory(new_item)
                    print(Constants.QUEST_HERO_INV_ITEM_ADDED)
                    #done
            
            #updatestats

executeQuest(quest_1, player_1)