class Parfumes:
    my_str = "static field"

    def __init__(self, formatInMl=None, price=None, nameOfProducer=None, category=None, country=None,
                 yearOfMaking=None):
        self.formatInMl = formatInMl
        self.price = price
        self.nameOfProducer = nameOfProducer
        self.category = category
        self.country = country
        self.yearOfMaking = yearOfMaking

    def __del__(self):
        print("Deleted Fields:", self.formatInMl, self.price, self.nameOfProducer, self.category, self.country,
              self.yearOfMaking)
        return

    def __str__(self):
        return "Format: {} \t Price: {} \t NameOfProducer: {} \t Category: {} \t Country: {} \t YearOfMaking: {} \t " \
            .format(self.formatInMl, self.price, self.nameOfProducer, self.category, self.country,
                    self.yearOfMaking, Parfumes.my_str)

    @staticmethod
    def get_str():
        return Parfumes.my_str

    @classmethod
    def main(cls):
        first_parfume = Parfumes(145, 567)
        second_parfume = Parfumes(250, 1240, "casablanca", "so-so", "France", 2018)
        third_parfume = Parfumes(345, 2560, "channel", "luxury", "Italy", 2020)
        objects = [first_parfume, second_parfume, third_parfume]
        for x in objects:
            print(x)
