from ..animals import Animal
class Goat(Animal):
    def __init__(self, name, shift, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True
    def __repr__(self):
        return f'{self.__class__.__name__}: ({self.name}, {self.species}, {self.date_added}, {self.walking}, {self.shift}, {self.food}, {self.chip_number})'


# jim = Goat("Jim", "goat", "A", "hay")
# print(jim)
# print(f"{jim.name} is available during the {jim.shift} shift")