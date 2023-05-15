from datetime import date

class Zebra:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift


stripes = Zebra("Stripes", "Zebra", "C")
print(stripes)