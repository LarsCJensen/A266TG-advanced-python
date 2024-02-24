#!/usr/bin/env python
# coding: utf-8
# **********************************************************************************************************************
# Övningsuppgifter - Filtrera och gruppera data
# **********************************************************************************************************************

import pandas as pd

# **********************************************************************************************************************
# OBS! För att lösa övningsuppgifterna skall datafilen 'temp_falsterbo_froson.csv' användas. Datafilen
#     finns sparad i Canvas. Kopiera den sedan till det biblioteket där denna JN-fil finns.
#     Den innehåller temperaturdata från väderstationerna i Falsterbo och Frösön uppmätt varje dag
#     kl. 12.00 från 2018-01-01 -- 2019-12-31.
#     Nedanstående programrad läser in datat i variabeln 'temperatur_data'


temperatur_data = pd.read_csv("data/temp_falsterbo_froson.csv")

# **********************************************************************************************************************
# Uppgift 1:

# Skriv en programrad som listar antal rader och kolumner hos 'temperatur_data'

# Lösning:
print(temperatur_data.shape)

# **********************************************************************************************************************
# Uppgift 2:

# Skriv ett program som listar de första 15 raderna och de sista 15 raderna i 'temperatur_data'

# Lösning:
print(temperatur_data.iloc[0:15])
print(temperatur_data.iloc[-15:, :])
# Alternative
print(temperatur_data.head(15))
print(temperatur_data.tail(15))

# **********************************************************************************************************************
# Uppgift 3:

# Skriv ett program som gör en sammanställning av innehållet i 'temperatur_data' med avseende på antal data,
# medelvärde, min- och max- värde

# Lösning:
print(f"Count:\n{temperatur_data.describe().count()}")
print("--------------------------")
print(f"Mean:\n{temperatur_data.describe().mean()}")
print("--------------------------")
print(f"Min:\n{temperatur_data.describe().min()}")
print("--------------------------")
print(f"Max:\n{temperatur_data.describe().max()}")
print("--------------------------")


# **********************************************************************************************************************
# Uppgift 4:

# Skriv ett program som skriver ut de första två temperaturvärdena för Frösön

# Lösning:
print(temperatur_data.loc[0:1, ["Froson"]])
# alt
print(temperatur_data.iloc[0:2, [0, 3]])

# **********************************************************************************************************************
# Uppgift 5:

# Skriv ett program som skriver ut temperaturerna i Falsterbo och på Frösön under 4 slumässiga dagar.

# Lösning:
print(temperatur_data.sample(4))

# **********************************************************************************************************************
# Uppgift 6:

# Skriv ett program som listar alla temperaturer på Frösön under januari 2018.

# Lösning:
jan_filter = (temperatur_data["Datum"] >= "2018-01") & (
    temperatur_data["Datum"] < "2019-01-01"
)
date_grp = temperatur_data.loc[jan_filter, ["Datum", "Froson"]]
print(date_grp)

# **********************************************************************************************************************
# Uppgift 7:

# Skriv ett program som listar en sammanställning för temepraturen med avseende på medelvärde-, största-
# och minsta värden för Falsterbo under juli 2019.

# Lösning:
july_filter = (temperatur_data["Datum"] >= "2019-07") & (
    temperatur_data["Datum"] < "2019-08"
)
date_grp = temperatur_data.loc[july_filter, ["Datum", "Falsterbo"]]
print(date_grp.describe())

# **********************************************************************************************************************
# Uppgift 8:

# Skriv ett program som listar de dagar under 2019 när temperaturen på Frösön är högre än +25C

# Lösning:
froson_filter = (
    (temperatur_data["Datum"] >= "2019")
    & (temperatur_data["Datum"] < "2020")
    & (temperatur_data["Froson"] > 25)
)

date_grp = temperatur_data.loc[froson_filter, ["Datum", "Froson"]]
print(date_grp)
# **********************************************************************************************************************
# Uppgift 9:

