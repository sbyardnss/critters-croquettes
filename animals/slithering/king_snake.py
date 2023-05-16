from ..animals import Animal
from ..movements import Slithering
class Kingsnake(Animal):
    """slithering instance"""
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
    # def __repr__(self):
    #     return f'{self.__class__.__name__}: ({self.name}, {self.species}, {self.date_added}, {self.slithering}, {self.shift}, {self.food}, {self.chip_number})'
    def __str__(self):
        return f'{self.name} the {self.species}'

# majesty = Kingsnake("Majesty", "king snake", "mice")
# print(majesty)
