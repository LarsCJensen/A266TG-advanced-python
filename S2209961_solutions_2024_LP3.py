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
    # Only allow up to three countries to be added to the list or break loop if
    # user inputs "END"
    i = 0
    while i < max_countries:
        # TODO Perhaps case insensitive
        country = input(
            "Write a country to show inflation for or exit using command 'END': "
        )
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


def choose_year():
    while True:
        year = input("Select a year to show inflation numbers for: ")
        # We need to make sure that the year is in the columns (excluding "Landskod")
        if year in df_cpi.columns:
            return year
        else:
            print(f"Year {year} does not exist in the data, please try again")


def get_inflation_values_for_year(year, number_of_values):
    # Get inflation values exluding the ones with NaN values
    inflation_values = df_cpi[year].dropna().sort_values()
    # sort values
    highest_inflation_values = inflation_values[-number_of_values:]
    lowest_inflation_values = inflation_values[:number_of_values]
    # Create name + inflation DataFrame and sort according to inflation
    return pd.concat([highest_inflation_values, lowest_inflation_values]).sort_values()


def print_inflation_values(year, inflation_values):
    print("=" * 100)
    print("LÄNDER MED HÖGST OCH LÄGST INFLATION")
    print("{:^100}".format(f"ÅR {year}"))
    print("-" * 138)
    print("{:>20}".format("Lägst") + "{:>50}".format("Högst"))
    print("{:>20}".format("-" * 5) + "{:>50}".format("-" * 5))
    # PRINT full country name
    print(
        "<{:30}>".format("Land")
        + "<{:^20}>".format("Inflation [%]")
        + "<{:50}>".format("Land")
        + "<{:^20}>".format("Inflation [%]")
    )
    print("-" * 138)
    # Loop over items to get country-code and value
    # TODO SKapa array av strängar att loopa över
    str_array = []
    # for country_code, value in inflation_values.items():
    # Use this value to offset the print mechanism
    print_step_value = int(inflation_values.size / 2)
    for i in range(print_step_value):
        country_code = inflation_values.index[i]
        inflation_value = inflation_values.iloc[i]
        country_name = df_regions[df_regions["Landskod"] == country_code]["Land"]
        # If country name couldn't be found for the country code, use that instead.
        if country_name.size == 0:
            print(
                f"""Country name for country code {country_code}
                    could not be found. Using country code instead."""
            )
            country_name = country_code
        # Print lowest and highest on the same row according to the assignment spec
        country_code2 = inflation_values.index[i + print_step_value]
        inflation_value2 = inflation_values.iloc[i + print_step_value]
        country_name2 = df_regions[df_regions["Landskod"] == country_code2]["Land"]
        if country_name2.size == 0:
            print(
                f"""Country name for country code {country_code2}
                    could not be found. Using country code instead."""
            )
            country_name2 = country_code
        # TODO Ta bort ">"
        print(
            "<{:30}>".format(country_name.array[0])
            + "<{:^20.1f}>".format(inflation_value)
            + "<{:50}>".format(country_name2.array[0])
            + "<{:^20.1f}>".format(inflation_value2)
        )


def plot_inflation_values(year, inflation_values):
    plt.title(f"De lägsta och högsta inflationerna uppmätta år {year}")
    plt.ylabel("Förändring[%]")
    plt.grid()

    countries_list = []
    for country_code in inflation_values.index:
        # Get country name from df_regions based on country code
        country_name = df_regions[df_regions["Landskod"] == country_code]["Land"]
        if country_name.size == 0:
            print(
                f"""Country name for country code {country_code}
                    could not be found. Using country code instead."""
            )
            country_name = country_code
        countries_list.append(country_name.array[0])

    plt.bar(countries_list, inflation_values.values.tolist())
    plt.show()


# year = choose_year()
# inflation_values = get_inflation_values_for_year(year=year, number_of_values=6)
# print_inflation_values(year=year, inflation_values=inflation_values)
# plot_inflation_values(year=year, inflation_values=inflation_values)
# print("Done")

# ------------------------------------------------------------------------------------------------------------------------
# Uppgift 4
# ------------------------------------------------------------------------------------------------------------------------
# Skriv din kod här:
# TODO TA BORT
# I denna uppgift ska du analysera inflationen som har uppmätts per kontinent under tidsperioden
# 1960-2022 enligt den uppdelning som finns i kolumnen Kontinent i df_region.
# Skriv ett program som använder informationen i df_cpi och df_region och som skapar en tabell som dels presenterar
# medelinflationen per kontinent under tidsperioden 1960-2022 samt de 3 högsta- och de 3 lägsta
# förekommande inflationerna per kontinent under tidsperioden och i vilka länder dessa inflationer
# uppmättes.


def get_region_inflation_values():
    # Gruppera values per region
    # I utskriften ta de tre högsta och tre lägsta samt medel
    region_group = df_regions.groupby(["Kontinent"])
    for region_name, group in region_group:
        print(region_name)
        print(group)
        region_values = df_cpi[df_cpi.index.isin(group["Landskod"])]
    # Första kolumnen
    test = df_cpi.iloc[:, :0]
    pass


def plot_header():
    pass


region_inflation_values = get_region_inflation_values()

plot_header()
plot_regional_inflation_values()


# ------------------------------------------------------------------------------------------------------------------------
# Uppgift 5
# ------------------------------------------------------------------------------------------------------------------------
# Skriv din kod här:


# ------------------------------------------------------------------------------------------------------------------------
# Uppgift 6
# ------------------------------------------------------------------------------------------------------------------------
# Skriv din kod här:
