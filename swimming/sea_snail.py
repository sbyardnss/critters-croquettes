from datetime import date

class SeaSnail:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


sticky = SeaSnail("Sticky", "sea snail")
print(sticky)