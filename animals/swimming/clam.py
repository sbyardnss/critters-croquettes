from ..animals import Animal
class Clam(Animal):
    def __init__(self, name, shift, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.swimming = True
    def __repr__(self):
        return f'{self.__class__.__name__}: ({self.name}, {self.species}, {self.date_added}, {self.swimming}, {self.shift}, {self.food}, {self.chip_number})'



# cloyster = Clam("Cloyster", "clam", "clam food")
# print(cloyster)