from datetime import date
from ..animals import Animal
class Tiger(Animal):
    def __init__(self, name, shift, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True
    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today().strftime('%m/%d/%Y')}")
    def __repr__(self):
        return f'{self.__class__.__name__}: ({self.name}, {self.species}, {self.date_added}, {self.walking}, {self.shift}, {self.food})'



# rufus = Tiger("Rufus", "domestic tiger", "B", "Jim")
# print(rufus)
