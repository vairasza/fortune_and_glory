import json
import data.Constants as Constants

class Quest:

    quest_table = []

    def __init__(self, id):
        if len(Quest.quest_table) == 0: Quest.loadQuests()

        #creates an instance variable that holds one quest
        self.__dict__.update(Quest.quest_table[id])
    
    @staticmethod
    def loadQuests():
        Quest.quest_table = json.load(open(Constants.FN_QUEST_DATA))