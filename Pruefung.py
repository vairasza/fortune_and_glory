class Pruefung:

    #1: choice yes/no => different task
    #task 1: is set in a certain categorie e.g. speed
    #player has to overcome a price => player rolls as many dice as he got category points
    #if sum of dice eyes is greater than price, task succeeds and he gets a reward
    #otherwise he he loses lifepoints

    #1 quest has a text displayed to the player before accepting the quest

    #Vor dir tut sich eine tiefe Schlucht auf, über die eine wackelige Hängebrücke führt. Die Brücke könnte
    #jeden Moment einstürzen und dich in die Tiefe reißen. Betrittst du die Brücke?

    #2 player inputs yes
    # Auf der Mitte der Brücke hörst du ein bedrohliches Zischen: Eines der Seile, das die Brücke hält, ist
    #gerissen. Renne um dein Leben!

    #2 player inputs no
    #Du versuchst, einen anderen Weg um die Schlucht herum zu finden, doch das kostet Zeit – Setze eine
    #Runde aus.


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