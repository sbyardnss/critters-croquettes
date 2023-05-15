from datetime import date

class Anaconda:
    """slithering instance"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


angela = Anaconda("Angela", "anaconda")
print(angela)
