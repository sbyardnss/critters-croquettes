from ..animals import Animal

class Kingsnake(Animal):
    """slithering instance"""
    def __init__(self, name, shift, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.slithering = True
    def __repr__(self):
        return f'{self.__class__.__name__}: ({self.name}, {self.species}, {self.date_added}, {self.slithering}, {self.shift}, {self.food}, {self.chip_number})'


# majesty = Kingsnake("Majesty", "king snake", "mice")
# print(majesty)
