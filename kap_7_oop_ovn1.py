# 1.1 Klassen Film
# Definiera klassen Film som innehåller information om en film. Filmen har en titel,
# namnet på en regissör, en längd i minuter, namnet på en huvudrollsinnehavare och ett
# biljettpris. Det skall gå att skapa nya filmer med alla uppgifter inkluderade direkt
# men det behövs inga metoder för att ändra dem. Det skall också gå att skriva ut alla
# filmer med dess kompletta information.

# 1.2 Klassen Person
# Definiera klassen Person som innehåller information om en person. Personen har ett förnamn,
# ett efternamn, ett födelseår och en längd. Det skall gå att skapa nya personer med
# alla uppgifter inkluderade direkt men de behöver ännu inga metoder för att ändra dem.
# Det skall också gå att skriva ut alla personer med dess kompletta information.

# Skriv ett testprogram som skapar ett antal personer och skriver ut informationen om dem igen på ett lättläst sätt.

# Du får lösa uppgiften på valfritt sätt utan att tänka på inkapsling, säkerhet vid inmatning, egenskaper m.m.

# 1.3 Koppla ihop Film och Person
# Uppdatera nu klassen Film så att regissör och huvudrollsinnehavare är personer från klassen Person.

# Skriv ett testprogram som skapar ett antal personer och ett antal filmer. Skriv ut informationen om filmerna på ett lättläst sätt.

# Du får lösa uppgiften på valfritt sätt utan att tänka på inkapsling, säkerhet vid inmatning, egenskaper m.m.

# 1.4 Komplettera klasserna Film & Person.
# Priset är beroende av efterfrågan. Komplettera klassen film med en metod för att ändra
# biljettpriset. Metoden ska kontrollera att ändringen är rimlig (< +/- 10%) annars ska
# ett felmeddelande ges.

# En person växer, komplettera klassen Person med en metod för att ändra längden. Metoden ska kontrollera att längden är rimlig (mellan 30 cm och 2 meter) annars ska ett felmeddelande ges.


class Person:
    def __init__(self, first_name, sir_name, year_of_birth, height):
        self._first_name = first_name
        self._sir_name = sir_name
        self._year_of_birth = year_of_birth
        self._height = height

    def __str__(self):
        return (
            f"{self._first_name} {self._sir_name} "
            f"Födelseår: {self._year_of_birth} Längd: {self._height}"
        )


# 1.1 Svar
class Film:
    def __init__(self, title, director, length, main_actor, price):
        self._title = title
        self._director = director
        self._length = length
        self._main_actor = main_actor
        self._price = price

    def __str__(self):
        return (
            "Film information: \n"
            f"\t Title: {self._title} \n"
            f"\t Director : {self._director} \n"
            f"\t Length: {self._length} \n"
            f"\t Main actor: {self._main_actor} \n"
            f"\t Price: {self._price}"
        )

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if (value > (self._price * 0.9)) and value < (self._price * 1.1):
            self._price = value
        else:
            print("Value is above/below 10% increase/decrease!")


if __name__ == "__main__":
    director = Person(
        first_name="Kalle", sir_name="Svensson", year_of_birth=1987, height=174
    )
    actor = Person(first_name="Kim", sir_name="Scott", year_of_birth=1967, height=156)
    movie = Film(
        title="Test Title",
        director=director,
        length=123,
        main_actor=actor,
        price=321,
    )
    print(movie)
    movie.price = 354
