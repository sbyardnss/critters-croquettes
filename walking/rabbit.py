from datetime import date

class Rabbit:
    def __init__(self, name, species):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True


hopper = Rabbit("Hopper", "rabbit")
print(hopper)