from animals import Anaconda, Kingsnake, Copperhead, Salamander, GardenSnake, Octopus, Clam, Goldfish, BetaFish, SeaSnail, Llama, Tiger, Zebra, Rabbit, Rhino, Goat, Goose
from attractions import PettingZoo, Wetlands, SnakePit

# from attractions.attractions import SnakePit, Wetlands, PettingZoo

animals = []
jim = Goat("Jim", "goat", "hay", 191683)
hopper = Rabbit("Hopper", "rabbit", "rabbit food", 967298)
bill = Rhino("Bill", "rhino", "grass", 898528)
rufus = Tiger("Rufus", "domestic tiger", "Jim", 409761)
stripes = Zebra("Stripes", "Zebra", "grass", 187308)
miss_fuzz = Llama("Miss Fuzz", "domestic llama", "oats", 299476)
goldie = Goldfish("Goldie", "goldfish", "fish food", 781092)
cloyster = Clam("Cloyster", "clam", "clam food", 482087)
sticky = SeaSnail("Sticky", "sea snail", "algae", 502864)
angry = BetaFish("Angry", "beta fish", "fish food", 792096)
arms = Octopus("Arms", "octopus", "fish", 792074)
sal = Salamander("Sal", "salamander", "no idea", 572943)
majesty = Kingsnake("Majesty", "king snake", "mice", 582085)
squirmy = GardenSnake("Squirmy", "garden snake", "mice", 263495)
slithery_boy = Copperhead("Slithery Boy", "copperhead", "mice", 555783)
angela = Anaconda("Angela", "anaconda", "mice", 123456)
animals.append(jim)
animals.append(hopper)
animals.append(bill)
animals.append(rufus)
animals.append(stripes)
animals.append(miss_fuzz)
animals.append(goldie)
animals.append(cloyster)
animals.append(sticky)
animals.append(angry)
animals.append(arms)
animals.append(sal)
animals.append(majesty)
animals.append(squirmy)
animals.append(slithery_boy)
animals.append(angela)

varmint_village = PettingZoo("Varmint Village", "critters that like to dig and scour")
marsh_madness = Wetlands("Marsh Madness", "wet place")
noodle_town = SnakePit("Noodle Town", "snake place")
for animal in animals:
    varmint_village.add_animal_pythonic(animal)
for animal in animals:
    marsh_madness.add_animal_pythonic(animal)
for animal in animals:
    noodle_town.add_animal_pythonic(animal)
for animal in noodle_town.animals:
    print(animal)

# for animal in varmint_village.animals:
#     print(f'you can find {animal.name} in {varmint_village.attraction_name}')

# for animal in marsh_madness.animals:
#     print(f'you can find {animal.name} in {marsh_madness.attraction_name}')

# for animal in noodle_town.animals:
#     print(f'you can find {animal.name} in {noodle_town.attraction_name}')

# attractions = []
# attractions.append(varmint_village)
# attractions.append(marsh_madness)
# attractions.append(noodle_town)

# for attraction in attractions:
#     print(f'{attraction.attraction_name} is where you will find:')
#     for animal in attraction.animals:
#         print(f'{animal.name} the {animal.species}')

# slithery_boy.chip_num = 555784
# print(slithery_boy.chip_number)  


bob = Goose("Bob", "Canada goose", "watercress sandwiches", 678203)
# varmint_village.add_animal(bob)
# bob.run()
# bob.swim()
# print(bob)

# varmint_village.add_animal_pythonic(bob)
# varmint_village.add_animal_type_check(bob)
# varmint_village.add_animal_pythonic(angela)
# varmint_village.add_animal_type_check(angela)
# for animal in varmint_village.animals:
#     print(animal)