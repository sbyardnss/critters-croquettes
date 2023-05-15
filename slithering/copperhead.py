from datetime import date

class Copperhead:
    def __init__(self, name, species):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.slithering = True


slithery_boy = Copperhead("Slithery Boy", "copperhead")
print(slithery_boy)