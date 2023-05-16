from .attraction import Attraction
from animals import Walking, Slithering, Swimming

class PettingZoo(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal_pythonic(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            pass
            # print(f'{animal} doesn\'t like to be petted, so please do not put it in the {self.__class__.__name__} attraction')
    def add_animal_type_check(self, animal):
        if isinstance(animal, Walking):
            self.animals.append(animal)
            print(f"{animal} now lives in {self.attraction_name}")
        else:
            pass
            # print(f'{animal} doesn\'t like to be petted, so please do not put it in the {self.__class__.__name__} attraction')


class Wetlands(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)
    def add_animal_pythonic(self, animal):
        try:
            if animal.swim_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            pass
            # print(f'{animal} doesn\'t like to swim, so please do not put it in the {self.__class__.__name__} attraction')
    def add_animal_type_check(self, animal):
        if isinstance(animal, Swimming):
            self.animals.append(animal)
            print(f"{animal} now lives in {self.attraction_name}")
        else:
            pass
            # print(f'{animal} doesn\'t like to swim, so please do not put it in the {self.__class__.__name__} attraction')


class SnakePit(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)
    def add_animal_pythonic(self, animal):
        try:
            if animal.slither_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            pass
            # print(f'{animal} doesn\'t like to slither, so please do not put it in the {self.__class__.__name__} attraction')
    def add_animal_type_check(self, animal):
        if isinstance(animal, Slithering):
            self.animals.append(animal)
            print(f"{animal} now lives in {self.attraction_name}")
        else:
            pass
            # print(f'{animal} doesn\'t like to slither, so please do not put it in the {self.__class__.__name__} attraction')


# class PettingZoo:
#     def __init__(self, name):
#         self.attraction_name = name
#         self.description = "cute and fuzzy critters to cuddle"
#         self.animals = list()
#     def house_animal(self, animal):
#         self.animals.append(animal)
#     @property
#     def last_critter_added(self):
#         return self.animals[-1]
# # varmint_village = PettingZoo("Varmint Village")

# class Wetlands:
#     def __init__(self, name):
#         self.attraction_name = name
#         self.description = "slightly wet critters to cuddle"
#         self.animals = list()
#     def house_animal(self, animal):
#         self.animals.append(animal)

# # marsh_madness = Wetlands("Marsh Madness")

# class SnakePit:
#     def __init__(self, name):
#         self.attraction_name = name
#         self.description = "slithery critters to cuddle"
#         self.animals = list()
#     def house_animal(self, animal):
#         self.animals.append(animal)

# # noodle_town = SnakePit("Noodle Town")