from datetime import date

class Copperhead:
    """slithering instance"""
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
    def __str__(self):
        return f'{self.name} is a {self.species}'


slithery_boy = Copperhead("Slithery Boy", "copperhead", "mice")
print(slithery_boy)
