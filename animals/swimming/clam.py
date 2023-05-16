from ..animals import Animal
from ..movements import Swimming
class Clam(Animal):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
    # def __repr__(self):
    #     return f'{self.__class__.__name__}: ({self.name}, {self.species}, {self.date_added}, {self.swimming}, {self.shift}, {self.food}, {self.chip_number})'
    def __str__(self):
        return f'{self.name} the {self.species}'


# cloyster = Clam("Cloyster", "clam", "clam food")
# print(cloyster)