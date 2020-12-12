#import json

class Pruefung:

    def __init__(self, TextEntscheidung, TextJa, TextNein,
        AufgabeJaKategorie, AufgabeJaKosten,
        AufgabeNeinKategorie, AufgabeNeinKosten):
        self.TextEntscheidung = TextEntscheidung
        self.TextJa = TextJa
        self.TextNein = TextNein
        self.AufgabeJaKategorie = AufgabeJaKategorie
        self.AufgabeNeinKategorie = AufgabeNeinKategorie
        self.AufgabeJaKosten = AufgabeJaKosten
        self.AufgabeNeinKosten = AufgabeNeinKosten
'''
        f =  open("./test.json")
        pruefung_data = json.load(f, "utf-8")
        Pruefung.pruefungen.append(pruefung_data)
    
    @staticmethod
    def definePruefungen():
        f =  open("./test.json")
        pruefung_data = json.load(f, "utf-8")
        Pruefung.pruefungen.append(pruefung_data)

    def getJson(self):
        return Pruefung.pruefungen



test = Pruefung(1,1,1,1,1,1,1)
test2 = Pruefung(1,1,1,1,1,1,1)
print(test.getJson())
print(test2.getJson())
Pruefung.definePruefungen()
print(test.getJson())
print(test2.getJson())
print(test2.TextEntscheidung)
'''