from ..animals import Animal
from datetime import date

class BetaFish(Animal):
    def __init__(self, name, shift, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.swimming = True
    def __repr__(self):
        return f'{self.__class__.__name__}: ({self.name}, {self.species}, {self.date_added}, {self.swimming}, {self.shift}, {self.food}, {self.chip_number})'
    def feed(self):
        return f'{self.name} the {self.species} feasted on the blood of their enemies on {date.today().strftime("%m/%d/%Y")} '



# angry = BetaFish("Angry", "beta fish", "fish food")
# print(angry)