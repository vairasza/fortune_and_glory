class Spielfigur:

    #name
    #int: life, strength, int, speed, charisma (3-6)
    #has backpack -> list of objects (limit für alle gleich N=5)
    #bool aussetzen
    #static var fortschritt

    def __init__(self, name):
        self.name = name

    def getName(self):
        self.name

    def setName(self, name):
        self.name = name


test = Spielfigur("torsten")

print(test.getName())