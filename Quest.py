import json
import data.Constants as Constants
import random

class Quest:

    quest_table = []

    def __init__(self, quest_obj):
        self.quest_id = quest_obj["quest_id"]
        self.quest_type = quest_obj["quest_type"]
        self.text_decision = quest_obj["text_decision"]
        self.text_confirm = quest_obj["text_confirm"]
        self.text_deny = quest_obj["text_deny"]
        self.quest_yes_category = quest_obj["quest_yes_category"]
        self.quest_yes_price = quest_obj["quest_yes_price"]
        self.quest_no_category = quest_obj["quest_no_category"]
        self.quest_no_price = quest_obj["quest_no_price"]
        self.difficulty = quest_obj["difficulty"]

    def __lt__(self, other):
        return self.difficulty < other.difficulty

    @staticmethod
    def loadQuests():
        quest_list = json.load(open(Constants.FN_QUEST_DATA))

        Quest.quest_table = [Quest(quest) for quest in quest_list]
        
        #sort by difficulty so we get the easy quests first
        random.shuffle(Quest.quest_table)
        Quest.quest_table.sort()
        Quest.length = len(Quest.quest_table)
    
    #remove quest from list so we dont get the same quest over and over again
    @staticmethod
    def getQuest():
        return Quest.quest_table.pop(0)