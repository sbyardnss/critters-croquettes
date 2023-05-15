from datetime import date

class Copperhead:
    """slithering instance"""
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
        self.__chip_number = chip_num
    def __str__(self):
        return f'{self.name} is a {self.species}'
    @property 
    def chip_number(self):
        return self.__chip_number
    @chip_number.setter
    def chip_number(self, number):
        pass


# slithery_boy = Copperhead("Slithery Boy", "copperhead", "mice")
# print(slithery_boy)
