from datetime import date

class Octopus:
    def __init__(self, name, species):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True


arms = Octopus("Arms", "octopus")
print(arms)