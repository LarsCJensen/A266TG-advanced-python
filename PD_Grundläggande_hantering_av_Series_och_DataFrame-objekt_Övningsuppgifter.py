#!/usr/bin/env python
# coding: utf-8

# **********************************************************************************************************************
# ### Övningsuppgifter och lösningsförslag - Grundläggande hantering av Series- och DataFrame-objekt.
# **********************************************************************************************************************

import pandas as pd
import numpy as np

# **********************************************************************************************************************
# Uppgift 1:

# Skapa ett Series-objekt med namnet 'artiklar' som innehåller kolumnen 'Artikel' i nedanstående
# DataFrame-objekt. Visa två olika sätt som detta kan göras på. Metoderna iloc och loc får inte användas

dict_data = {
    "Artikelnummer": ["100-100", "100-101", "100-102"],
    "Artikel": ["Skruv", "Mutter", "Bricka"],
    "Pris": [
        10.25,
        9.60,
        6.30,
    ],
}


artikel_data = pd.DataFrame(dict_data)

# Lösning:
artikel_1 = artikel_data["Artikel"]
artikel_2 = artikel_data.Artikel

# **********************************************************************************************************************
# Uppgift 2:

# Skapa ett DataFrame-objekt med innehåller första och sista kolumnen i DataFrame-objektet 'artikel_data'.
# Metoderna iloc och loc får inte användas:

dict_data = {
    "Artikelnummer": ["100-100", "100-101", "100-102"],
    "Artikel": ["Skruv", "Mutter", "Bricka"],
    "Pris": [
        10.25,
        9.60,
        6.30,
    ],
}  # skapa ett strängindexerat fält

artikel_data = pd.DataFrame(dict_data)

# Lösning:
df = artikel_data[["Artikelnummer", "Pris"]]
# **********************************************************************************************************************
# Uppgift 3:

# Skriv ut rad 2 och 4 i nedanstående Series-objekt med metoden 'iloc' OCH med metoden 'loc'.
# Vad är skillnaden mellan dessa två metoder?

ds = pd.Series(["Ett", 2, 3, "Fyra"], index=["A", "B", "C", "D"])

# Lösning:
print(ds.iloc[[1, 3]])
print(ds.loc[["B", "D"]])

# **********************************************************************************************************************
# Uppgift 4:

# Skriv ut rad 1 till och med rad 3 i nedanstående Series-objekt med metoden 'iloc' OCH med metoden 'loc'.
# Kolontecknet ska användas i hakparentesen hos iloc och loc.
# Notera, precis som för uppgift 3, skillnaden i indexeringsmetoder mellan dessa båda metoder!

ds = pd.Series(["Ett", 2, 3, "Fyra"], index=["A", "B", "C", "D"])

# Lösning:
print(ds.iloc[0:3,])
print(ds.loc["A":"C",])

# **********************************************************************************************************************
# Uppgift 5:

# Skapa ett DataFrame-objekt med namnet 'data' som innehåller kolumn 1 och kolumn 2 i DataFrame-objektet
# 'artikel_data' nedan. Metoden loc ska användas.

dict_data = {
    "Artikelnummer": ["100-100", "100-101", "100-102"],
    "Artikel": ["Skruv", "Mutter", "Bricka"],
    "Pris": [
        10.25,
        9.60,
        6.30,
    ],
}  # skapa ett strängindexerat fält

artikel_data = pd.DataFrame(dict_data)

# Lösning:
data = artikel_data.loc[:, "Artikelnummer":"Artikel"]

# **********************************************************************************************************************
# Uppgift 6:

# Skriv ut priset för artikelnummer '100-100' och 100-102 från 'artikel_data' nedan.
# Artikelnumren ska finnas med i svaret.

# Uppgiften ska lösas med både iloc och loc.

dict_data = {
    "Artikelnummer": ["100-100", "100-101", "100-102"],
    "Artikel": ["Skruv", "Mutter", "Bricka"],
    "Pris": [
        10.25,
        9.60,
        6.30,
    ],
}  # skapa ett strängindexerat fält

artikel_data = pd.DataFrame(dict_data)

# Lösning:
print(artikel_data.iloc[[0, 2], [0, 2]])
print(artikel_data.loc[[0, 2], ["Artikelnummer", "Pris"]])

# **********************************************************************************************************************
# Uppgift 7:

# Skriv ut raderna som tillhör artiklarna '100-100 och 100-101 med hjälp av metoden loc.
# Lös uppgiften genom att a) använda en lista som inargument till loc och b) använda kolontecknet inuti
# hakparentesen i loc-argumentet.

dict_data = {
    "Artikelnummer": ["100-100", "100-101", "100-102"],
    "Artikel": ["Skruv", "Mutter", "Bricka"],
    "Pris": [
        10.25,
        9.60,
        6.30,
    ],
}  # skapa ett strängindexerat fält

artikel_data = pd.DataFrame(dict_data)

# Lösning:
# a
print(artikel_data.loc[[0, 1]])
# b
print(artikel_data.loc[0:1])
# **********************************************************************************************************************
# Uppgift 8:

# Skriv ett program som ändrar innehållet i 3:e raden i nedanstående Series-objekt från 3 till 'tre'

ds = pd.Series([1, 2, 3, 4, 5])

# Lösning:
ds[2] = "tre"
print(ds.values)

# **********************************************************************************************************************
# Uppgift 9:

# Skapa ett Series-objekt 'ds_artikel' bestående av innehållet i kolumnen 'Artikel' i DataFrame-objektet
# 'artikel_data'

dict_data = {
    "Artikelnummer": ["100-100", "100-101", "100-102"],
    "Artikel": ["Skruv", "Mutter", "Bricka"],
    "Pris": [
        10.25,
        9.60,
        6.30,
    ],
}  # skapa ett strängindexerat fält


