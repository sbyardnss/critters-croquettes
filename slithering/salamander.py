from datetime import date

class Salamander:
    def __init__(self, name, species):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True


sal = Salamander("Sal", "salamander")
print(sal)