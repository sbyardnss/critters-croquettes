from datetime import date

class Goat:
    def __init__(self, name, species):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True


jim = Goat("Jim", "goat")
print(jim)