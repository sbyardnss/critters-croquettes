from datetime import date

class Rhino:
    def __init__(self, name, species):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.walking = True


bill = Rhino("Bill", "rhino")
print(bill)