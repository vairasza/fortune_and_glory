import json
import Pruefung

quest_table = []

quest_data = json.load(open("./data.json"))

quest_1 = Pruefung(quest_data[1]["text_decision"], quest_data[1]["text_confirm"], quest_data[1]["text_deny"],
    quest_data[1]["quest_yes_category"], quest_data[1]["quest_yes_price"],
    quest_data[1]["quest_no_category"], quest_data[1]["quest_no_price"])

quest_2 = Pruefung(quest_data[2]["text_decision"], quest_data[2]["text_confirm"], quest_data[2]["text_deny"],
    quest_data[2]["quest_yes_category"], quest_data[2]["quest_yes_price"],
    quest_data[2]["quest_no_category"], quest_data[2]["quest_no_price"])

quest_3 = Pruefung(quest_data[3]["text_decision"], quest_data[3]["text_confirm"], quest_data[3]["text_deny"],
    quest_data[3]["quest_yes_category"], quest_data[3]["quest_yes_price"],
    quest_data[3]["quest_no_category"], quest_data[3]["quest_no_price"])

quest_table.append(quest_1)
quest_table.append(quest_2)
quest_table.append(quest_3)
