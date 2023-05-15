from datetime import date

class Clam:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food
    def __str__(self):
        return f'{self.name} is a {self.species}'


cloyster = Clam("Cloyster", "clam", "clam food")
print(cloyster)