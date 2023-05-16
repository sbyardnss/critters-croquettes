from ..animals import Animal
from ..movements import Walking
class Goat(Animal):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
    # def __repr__(self):
    #     return f'{self.__class__.__name__}: ({self.name}, {self.species}, {self.date_added}, {self.walking}, {self.shift}, {self.food}, {self.chip_number})'
    def __str__(self):
        return f'{self.name} the {self.species}'

# jim = Goat("Jim", "goat", "A", "hay")
# print(jim)
# print(f"{jim.name} is available during the {jim.shift} shift")