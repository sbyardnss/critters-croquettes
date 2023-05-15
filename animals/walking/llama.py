from datetime import date


class Llama:
    """llama"""
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food
    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today().strftime('%m/%d/%Y')}")
    def __repr__(self):
        return f'{self.__class__.__name__}: ({self.name}, {self.species}, {self.date_added}, {self.walking}, {self.shift}, {self.food})'


# miss_fuzz = Llama("Miss Fuzz", "domestic llama", "C", "oats")
# # print(miss_fuzz)
# # print(miss_fuzz.feed())
# print(miss_fuzz)