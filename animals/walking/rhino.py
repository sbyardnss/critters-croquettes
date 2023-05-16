from datetime import date
from ..animals import Animal
from ..movements import Walking

class Rhino(Animal):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
    # def feed(self):
    #     print(f"{self.name} was fed {self.food} on {date.today().strftime('%m/%d/%Y')}")
    # def __repr__(self):
    #     return f'{self.__class__.__name__}: ({self.name}, {self.species}, {self.date_added}, {self.walking}, {self.shift}, {self.food})'
    def __str__(self):
        return f'{self.name} the {self.species}'


# bill = Rhino("Bill", "rhino", "B", "grass")
# print(bill)