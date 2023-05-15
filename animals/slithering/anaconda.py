from ..animals import Animal

class Anaconda(Animal):
    """slithering instance"""
    def __init__(self, name, shift, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.slithering = True
    # def __str__(self):
    #     return f'{self.name} is a {self.species}'
    def __repr__(self):
        return f'{self.__class__.__name__}: ({self.name}, {self.species}, {self.date_added}, {self.slithering}, {self.shift}, {self.food}, {self.chip_number})'



# angela = Anaconda("Angela", "anaconda", "mice")
# print(angela)

