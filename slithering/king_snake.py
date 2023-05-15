from datetime import date

class Kingsnake:
    """slithering instance"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


majesty = Kingsnake("Majesty", "king snake")
print(majesty)