artikel_data = pd.DataFrame(dict_data)

# Lösning:
ds_artikel = artikel_data["Artikel"]
print(ds_artikel)

# **********************************************************************************************************************
# Uppgift 10:

# Skriv ett program som adderar, subtraherar, multiplicerar dividerar två Series-objekt ds_1 och ds_2, där
# ds_1 ska innehålla flyttalen [-1.2, 4, 6.6, 3.9, 12.3] och ds_2 ska innehålla flytttalen
# [3.3, 4.9,-11.6, 14.0, 2.12]

# Reflektera över vilka element som beräkningarna utförs på.

# Lösning:
ds_1 = pd.Series([-1.2, 4, 6.6, 3.9, 12.3])
ds_2 = pd.Series([3.3, 4.9, -11.6, 14.0, 2.12])

add = ds_1 + ds_2
print(add)
subtr = ds_1 - ds_2
print(subtr)
mult = ds_1 * ds_2
print(mult)

# **********************************************************************************************************************
# Uppgift 11:

# Skapa ett DataFrame-objekt 'df_data' bestående av ds_1 och ds_2 nedan. Skapa därefter en ny kolumn
# i 'df_data' som innehåller medelvärdet av elementen i två kolumnerna. Kolumnerna i 'df_data' ska heta
# 'K1', 'K2' och 'Medel'. Använd metoden 'mean()'.

ds_1 = pd.Series([-1.2, 4, 6.6, 3.9, 12.3])
ds_2 = pd.Series([3.3, 4.9, -11.6, 14.0, 2.12])

# Lösning:
ds = pd.concat([ds_1, ds_2], axis=1)
df_data = pd.DataFrame(ds)
df_data.columns = ["K1", "K2"]
df_data["Medel"] = df_data.mean(axis=1)
print(df_data)

# **********************************************************************************************************************
# Uppgift 12:

# Skriv EN programrad som multiplicerar vartannat värde i Series-objektet 'ds_data' med 2. For-loop får ej
# användas.

ds_data = pd.Series([1, 2, 3, 4, 5, 6])

# Lösning:
res = ds_data[1::2] * 2
# ds_data=ds_data*[1,2,1,2,1,2]
print(res)

# **********************************************************************************************************************
# Uppgift 13:

# Skriv ett program som beräknar medelvärde-, minsta-, största- och standardavvikelse per rad och
# kolumn för nedanstående DataFrame-objekt. Nya rader och kolumner ska skapas som innehåller de
# beräknade storheterna.

df_data = pd.DataFrame([[-1, -6, -7, -5], [-7, -6, -6, -1], [9, -5, -10, -9]])

# Lösning:
# Expanding a dataframe is expensive so instead we create a new list of values to
# create a new dataframe from
df_data_list = df_data.values.tolist()
df_data_list.append(df_data.mean(axis=0).values.tolist())
df_data_list.append(df_data.max(axis=0).values.tolist())
df_data_list.append(df_data.min(axis=0).values.tolist())
df_data_list.append(df_data.std(axis=0).values.tolist())

new_df_data = pd.DataFrame(df_data_list)

# mean per row
new_df_data["K_mean"] = df_data.mean(axis=1)
# max per row
new_df_data["K_max"] = df_data.max(axis=1)
# min per row
new_df_data["K_min"] = df_data.min(axis=1)
# std per row
new_df_data["K_std"] = df_data.std(axis=1)

new_df_data.index = ["R1", "R2", "R3", "R_mean", "R_min", "R_max", "R_std"]
new_df_data.columns = ["K1", "K2", "K3", "K4", "K_mean", "K_min", "K_max", "K_std"]
print(new_df_data)
# **********************************************************************************************************************
# Uppgift 14:

# Hur många gånger förekommer varje siffra i 'rad1' och 'rad2' i DataFrame-objektet 'df_data'?
# Lösningen ska utföras med medoden 'value_counts'.

df_data = pd.DataFrame(
    [[1, 2, 3, 3, 3, 4, 4, 5], [10, 10, 10, 20, 30, 30, 40, 40]], index=["rad1", "rad2"]
)

# Lösning:
print(df_data.loc["rad1"].value_counts())
print(df_data.loc["rad2"].value_counts())

# **********************************************************************************************************************
# Uppgift 15.

# Skriv ett program som sammanfogar (stackar) 'ds_1' och 'ds_2' 1) vertikalt, 2) horisontellt.
# Vilka datatyper får resultaten?

ds_1 = pd.Series([1, 2, 3, 4, 5, 6])
ds_2 = pd.Series(list("abcdef"))

# Lösning:
# Type == DataFrame
print(
    f"Horizontally: {pd.concat([ds_1, ds_2], axis=1)} \n Type={type(pd.concat([ds_1, ds_2], axis=1))}"
)

# Type == Series
print(
    f"Vertically: {pd.concat([ds_1, ds_2], axis=0)} \n Type={type(pd.concat([ds_1, ds_2], axis=0))}"
)

# **********************************************************************************************************************
# Uppgift 16.

# Skriv ett program som stryker alla rader som innehåller bokstaven 'A' i DataFrame-objektet 'df_1' och sparar
# resultatet i en nytt DataFrane-objekt 'df_2'.

df_1 = pd.DataFrame(
    [[1, "A"], [2, "B"], [3, "A"], [4, "C"], [3, "A"], [4, "D"]], columns=["K1", "K2"]
)


# Lösning:
# Return the contents of the index which matches the filter (!= "A")
df_2 = df_1[df_1["K2"] != "A"]
print(df_2)
# **********************************************************************************************************************
