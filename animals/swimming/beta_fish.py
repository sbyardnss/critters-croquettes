from ..animals import Animal
from datetime import date
from ..movements import Swimming
class BetaFish(Animal):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
    # def __repr__(self):
    #     return f'{self.__class__.__name__}: ({self.name}, {self.species}, {self.date_added}, {self.swimming}, {self.shift}, {self.food}, {self.chip_number})'
    def feed(self):
        return f'{self.name} the {self.species} feasted on the blood of their enemies on {date.today().strftime("%m/%d/%Y")} '
    def __str__(self):
        return f'{self.name} the {self.species}'

# angry = BetaFish("Angry", "beta fish", "fish food")
# print(angry)