from datetime import date
from ..animals import Animal
from ..movements import Walking
class Llama(Animal):
    """llama"""
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today().strftime('%m/%d/%Y')}")
    # def __repr__(self):
    #     return f'{self.__class__.__name__}: ({self.name}, {self.species}, {self.date_added}, {self.walking}, {self.shift}, {self.food})'
    def __str__(self):
        return f'{self.name} the {self.species}'

# miss_fuzz = Llama("Miss Fuzz", "domestic llama", "C", "oats")
# # print(miss_fuzz)
# # print(miss_fuzz.feed())
# print(miss_fuzz)