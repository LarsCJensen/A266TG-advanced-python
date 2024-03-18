import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# uppgift 3:
# ----------
# a
df_cia_factbook = pd.read_csv("tentamen/cia_factbook.csv", delimiter=";")


# b
def prepare_data():
    df_cia_factbook["density"] = df_cia_factbook["population"] / df_cia_factbook["area"]
    # Remove NaN values, but first replace inf with NaN
    df_cia_factbook.replace([np.inf, -np.inf], np.nan, inplace=True)
    df_cia_factbook.dropna(axis="index", subset=["density"], inplace=True)


prepare_data()


# c
def plot_data(data):
    # If the lowest values are chose, change title of plot
    title_order = "störst"
    if len(data) <= 5:
        title_order = "lägst"

    plt.title(f"Länder med {title_order} befolkningstäthet")
    # Rotate the X values (years) to fit
    plt.xticks(rotation=45)
    plt.ylabel("Befolkningstäthet [inv/km2]")
    plt.grid()

    # years = df_cpi.columns
    # cpi_values = df_cpi.loc[country_code]
    # change_factor_values = _get_change_factor_values(cpi_values)
    plt.bar(data["country"], data["density"])
    plt.show()


def get_data_to_plot(number):
    if number <= 5:
        sorted_vals = df_cia_factbook.sort_values(by="density", ascending=True)
        # matar man in 5- ska de fem länderna med lägst befolkningstäthet plottas osv
    else:
        # Matar man in 7+ ska de sju länderna med störst befolkningstäthet plottas i stapeldiagramme
        sorted_vals = df_cia_factbook.sort_values(by="density", ascending=False)
    # Only return needed data
    return sorted_vals[:number][["country", "density"]]


def assignment_3b():
    while True:
        num_of_countries = input(
            "Ange antal länder du vill plotta befolkningstäthet för, eller ange ett land: "
        )
        try:
            if int(num_of_countries) <= 10 and int(num_of_countries) > 0:
                data = get_data_to_plot(int(num_of_countries))
                plot_data(data)
                input("Tryck Enter för att fortsätta..")
                break
            else:
                print("Välj en siffra mellan 1 och 10")
        except ValueError:
            # If you input strings, validate that the country exits
            value = df_cia_factbook[df_cia_factbook["country"] == num_of_countries][
                "density"
            ]
            if not len(value):
                print(
                    f"Det finns inget data för landet {num_of_countries}, försök igen!"
                )
                continue
            print(f"Befolkningstätheten för {num_of_countries} är {value.values[0]}")


def _get_country_data():
    mean_pop = df_cia_factbook["population"].mean()
    mean_area = df_cia_factbook["area"].mean()
    mean_birth_rate = df_cia_factbook["birth_rate"].mean()
    mean_life_exp_at_birth = df_cia_factbook["life_exp_at_birth"].mean()

    country_data_filter = (
        (df_cia_factbook["population"] > mean_pop)
        & (df_cia_factbook["area"] > mean_area)
        & (df_cia_factbook["birth_rate"] > mean_birth_rate)
        & (df_cia_factbook["life_exp_at_birth"] > mean_life_exp_at_birth)
    )

    contry_data = df_cia_factbook.loc[
        country_data_filter, ["country", "area", "birth_rate", "life_exp_at_birth"]
    ]
    return country_data


def _print_header():
    print("Land\tArea[km2]\tAntal födslar[per 1000 inf]\tLivslängd[år]")
    print("-" * 75)


def print_country_info():
    # print country, area, birth_rate och life_exp_at_birth
    country_data = _get_country_data()
    _print_header()


def assignment_3c():
    while True:
        print(
            "Välj mellan följande alternativ\n1. Visa statistik\n2. Internetmognad\n3. Befolkningstrend\n4. Avsluta"
        )
        menu_choice = input("Välj funktion: ")
        try:
            if int(menu_choice) < 0 or int(menu_choice) > 4:
                print("Ogiltigt val. Försök igen!")
            else:
                if int(menu_choice) == 1:
                    print_country_info()

        except ValueError:
            print("Ogiltigt val. Försök igen!")


if __name__ == "__main__":
    while True:
        choice = input(
            "Välj mellan följande alternativ:\n1. Uppgift 3b\n2. Uppgift 3c\n"
        )

        if choice == "1":
            assignment_3b()
        elif choice == "2":
            assignment_3c()
        else:
            print("Försök igen!")
