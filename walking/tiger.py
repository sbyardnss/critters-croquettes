from datetime import date

class Tiger:
    def __init__(self, name, species):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True


rufus = Tiger("Rufus", "domestic tiger")
print(rufus)
