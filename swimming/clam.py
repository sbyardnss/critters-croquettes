from datetime import date

class Clam:
    def __init__(self, name, species):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True


cloyster = Clam("Cloyster", "clam")
print(cloyster)