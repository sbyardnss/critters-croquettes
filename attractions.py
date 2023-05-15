class PettingZoo:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()
    def house_animal(self, animal):
        self.animals.append(animal)

# varmint_village = PettingZoo("Varmint Village")

class Wetlands:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "slightly wet critters to cuddle"
        self.animals = list()
    def house_animal(self, animal):
        self.animals.append(animal)

# marsh_madness = Wetlands("Marsh Madness")

class SnakePit:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "slithery critters to cuddle"
        self.animals = list()
    def house_animal(self, animal):
        self.animals.append(animal)

# noodle_town = SnakePit("Noodle Town")