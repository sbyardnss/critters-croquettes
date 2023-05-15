from datetime import date

class Anaconda:
    def __init__(self, name, species):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True


angela = Anaconda("Angela", "anaconda")
print(angela)