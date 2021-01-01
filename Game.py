from Quest import Quest
from Item import Item
from Meeple import Meeple
import data.Constants as Constants
import random

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
                
            current_lifepoints = hero.lifepoints if hero.knight_talent_roll() else hero.loseLifepoints()

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
            new_item = Item.rewardItem()

            print(Constants.QUEST_HERO_RECEIVED_ITEM.replace("XX", new_item.name).replace("YY", new_item.getStats()))

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
                        print(", ".join([f"{i + 1} - {j.name}" for i, j in enumerate(hero.getInventoryList())]))
                        
                        expectedInput = [{"input": str(i), "output": i} for i in range(1, Constants.HERO_INV_MAX_SIZE + 1)]

                        player_decision = getInput(expectedInput)

                        del_item = hero.removeItemById(player_decision - 1)
                        hero.addItemToInventory(new_item)

                        print(Constants.QUEST_HERO_ITEM_REPLACE.replace("XX", del_item.name).replace("YY", new_item.name))
                        
                        return Constants.GAME_CONTINUE

                    #11aba invenotry is full and item can be replaced; player wants to trash the item
                    else:
                        print(Constants.QUEST_HERO_ITEM_DROPPED.replace("XX", new_item.name))
                        
                        return Constants.GAME_CONTINUE

            #11b invenotry is not full and item in inv => draw
            else:
                #11ba invenotry is not full and item in inv => draw
                if (hero.checkItemInInventory(new_item)):
                    print(Constants.QUEST_HERO_ITEM_DOUBLE)

                    print(Constants.QUEST_HERO_ITEM_DROPPED.replace("XX", new_item.name))
                    
                    return Constants.GAME_CONTINUE

                #11bb invenotry is not full and item not in inv => added
                else:
                    hero.addItemToInventory(new_item)
                    
                    print(Constants.QUEST_HERO_INV_ITEM_ADDED.replace("XX", new_item.name))
                    
                    return Constants.GAME_CONTINUE

def executeLastQuest(quest, hero):
    #1. player is confronted with text where he must make a decision yes/no
    print(quest.text_decision)

    highest_stat = max(hero.intellect, hero.strength, hero.agility)

    #2. look up how many dices the player can roll
    number_of_dices = getattr(hero, highest_stat)
    rolling_result = rollDices(number_of_dices)
    
    #3. present rolling result to player
    print(Constants.QUEST_ROLLING_RESULT.replace("XX", str(highest_stat)).replace("YY", str(rolling_result)))

    #4. decision for this round
    round_result = highest_stat - rolling_result
    print(Constants.QUEST_SUCCESS if round_result < 0 else Constants.QUEST_FAIL)

    #5a. player failed quest and loses 1 lifepoint
    if (round_result >= 0):
            
        current_lifepoints = hero.lifepoints if hero.knight_talent_roll() else hero.loseLifepoints()

        #6a. player has  0 lifepoints -> lost game
        if (current_lifepoints <= 0):
            print(Constants.QUEST_HERO_LIFEPOINTS_ZERO)
            
            return Constants.GAME_LOST

        #6b. player loses 1 lifepoint
        else:
            print(Constants.QUEST_HERO_LIFEPOINTS_LEFT.replace("XX", str(current_lifepoints)))
            
            return Constants.GAME_CONTINUE

def initRequirements():
    Item.loadItems()
    Quest.loadQuests()

