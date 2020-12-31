import json
import data.Constants as Constants
import random

class Quest:

    quest_table = []

    def __init__(self, id):
        #if len(Quest.quest_table) == 0: Quest.loadQuests()

        #creates an instance variable that holds one quest
        self.__dict__.update(Quest.quest_table[id])
    
    @staticmethod
    def loadQuests():
        Quest.quest_table = json.load(open(Constants.FN_QUEST_DATA))
        Quest.length = len(Quest.quest_table)
    
    #remove quest from list so we dont get the same quest over and over again
    @staticmethod
    def getQuest():
        rnd_quest = random.choice(Quest.quest_table)
        Quest.quest_table.remove(rnd_quest)
        return rnd_quest