from .attraction import Attraction

class PettingZoo(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)

class Wetlands(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)

class SnakePit(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)


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