def initPlayers():
    print(Constants.GAME_WELCOME)
    expectedInput = [{"input": str(i), "output": i} for i in range(Constants.MIN_PLAYERS, Constants.MAX_PLAYERS + 1)]
    player_number = getInput(expectedInput)

    #ask all players individually for their name and character typ
    for i in range(player_number):
        print(Constants.GAME_CHOOSE_NUM_PLAYERS.replace("XX", str(i + 1)))
        print(Constants.GAME_HERO_NAME_CHOOSE)
        #hero name
        hero_name = input(Constants.QUEST_INPUT_DECISION.replace("XX", "name"))
        #hero type
        print(Constants.GAME_HERO_TYPE_CHOOSE)
        print(Constants.GAME_HERO_TYPE_CHOOSE_K + Constants.GAME_HERO_TYPE_CHOOSE_W + Constants.GAME_HERO_TYPE_CHOOSE_A)
        expectedInput = [
            {"input": "1", "output": Constants.HERO_TYPE_KNIGHT},
            {"input": "2", "output": Constants.HERO_TYPE_WIZARD},
            {"input": "3", "output": Constants.HERO_TYPE_ARCHER}
        ]
        hero_type = getInput(expectedInput)

        Meeple.addNewPlayer(hero_name, hero_type)

        print("\n~ ~ ~ Folgende Spieler haben das Spielfeld betreten: ~ ~ ~")
        print("\n".join([f"{i.name} spielt {i.getHeroType()}." for i in Meeple.players]))

        print("\n~ ~ ~ Folgende Vorkehrungen wurden getroffen: ~ ~ ~")
        print(f"{len(Quest.quest_table)} Questkarten wurden gemischt und {len(Item.item_table)} Gegenstände wurden Monstern übergeben.")

def gameLoop():
    game_running = True

    while game_running:
        print(Constants.GAME_NEW_ROUND_START.replace("XX", str(Meeple.rounds)))

        result = roundLoop()

        #check if players dead or wincondition
        if len(Meeple.players) == 0 or result == Constants.GAME_NO_QUEST:
            game_running = False
            print(Constants.GAME_LOST_FOR_ALL)
        
        if result == Constants.GAME_WON:
            break

        Meeple.resetRoundPlayed()

def roundLoop():
    while True:
        next_player = Meeple.nextPlayer()
        if next_player is None:
            return Constants.GAME_ALL_PLAYED

        if next_player.progress == Constants.GAME_REQ_LAST_QUEST:
            rnd_quest = Quest.lastQuest

            print(Constants.GAME_PLAYER_GO.replace("XX", next_player.name))

            if next_player.checkSkipMove() or next_player.archer_talent_roll():
                #diffquesttypes
                result = executeLastQuest(rnd_quest, next_player)
                if result:
                    print(Constants.GAME_PLAYER_WINS.replace("XX", next_player.name))
                    return Constants.GAME_WON
                else:
                    Meeple.removePlayer(next_player)
                    print(Constants.GAME_PLAYER_LOST)

        else:
            rnd_quest = Quest.getQuest()
            if rnd_quest is None:
                return Constants.GAME_NO_QUEST

            print(Constants.GAME_PLAYER_GO.replace("XX", next_player.name))

            if next_player.checkSkipMove() or next_player.archer_talent_roll():
                #diffquesttypes
                result = executeQuest(rnd_quest, next_player)

                #handleresults in quest.py
                if result:
                    next_player.progress += 1
                    print(Constants.GAME_PLAYER_STAT_CHANGE)
                    
                    #wizardquest
                    if next_player.wizard_talent_roll():
                        print(Constants.GAME_PLAYER_GO.replace("XX", next_player.name))
                        rnd_quest = Quest.getQuest()
                        result = executeQuest(rnd_quest, next_player)

                        if result:
                            next_player.progress += 1
                            print(Constants.GAME_PLAYER_STAT_CHANGE)
                        else:
                            Meeple.removePlayer(next_player)
                            print(Constants.GAME_PLAYER_LOST)

                else:
                    Meeple.removePlayer(next_player)
                    print(Constants.GAME_PLAYER_LOST)

            else:
                next_player.freeSkipMoves()
                print(Constants.GAME_PLAYER_SKIP_MOVE)
            
            next_player.setRoundPlayed()
            print(Constants.GAME_ROUND_OVER.replace("XX", next_player.name))

initRequirements()
initPlayers()
gameLoop()