from datetime import date

class Kingsnake:
    def __init__(self, name, species):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True


majesty = Kingsnake("Majesty", "king snake")
print(majesty)