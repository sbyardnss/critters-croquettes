from datetime import date

class GardenSnake:
    """slithering instance"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


squirmy = GardenSnake("Squirmy", "garden snake")
print(squirmy)
