# from datetime import date


# class Llama:
#     def __init__(self):
#         self.name = ""
#         self.species = ""
#         self.date_added = date.today()


# miss_fuzz = Llama()
# miss_fuzz.name = "Miss Fuzz"
# miss_fuzz.species = "domestic llama"
# miss_fuzz.walking = True
# print(miss_fuzz)


# class Tiger:
#     def __init__(self, name, species):
#         self.name = ""
#         self.species = ""
#         self.date_added = date.today()
#         self.walking = True


# rufus = Tiger("Rufus", "domestic tiger")
# print(rufus)


# class Zebra:
#     def __init__(self, name, species):
#         self.name = ""
#         self.species = ""
#         self.date_added = date.today()
#         self.walking = True


# stripes = Zebra("Stripes", "Zebra")
# print(stripes)


# class Rhino:
#     def __init__(self, name, species):
#         self.name = ""
#         self.species = ""
#         self.date_added = date.today()
#         self.walking = True


# bill = Rhino("Bill", "rhino")
# print(bill)


# class Rabbit:
#     def __init__(self, name, species):
#         self.name = ""
#         self.species = ""
#         self.date_added = date.today()
#         self.walking = True


# hopper = Rabbit("Hopper", "rabbit")
# print(hopper)


# class Goat:
#     def __init__(self, name, species):
#         self.name = ""
#         self.species = ""
#         self.date_added = date.today()
#         self.walking = True


# jim = Goat("Jim", "goat")
# print(jim)


# class Copperhead:
#     def __init__(self, name, species):
#         self.name = ""
#         self.species = ""
#         self.date_added = date.today()
#         self.slithering = True


# slithery_boy = Copperhead("Slithery Boy", "copperhead")
# print(slithery_boy)


# class Salamander:
#     def __init__(self, name, species):
#         self.name = ""
#         self.species = ""
#         self.date_added = date.today()
#         self.slithering = True


# sal = Salamander("Sal", "salamander")
# print(sal)


# class Kingsnake:
#     def __init__(self, name, species):
#         self.name = ""
#         self.species = ""
#         self.date_added = date.today()
#         self.slithering = True


# majesty = Kingsnake("Majesty", "king snake")
# print(majesty)


# class GardenSnake:
#     def __init__(self, name, species):
#         self.name = ""
#         self.species = ""
#         self.date_added = date.today()
#         self.slithering = True


# squirmy = GardenSnake("Squirmy", "garden snake")
# print(squirmy)


# class Anaconda:
#     def __init__(self, name, species):
#         self.name = ""
#         self.species = ""
#         self.date_added = date.today()
#         self.slithering = True


# angela = Anaconda("Angela", "anaconda")
# print(angela)


# class Goldfish:
#     def __init__(self, name, species):
#         self.name = ""
#         self.species = ""
#         self.date_added = date.today()
#         self.swimming = True


# goldie = Goldfish("Goldie", "goldfish")
# print(goldie)


# class Octopus:
#     def __init__(self, name, species):
#         self.name = ""
#         self.species = ""
#         self.date_added = date.today()
#         self.swimming = True


# arms = Octopus("Arms", "octopus")
# print(arms)


# class SeaSnail:
#     def __init__(self, name, species):
#         self.name = ""
#         self.species = ""
#         self.date_added = date.today()
#         self.swimming = True


# sticky = SeaSnail("Sticky", "sea snail")
# print(sticky)


# class BetaFish:
#     def __init__(self, name, species):
#         self.name = ""
#         self.species = ""
#         self.date_added = date.today()
#         self.swimming = True


# angry = BetaFish("Angry", "beta fish")
# print(angry)


# class Clam:
#     def __init__(self, name, species):
#         self.name = ""
#         self.species = ""
#         self.date_added = date.today()
#         self.swimming = True


# cloyster = Clam("Cloyster", "clam")
# print(cloyster)

from animals import Anaconda, Kingsnake, Copperhead, Salamander, GardenSnake, Octopus, Clam, Goldfish, BetaFish, SeaSnail, Llama, Tiger, Zebra, Rabbit, Rhino, Goat

from attractions import SnakePit, Wetlands, PettingZoo

jim = Goat("Jim", "goat", "A", "hay")
hopper = Rabbit("Hopper", "rabbit", "A", "rabbit food")
bill = Rhino("Bill", "rhino", "B", "grass")
rufus = Tiger("Rufus", "domestic tiger", "B", "Jim")
stripes = Zebra("Stripes", "Zebra", "C", "grass")
miss_fuzz = Llama("Miss Fuzz", "domestic llama", "C", "oats")
goldie = Goldfish("Goldie", "goldfish", "fish food")
cloyster = Clam("Cloyster", "clam", "clam food")
sticky = SeaSnail("Sticky", "sea snail", "algae")
angry = BetaFish("Angry", "beta fish", "fish food")
arms = Octopus("Arms", "octopus", "fish")
sal = Salamander("Sal", "salamander", "no idea")
majesty = Kingsnake("Majesty", "king snake", "mice")
squirmy = GardenSnake("Squirmy", "garden snake", "mice")
slithery_boy = Copperhead("Slithery Boy", "copperhead", "mice")
angela = Anaconda("Angela", "anaconda", "mice")

varmint_village = PettingZoo("Varmint Village")
marsh_madness = Wetlands("Marsh Madness")
noodle_town = SnakePit("Noodle Town")

varmint_village.house_animal(jim)
varmint_village.house_animal(hopper)
varmint_village.house_animal(rufus)
varmint_village.house_animal(miss_fuzz)
varmint_village.house_animal(stripes)
varmint_village.house_animal(bill)

marsh_madness.house_animal(goldie)
marsh_madness.house_animal(cloyster)
marsh_madness.house_animal(sticky)
marsh_madness.house_animal(angry)
marsh_madness.house_animal(arms)

noodle_town.house_animal(sal)
noodle_town.house_animal(majesty)
noodle_town.house_animal(squirmy)
noodle_town.house_animal(slithery_boy)
noodle_town.house_animal(angela)

for animal in varmint_village.animals:
    print(f'you can find {animal.name} in {varmint_village.attraction_name}')

for animal in marsh_madness.animals:
    print(f'you can find {animal.name} in {marsh_madness.attraction_name}')

for animal in noodle_town.animals:
    print(f'you can find {animal.name} in {noodle_town.attraction_name}')