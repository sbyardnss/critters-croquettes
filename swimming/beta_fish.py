from datetime import date

class BetaFish:
    def __init__(self, name, species):
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True


angry = BetaFish("Angry", "beta fish")
print(angry)