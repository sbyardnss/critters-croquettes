from animals import Anaconda, Kingsnake, Copperhead, Salamander, GardenSnake, Octopus, Clam, Goldfish, BetaFish, SeaSnail, Llama, Tiger, Zebra, Rabbit, Rhino, Goat, Goose
from attractions import PettingZoo
# from attractions.attractions import SnakePit, Wetlands, PettingZoo

jim = Goat("Jim", "A", "goat", "hay", 191683)
hopper = Rabbit("Hopper", "A", "rabbit", "rabbit food", 967298)
bill = Rhino("Bill", "B", "rhino", "grass", 898528)
rufus = Tiger("Rufus", "B", "domestic tiger", "Jim", 409761)
stripes = Zebra("Stripes", "C", "Zebra", "grass", 187308)
miss_fuzz = Llama("Miss Fuzz", "C", "domestic llama", "oats", 299476)
goldie = Goldfish("Goldie", "C", "goldfish", "fish food", 781092)
cloyster = Clam("Cloyster", "B", "clam", "clam food", 482087)
sticky = SeaSnail("Sticky", "B", "sea snail", "algae", 502864)
angry = BetaFish("Angry", "A", "beta fish", "fish food", 792096)
arms = Octopus("Arms", "A", "octopus", "fish", 792074)
sal = Salamander("Sal", "C", "salamander", "no idea", 572943)
majesty = Kingsnake("Majesty", "B", "king snake", "mice", 582085)
squirmy = GardenSnake("Squirmy", "B", "garden snake", "mice", 263495)
slithery_boy = Copperhead("Slithery Boy", "A", "copperhead", "mice", 555783)
angela = Anaconda("Angela", "A", "anaconda", "mice", 123456)
# angela.__chip_number = 987654
# print(angela.__chip_number)
varmint_village = PettingZoo("Varmint Village", "critters that like to dig and scour")
# marsh_madness = Wetlands("Marsh Madness")
# noodle_town = SnakePit("Noodle Town")

# varmint_village.house_animal(jim)
# varmint_village.house_animal(hopper)
# varmint_village.house_animal(rufus)
# varmint_village.house_animal(miss_fuzz)
# varmint_village.house_animal(stripes)
# varmint_village.house_animal(bill)

# marsh_madness.house_animal(goldie)
# marsh_madness.house_animal(cloyster)
# marsh_madness.house_animal(sticky)
# marsh_madness.house_animal(angry)
# marsh_madness.house_animal(arms)

# noodle_town.house_animal(sal)
# noodle_town.house_animal(majesty)
# noodle_town.house_animal(squirmy)
# noodle_town.house_animal(slithery_boy)
# noodle_town.house_animal(angela)

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
varmint_village.add_animal(bob)
for animal in varmint_village.animals:
    print(animal)
# bob.run()
# bob.swim()
# print(bob)