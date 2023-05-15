from datetime import date


class Llama:
    def __init__(self):
        self.name = ""
        self.species = ""
        self.date_added = date.today()


miss_fuzz = Llama()
miss_fuzz.name = "Miss Fuzz"
miss_fuzz.species = "domestic llama"
miss_fuzz.walking = True
print(miss_fuzz)