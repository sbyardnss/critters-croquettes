from ..animals import Animal
from ..movements import Slithering
# class Copperhead:
#     """slithering instance"""
#     def __init__(self, name, species, food, chip_num):
#         self.name = name
#         self.species = species
#         self.date_added = date.today()
#         self.slithering = True
#         self.food = food
#         self.__chip_number = chip_num
#     def __str__(self):
#         return f'{self.name} is a {self.species}'
#     @property 
#     def chip_number(self):
#         return self.__chip_number
#     @chip_number.setter
#     def chip_number(self, number):
#         pass


# # slithery_boy = Copperhead("Slithery Boy", "copperhead", "mice")
# # print(slithery_boy)

class Copperhead(Animal):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self,name, species, food, chip_num)
        Slithering.__init__(self)
    # def __repr__(self):
    #     return f'{self.__class__.__name__}: ({self.name}, {self.species}, {self.date_added}, {self.slithering}, {self.shift}, {self.food}, {self.chip_number})'
    def __str__(self):
        return f'{self.name} the {self.species}'