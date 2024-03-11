# 3.1 Växter
# Växter kan beskrivas med hjälp av klasser och arv. Definiera några olika växter
# utgående från superklassen Vaxter. Ta gärna med några mellanklasser som t.ex. Blommor,
# Buskar, Gronsaker m.fl. Vaxter har en metod farg som talar om vilken färg som växten
# förknippas med (blomman, bären etc.) Ta med de instansvariabler och metoder du anser
# nödvändiga och tänk på inkapsling och arv.

# Skapa ett testprogram som deklarerar en lista med ett antal växter och sedan skriver
# ut växternas namn och färg.


class Plant(object):
    def __init__(self, color="white"):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def __str__(self):
        return f"Color: {self.color}"


class Flower(Plant):
    def __init__(self, name, color="white"):
        super().__init__(color)
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return_string = f"Color: {self.color} \nName: {self.name}"
        return return_string


class Vegetable(Plant):
    def __init__(self, name, color="white", planting_period="Not set"):
        super().__init__(color)
        self.__name = name
        self.__planting_period = planting_period

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def planting_period(self):
        return self.__planting_period

    @planting_period.setter
    def planting_period(self, period):
        self.__planting_period = period

    def __str__(self):
        return_string = f"Color: {self.color} \nName: {self.name}\nPlanting period: {self.planting_period}"
        return return_string


plant = Plant()
plant.color = "Red"
print(plant)

flower = Flower(color="White", name="Daisy")
print(flower)

vegetable = Vegetable(color="Green", name="Pea", planting_period="Summer")
print(vegetable)
