from datetime import date

class Goat:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift


jim = Goat("Jim", "goat", "A")
print(jim)
print(f"{jim.name} is available during the {jim.shift} shift")