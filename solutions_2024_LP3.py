import matplotlib.pyplot as plt
import pandas as pd
import typing

# ------------------------------------------------------------------------------------------------------------------------
# Uppgift 1
# ------------------------------------------------------------------------------------------------------------------------
# Skriv din kod här:

# Add Landskod as index to make it easy to find values for countries
df_cpi = pd.read_csv(r"data/cpi.csv", delimiter=";", index_col="Landskod")
# TODO Should landskod be indexed?
df_regions = pd.read_csv(r"data/regions.csv", delimiter=";")
df_inflation = pd.read_csv(r"data/inflation.csv")


# ------------------------------------------------------------------------------------------------------------------------
# Uppgift 2
# ------------------------------------------------------------------------------------------------------------------------
# Skriv din kod här:
# A


def choose_countries():
    max_countries = 3
    countries = {}
    # Only allow up to three countries to be added to the list
    i = 0
    while i < max_countries:
        # TODO Perhaps case insensitive
        country = input("Write a country to show inflation for: ")
        if country == "END":
            # Exit loop
            break
        if country in df_regions.values:
            # Extract the country code and append it to the list. It will be matched
            # against the entires in the cpi file
            # TODO is there a better way?
            countries[country] = df_regions[df_regions["Land"] == country][
                "Landskod"
            ].to_list()[0]
            # Only increment the counter when a valid country is chosen
            i += 1
        else:
            print(f"Country {country} does not exist in the data, please try again")
    return countries


def plot_countries(countries):
    plt.title("Årlig inflationstakt under åren 1960-2022")
    plt.xlabel("År")
    # Rotate the X values (years) to fit
    plt.xticks(rotation=90)
    plt.ylabel("Inflationstakt [%]")
    plt.grid()

    for country, country_code in countries.items():
        # Get columns with years for x-lim
        # years = df_cpi.columns[1:]
        years = df_cpi.columns
        # Extract yearly values for country
        # TODO Kolla
        # cpi_values = df_cpi[df_cpi["Landskod"] == country_code].iloc[:1, 1:].values[0]
        cpi_values = df_cpi.loc[country_code]
        # Get max and min values and which year they belong to
        cpi_max = cpi_values.max()
        cpi_max_year = years[cpi_values.argmax()]
        cpi_min = cpi_values.min()
        cpi_min_year = years[cpi_values.argmin()]
        plt.plot(years, cpi_values, label=f"{country}")
        # Create circles for the max and min
        # TODO Gör snyggare
        max_circle = plt.Circle((cpi_max_year, cpi_max), 0.1, color="r")
        min_circle = plt.Circle((cpi_min_year, cpi_min), 0.1, color="b")
        # Get current axis and add circles to it as patch
        plt.gca().add_patch(max_circle)
        plt.gca().add_patch(min_circle)

    plt.legend()
    plt.show()


# countries = choose_countries()
# plot_countries(countries)


# 2B


def choose_country():
    while True:
        # TODO Perhaps case insensitive
        country = input("Write a country to show change factor for: ")
        if country in df_regions.values:
            # Extract the country code and append it to the list. It will be matched
            # against the entires in the cpi file
            # TODO is there a better way?
            country_code = df_regions[df_regions["Land"] == country][
                "Landskod"
            ].to_list()[0]
            break
        else:
            print(f"Country {country} does not exist in the data, please try again")
    return country, country_code


# Helper method to calculate change factor
def _get_change_factor(this_month, prev_month):
    # Return in percent
    return ((this_month - prev_month) / prev_month) * 100


def _get_change_factor_values(cpi_values):
    prev_val = 0
    change_factor_values = []
    for i in range(cpi_values.size):
        if i == 0:
            # If i == 0 then we are at the first month, so no diff can be calculated
            prev_val = cpi_values[i]
            # Add value of 0 to keep length of values the same as number of years
            change_factor_values.append(0)
            continue
        change_factor_values.append(_get_change_factor(cpi_values[i], prev_val))
        prev_val = cpi_values[i]
    return change_factor_values


def plot_change_factor(country, country_code):
    # TODO Gör generell
    plt.title(
        f"{country} - förändring av inflation i förhållande till föregående år (1960-2022)"
    )
    plt.xlabel("År")
    # Rotate the X values (years) to fit
    plt.xticks(rotation=90)
    plt.ylabel("Inflationstakt [%]")
    plt.grid()

    years = df_cpi.columns
    # cpi_values = df_cpi[df_cpi["Landskod"] == country_code].iloc[:1, 1:].values[0]
    cpi_values = df_cpi.loc[country_code]
    change_factor_values = _get_change_factor_values(cpi_values)
    plt.bar(years, change_factor_values, label=f"{country}")
    plt.show()


# country, country_code = choose_country()
# plot_change_factor(country, country_code)

# ------------------------------------------------------------------------------------------------------------------------
# Uppgift 3
# ------------------------------------------------------------------------------------------------------------------------
# Skriv din kod här:
# TODO TA BORT
# Skriv ett program där man först anger årtalet som ska analyseras och därefter beräknar programmet
# de 6 länder som hade lägst respektive högst inflation för året ifråga. Informationen ska presenteras i
# tabellform och i ett stapeldiagram enligt nedansteånde utseenden. Vi bortser från de länder som
# inte rapporterat inflationen för året i fråga.
# Nedan visas en körning av programmet:


def choose_year():
    while True:
        year = input("Select a year to show inflation numbers for: ")
        # We need to make sure that the year is in the columns (excluding "Landskod")
        if year in df_cpi.columns:
            return year
        else:
            print(f"Year {year} does not exist in the data, please try again")


def get_inflation_values_for_year(year):
    # Get inflation values exluding the ones with NaN values
    inflation_values = df_cpi[year].dropna()
    # sort values
    highest_inflation_values = inflation_values.sort_values()[-6:]
    lowest_inflation_values = inflation_values.sort_values()[:6]
    # Create name + inflation
    return pd.concat([highest_inflation_values, lowest_inflation_values])


def print_inflation_values(year, inflation_values):
    print("=" * 100)
    print("LÄNDER MED HÖGST OCH LÄGST INFLATION")
    print("{:^15}".format(f"ÅR {year}"))
    print("-" * 100)
    print("{:>15}".format("Lägst") + "{:>20}".format("Högst"))
    print("{:>15}".format("-" * 5) + "{:>20}".format("-" * 5))
    # PRINT full country name
    print(
        "{:20}<".format("Land")
        + "{:>20}>".format("Inflation [%]")
        + "{:20}<".format("Land")
        + "{:>20}>".format("Inflation [%]")
    )
    # Loop over items to get country-code and value
    for country_code, value in inflation_values.items():
        country_name = df_regions[df_regions["Landskod"] == country_code]["Land"]
        print("{:20}<".format(country_name) + "{:>20}>".format(value))


year = choose_year()
inflation_values = get_inflation_values_for_year(year)
print_inflation_values(year, inflation_values)


# ------------------------------------------------------------------------------------------------------------------------
# Uppgift 4
# ------------------------------------------------------------------------------------------------------------------------
# Skriv din kod här:


# ------------------------------------------------------------------------------------------------------------------------
# Uppgift 5
# ------------------------------------------------------------------------------------------------------------------------
# Skriv din kod här:


# ------------------------------------------------------------------------------------------------------------------------
# Uppgift 6
# ------------------------------------------------------------------------------------------------------------------------
# Skriv din kod här:
