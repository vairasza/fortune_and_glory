FN_QUEST_DATA = "./data/quest_data.json"
FN_ITEM_DATA = "./data/item_data.json"

HERO_BASIC_STAT = 5
HERO_BASIC_STAT_SPREAD = 2
HERO_INV_MAX_SIZE = 5
DICE_SIDES = 6
HERO_TYPE_KNIGHT = "knight"
HERO_TYPE_WIZARD = "wizard"
HERO_TYPE_ARCHER = "archer"
HERO_TYPE_KNIGHT_LOC = "Ritter"
HERO_TYPE_WIZARD_LOC = "Zauberer"
HERO_TYPE_ARCHER_LOC = "Bogenschütze"

WIZARD_TALENT_REQ = 5
ARCHER_TALENT_REQ = 3
KNIGHT_TALENT_REQ = 5
WIZARD_TALENT_NAME = "Temporalschleife"
ARCHER_TALENT_NAME = "Camouflage"
KNIGHT_TALENT_NAME = "Schildwall"
WIZARD_TALENT_DESC = f"Wenn du eine Quest erfolgreich abschließt, kannst du mit einer {WIZARD_TALENT_REQ} oder höher eine weitere Quest diese Runde bestreiten."
ARCHER_TALENT_DESC = f"Wenn du die nächste Runde aussetzen musst, kannst du das mit einer {ARCHER_TALENT_REQ} oder höher verhindern."
KNIGHT_TALENT_DESC = f"Wenn du eine Quest verlierst, kannst du mit einer {KNIGHT_TALENT_REQ} oder höher den Lebenspunkteverlust verhindern."
WIZARD_TALENT_USE = f"~ ~ ~ Du setzt dein Talent ein: {WIZARD_TALENT_NAME} ~ ~ ~"
ARCHER_TALENT_USE = f"~ ~ ~ Du setzt dein Talent ein: {ARCHER_TALENT_NAME} ~ ~ ~"
KNIGHT_TALENT_USE = f"~ ~ ~ Du setzt dein Talent ein: {KNIGHT_TALENT_NAME} ~ ~ ~"
ARCHER_TALENT_PROC = "Erfolg: Du hast keinen Lebenspunkt verloren."
WIZARD_TALENT_PROC = "Erfolg: Du kannst eine weitere Quest in diesem Zug machen."
KNIGHT_TALENT_PROC = "Erfolg: Du musst die nächste Runde nicht aussetzen."
WIZARD_STATS = {
    "lifepoints": 0,
    "strength": -1,
    "intellect": 4,
    "agility": 0,
    "speed": 0,
    "charisma": 2
}
ARCHER_STATS = {
    "lifepoints": 0,
    "strength": 0,
    "intellect": 4,
    "agility": 0,
    "speed": 2,
    "charisma": 1
}
KNIGHT_STATS = {
    "lifepoints": 2,
    "strength": 3,
    "intellect": 0,
    "agility": 0,
    "speed": -1,
    "charisma": 0
}

GAME_NAME = "Fortune and Glory"
GAME_WELCOME = "\n~ ~ ~ Herzlich Willkommen zu 'Fortune and Glory'! ~ ~ ~\n\nWie viele Spieler seid ihr?"
MIN_PLAYERS = 1
MAX_PLAYERS = 4

QUEST_INPUT_DECISION = "Gib folgendes ein [XX]: "
QUEST_SUCCESS = "\t=> Erfolg: Du hast die Aufgabe bestanden.\n"
QUEST_FAIL = "\t=> Niederlage: Die Aufgabe ist fehlgeschlagen.\n"
QUEST_ROLLING_RESULT = "Die Kosten betragen XX. Dein Ergebnis ist YY."
QUEST_HERO_LIFEPOINTS_LEFT = "Du hast noch XX Lebenspunkte übrig."
QUEST_HERO_LIFEPOINTS_ZERO = "Du hast keine Lebenspunkte mehr."
QUEST_HERO_RECEIVED_ITEM = "Durch deinen Erfolg hast du folgenden Gegenstand erhalten: XX. Es hat folgende Werte: YY"
QUEST_HERO_INV_FULL_1 = "Du kannst den Gegenstand nicht mitnehmen, da dein Inventar leider voll ist und Sie den Gegenstand bereits besitzen."
QUEST_HERO_INV_FULL_2 = "Du kannst den Gegenstand nicht mitnehmen, da dein Inventar leider voll ist. Möchtest du einen Gegenstand dafür wegwerfen?"
QUEST_HERO_INV_ITEM_ADDED = "XX wurde deinem Inventar hinzugefügt."
QUEST_HERO_ITEM_DROPPED = "XX wurde liegen gelassen und nicht deinem Inventar hinzugefügt."
QUEST_HERO_ITEM_DOUBLE = "Der erhaltene Gegenstand ist bereits in eurem Inventar. Du kannst ihn demnach nicht mehr mitnehmen."
QUEST_HERO_ITEM_REPLACE = "XX wurde durch YY in deinem Inventar ersetzt."

GAME_LOST = 0
GAME_CONTINUE = 1
GAME_NO_QUEST = 2
GAME_ALL_PLAYED = 3
GAME_WON = 4
GAME_LOST_FOR_ALL = "\n~ ~ ~ Spiel vorbei! Ihr habt alle verloren! ~ ~ ~"
GAME_PLAYER_GO = "\n~ ~ ~ XX ist an der Reihe! ~ ~ ~"
GAME_PLAYER_LOST = "Du hast keine Lebenspunkte mehr und kannst nicht mehr mitspielen."
GAME_PLAYER_SKIP_MOVE = "Du musst diese Runde aussetzen."
GAME_PLAYER_STAT_CHANGE = "Deine Werte haben sich geändert."
GAME_NEW_ROUND_START = "\n~ ~ ~ Runde XX beginnt: ~ ~ ~"
GAME_CHOOSE_NUM_PLAYERS = "\n~ ~ ~ Spieler XX ~ ~ ~\nBitte mach ein paar Anpassungen für deinen Helden."
GAME_HERO_NAME_CHOOSE = "Wie möchtest du genannt werden?"
GAME_HERO_TYPE_CHOOSE = "\nWelchen Heldentypen möchstest du spielen?"
GAME_HERO_TYPE_CHOOSE_K = f"1) {HERO_TYPE_KNIGHT_LOC}:\n\tTalent -> {KNIGHT_TALENT_DESC}\n\tZusätzliche Werte -> {KNIGHT_STATS}\n"
GAME_HERO_TYPE_CHOOSE_W = f"2) {HERO_TYPE_WIZARD_LOC}:\n\tTalent -> {WIZARD_TALENT_DESC}\n\tZusätzliche Werte -> {WIZARD_STATS}\n"
GAME_HERO_TYPE_CHOOSE_A = f"3) {HERO_TYPE_ARCHER_LOC}:\n\tTalent -> {ARCHER_TALENT_DESC}\n\tZusätzliche Werte -> {ARCHER_STATS}"
GAME_ROUND_OVER = "~ ~ ~ Der Zug von XX ist nun zu Ende! ~ ~ ~"
GAME_REQ_LAST_QUEST = 5
GAME_PLAYER_WINS = "~ ~ ~ Spieler XX hat das Spiel gewonnen! ~ ~ ~"