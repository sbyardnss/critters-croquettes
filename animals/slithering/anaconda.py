from ..animals import Animal
from ..movements import Swimming, Slithering
class Anaconda(Animal):
    """slithering instance"""
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
        Swimming.__init__(self)
    def __str__(self):
        return f'{self.name} is a {self.species}'
    # def __repr__(self):
    #     return f'{self.__class__.__name__}: ({self.name}, {self.species}, {self.date_added}, {self.slithering}, {self.shift}, {self.food}, {self.chip_number})'



