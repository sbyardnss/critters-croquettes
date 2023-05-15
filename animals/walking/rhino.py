from datetime import date

class Rhino:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
    def __str__(self):
        return f'{self.name} is a {self.species}'


# bill = Rhino("Bill", "rhino", "B", "grass")
# print(bill)