from Quest import Quest
from Item import Item
from Meeple import Meeple
import data.Constants as Constants
import random

quest_1 = Quest(0)
#print(quest_1.text_decision)

item_1 = Item(0)
#print(item_1.getName())

player_1 = Meeple("Richard Löwenherz")  #get via input
player_1.addItemToInventory(Item(0))
player_1.addItemToInventory(Item(2))

print(player_1.intellect)
print(getattr(player_1, "intellect"))

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
        rolling_result = Meeple.rollDices(number_of_dices)
        
        #7. present rolling result to player
        print(Constants.QUEST_ROLLING_RESULT.replace("XX", challenge).replace("YY", rolling_result))

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
            rnd_id = random.randint(1, Item.getSizeItemList() - 1)
            new_item = Item(rnd_id)
            feedback = hero.addItemToInventory(new_item)
            print(Constants.QUEST_HERO_RECEIVED_ITEM.replace("XX", Item.getName()))

            #return None if list is >= max_size, return item is double, return list if item was added

            if (feedback is None):
                print(Constants.QUEST_HERO_INV_FULL)
                player_decision = True

                while True:
                    player_input = input(Constants.QUEST_INPUT_DECISION)

                    if (player_input in ["ja", "j"]):
                        player_decision = True
                        break
                    if (player_input in ["nein", "n"]):
                        player_decision = False
                        break
                
                #1 - decide for new item
                if player_decision:
                    player_decision = 0
                    len_inv = len(hero.inventory)

                    print(" | ".join([f"{i + 1} - {val}" for i, val in range(len_inv )]))

                    while True:  
                        player_input = input(Constants.QUEST_INPUT_ITEMS.replace("XX", str([i for i in range(1,len_inv + 1)])))

                        if player_input.isnumeric() and player_input > 0 and player_input < len_inv + 2:

                            break

                        #if player has decided to remove a item and wants the new item => also check if item is double
                        

                #2 - draw
                else:
                    print(Constants.QUEST_HERO_ITEM_DROPPED)
            
            elif (feedback):
                print(Constants.QUEST_HERO_ITEM_DOUBLE)
            else:
                #already added before
                print(Constants.QUEST_HERO_INV_ITEM_ADDED)

            
            #generate new random item
            #YX = item to string
            #message that player was rewarded with XY
            #check if inventory of player is full
            #check if player has item
            #if full   => ask to replace if yes: replace no: draw => endround
            #else endround

            #UPDATE STATS