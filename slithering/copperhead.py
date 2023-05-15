from datetime import date

class Copperhead:
    """slithering instance"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


slithery_boy = Copperhead("Slithery Boy", "copperhead")
print(slithery_boy)