# Skriv ett program som listar de dagar under maj, juni, juli, augusti år 2019 när temperaturen på Frösön
# är högre än temperaturen i Falsterbo.

# Lösning:
froson_compare_filter = (
    (temperatur_data["Datum"] >= "2019-05")
    & (temperatur_data["Datum"] < "2019-09")
    & (temperatur_data["Froson"] > temperatur_data["Falsterbo"])
)

date_grp = temperatur_data.loc[froson_filter, ["Datum", "Falsterbo", "Froson"]]
print(date_grp)
# **********************************************************************************************************************
# Uppgift 10:

# Hur många grader skiljde sig medeltemperaturen mellan Fröson och Falsterbo under december månad 2018?

# Lösning:
dec_filter = (temperatur_data["Datum"] >= "2018-12") & (
    temperatur_data["Datum"] < "2019"
)

date_grp = temperatur_data.loc[dec_filter]
dec_diff = date_grp["Froson"].mean() - date_grp["Falsterbo"].mean()
print(dec_diff)

# **********************************************************************************************************************
# Uppgift 11:

# Skriv ett program som elementvis jämför nedanstående Series-objekt oh skriver ut 1) identiska element
# 2) de element i 'ds_1' som är större än elementen i 'ds_2', 3) de element som är olika

ds_1 = pd.Series([2, 3, 6, 4, 10])
ds_2 = pd.Series([1, 3, 5, 7, 10])

# Lösning:
# a
print(ds_1[ds_1 == ds_2])
# b
print(ds_1[ds_1 > ds_2])
# c
print(ds_1[ds_1 != ds_2])
# **********************************************************************************************************************
# Uppgift 12:

# Nedanstående strängindexerat fält innehåller resultatet från en försökserie med 4 olika preparat
# 'A', 'B', 'C' och deras uppmätta styrka. 1) Skapa ett DataFrame-objekt av det strängindexerade
# fältet och gruppera resultaten och 2) beräkna och skriv ut medelvärde, standardaavikelse, minsta- och
# största värde för varje preparat. Utifrån det beräknade resultet är det något/några värden som
# 'sticker ut'? Ge i så fall en möjlig förklaring.

test_serie = {
    "Preparat": ["A", "C", "B", "B", "A", "C", "B", "C", "A", "C", "C", "B", "A", "B"],
    "Styrka": [12.4, 5.3, 9.2, 8.9, 3.1, 6.4, 10.1, 5.9, 1.8, 4.9, 5.6, 9.0, 1.9, 8.6],
}
print(test_serie)

# Lösning:
# a
test_df = pd.DataFrame(test_serie)
prep_grp = test_df.groupby(["Preparat"])
# b
print(prep_grp.get_group(("A",)).describe())
print(prep_grp.get_group(("B",)).describe())
print(prep_grp.get_group(("C",)).describe())
# **********************************************************************************************************************

# Uppgift 13:

# Skriv ett program som byter ut alla 'A' i DataFrame-objektet 'df' mot 'Ö' och  4 mot 40.

df = pd.DataFrame(
    [[1, "A"], [2, "B"], [3, "A"], [4, "C"], [3, "A"], [4, "D"]], columns=["K1", "K2"]
)

# Lösning:
print(df)
df.replace("A", "Ö", inplace=True)
df.replace(4, 40, inplace=True)
print(df)

# **********************************************************************************************************************

# Uppgift 14:

# Skriv ett program som stryker alla rader som innehåller bokstaven 'A' i DataFrame-objektet 'df_1' och sparar
# resultatet i en nytt DataFrane-objekt 'df_2'.

df_1 = pd.DataFrame(
    [[1, "A"], [2, "B"], [3, "A"], [4, "C"], [3, "A"], [4, "D"]], columns=["K1", "K2"]
)

# Lösning:
print(df_1)
df_1.replace("A", None, inplace=True)
df_2 = df_1.dropna()
# alt
df_2 = df_1[df_1["K2"] != "A"]
print(df_2)
# **********************************************************************************************************************
