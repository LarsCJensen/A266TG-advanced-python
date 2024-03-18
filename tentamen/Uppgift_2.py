import os
import pickle

# uppgift 2:
# ----------

# a

# Global variable which hold all added computers
LIST_OF_COMPUTERS = []
DATA_FILE = f"{os.getcwd()}/dator.data"


class Dator:
    def __init__(self, maker=None, model=None, processor=None, ram=None, price=None):
        self._maker = maker
        self._model = model
        self._processor = processor
        self._ram = ram
        self._price = price

    @property
    def maker(self):
        return self._maker

    @maker.setter
    def maker(self, maker):
        self._maker = maker

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def processor(self):
        return self._processor

    @processor.setter
    def processor(self, processor):
        self._processor = processor

    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, ram):
        self._ram = ram

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    def __str__(self):
        # The string adaption follows the desired format
        str_repr = (
            "{:20}".format(self._maker)
            + "{:20}".format(self._model)
            + "{:20}".format(self._processor)
            + "{:20}".format(f"{self._ram}GB")
            + "{:>20}".format(self._price)
        )
        return str_repr


class Laptop(Dator):
    def __init__(
        self,
        maker=None,
        model=None,
        processor=None,
        ram=None,
        price=None,
        screen_size=None,
    ):
        super().__init__(
            maker=maker, model=model, processor=processor, ram=ram, price=price
        )
        self._screen_size = screen_size

    @property
    def screen_size(self):
        return self._screen_size

    @screen_size.setter
    def screen_size(self, screen_size):
        self._screen_size = screen_size

    def __str__(self):
        # The string adaption follows the desired format
        str_repr = (
            f"Tillverkare: {self._maker}\n"
            f"Modell: {self._model}\n"
            f"Processortyp: {self._processor}\n"
            f"Installerat RAM: {self._ram} GB\n"
            f"Pris: {self._price} Kr\n"
            f"Skärmstorlek: {self._screen_size} tum"
        )
        return str_repr


def _print_header():
    """ "Helper method to print header"""
    print(
        "{:20}".format("Tillverkare")
        + "{:20}".format("Modell")
        + "{:20}".format("Processortyp")
        + "{:20}".format("RAM")
        + "{:>20}".format("Pris[kr]")
    )
    print("=" * 100)


def _save_data():
    """Helper function to save data"""
    with open(DATA_FILE, "wb") as file:
        pickle.dump(LIST_OF_COMPUTERS, file)
    print("----------------------")
    print("Data är skriven till filen dator.dat")


def lista(number_of_computers):
    for _ in range(number_of_computers):
        comp = Dator()
        print("<---------- Ny dator ------------>")
        comp.maker = input("Ange tillverkare: ")
        comp.model = input("Ange modell: ")
        comp.processor = input("Ange processortyp: ")
        comp.ram = input("Ange installerad RAM (GB): ")
        # Since there is no requirement on valid input I skip error handling
        comp.price = input("Ange inköpspris: ")
        # Add computer to list
        LIST_OF_COMPUTERS.append(comp)
    _save_data()


def visa_data(data_file=None):
    if data_file:
        # Marking variable as global to be able to refer to it
        global LIST_OF_COMPUTERS
        print("<------ Using saved file ------>")
        with open(data_file, "rb") as file:
            LIST_OF_COMPUTERS = pickle.load(file)

    # If data_file is not passed in, list from memory
    # Use same functionality to display computers and
    _print_header()
    [print(comp) for comp in LIST_OF_COMPUTERS]


def add_laptop():
    laptop = Laptop(
        maker="ASUS",
        model="ExpertBook",
        processor="Core i5",
        ram="16",
        price=7990.0,
        screen_size=15.6,
    )
    print(laptop)


# I chose to implement this menu to make the code easier to test
if __name__ == "__main__":
    while True:
        print(
            "1. Lägg till datorer\n2. Visa registrerade datorer\n3. Lägg till laptop (2c)\n4. Visa sparad data (2d)\n5. Avsluta\n"
        )
        choice = input("Välj funktion att köra: ")
        if choice == "1":
            while True:
                number_of_computers = input("Hur många datorer vill du lägga till? ")
                try:
                    # Make sure input is valid
                    if int(number_of_computers) > 0:
                        lista(int(number_of_computers))
                    input("Tryck Enter för att fortsätta..")
                    break
                except ValueError:
                    print("Ogiltigt val. Försök igen!")
        elif choice == "2":
            visa_data()
            input("Tryck Enter för att fortsätta..")
        elif choice == "3":
            add_laptop()
            input("Tryck Enter för att fortsätta..")
        elif choice == "4":
            if not os.path.exists(DATA_FILE):
                # If you haven't added any computers yet, you are missing the data file
                print("Du måste först lägga till datorer att spara")
            else:
                visa_data(DATA_FILE)
                input("Tryck Enter för att fortsätta..")
        elif choice == "5":
            break
        else:
            print(f"{choice} är inget giltigt val. Försök igen!")
