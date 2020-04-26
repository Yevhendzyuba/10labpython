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
        1_parfume = Parfumes(145, 567)
        2_parfume = Parfumes(250, 1240, "casablanca", "so-so", "France", 2018)
        3_parfume = Parfumes(345, 2560, "channel", "luxury", "Italy", 2020)
        objects = [1_parfume, 2_parfume, 3_parfume]
        for x in objects:
            print(x)
            print("hello world")
            print(x)
