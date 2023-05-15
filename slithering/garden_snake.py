from datetime import date

class GardenSnake:
    def __init__(self, name, species):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True


squirmy = GardenSnake("Squirmy", "garden snake")
print(squirmy)