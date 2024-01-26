# -*- coding: utf-8 -*-

# **********************************************************************************************************************
# Övningsuppgifter och lösningsförslag till avsnittet Felhantering
# **********************************************************************************************************************

# Uppgift 1:

# Följande kod genererar en felsignal. Implementera felhantering med try-/except-block så att programmet blir körbart.
# Testa med att först fånga en specifik felsignal och sedan att fånga alla typer av felsignaler

dagar = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag"]

i = 0
while i <= 5:
    try:
        print(dagar[i])
    except IndexError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unhandled error! \nError: {e}")
    i += 1

print("Slut...")

# Lösningsförslag:


# **********************************************************************************************************************

# Uppgift 2:

# Följande kod kan generera fel beroende på vad användaren matar in.
# Implementera felhantering med try-/except-block så att programmet blir körbart oberoende av inmatning.
# Dessutom skall användaren kunna mata in data på nytt om fel uppstår.
while True:
    try:
        data1 = float(input("Ange tal 1: "))
        data2 = float(input("Ange tal 2: "))
        break
    except ValueError:
        print("The value you have given is not a number. Please try again!")

produkt = data1 * data2

print("Produkten ", data1, " * ", data2, " blir ", produkt)

print("Slut...")

# Lösningsförslag:

# **********************************************************************************************************************

# Uppgift 3:

# Koden nedan är felaktig och "buggig".
# Implementera felhantering med try-/except-block så att programmet blir körbart utan fel.
# Om en bloggpost inte har fått några 'Likes' så skall programmet lägga till värdet 0 till det totala antalet 'Likes'.

blog_posts = [
    {"Photos": 3, "Likes": 21, "Comments": 2},
    {"Likes": 13, "Comments": 2, "Shares": 1},
    {"Photos": 5, "Likes": 33, "Comments": 8, "Shares": 3},
    {"Comments": 4, "Shares": 2},
    {"Photos": 8, "Comments": 1, "Shares": 1},
    {"Photos": 3, "Likes": 19, "Comments": 3},
]

total_likes = 0

for post in blog_posts:
    try:
        total_likes = total_likes + post["Likes"]
    except KeyError:
        post["Likes"] = 0

print('Totalt antal "Likes":', total_likes)

# Lösningsförslag:

# **********************************************************************************************************************

# Uppgift 4:

# Koden nedan tar den 5:e bokstaven av varje ord i listan food och lägger till denna bokstav i den nya listan fifth. Denna kod genererar dock fel.
# Implementera felhantering med try-/except-block så att programmet blir körbart utan fel.
# Om ett ord inte är tillräckligt långt för att den 5:e bokstaven skall kunna plockas ut, så skall inget läggas till i listan fifth.
# Anmärkning: Man kan använda uttycket pass i Python om man vill ha ett uttyck i koden som inte utför något, d.v.s. pass är en null-operation och inget händer när det exekveras.

food = [
    "chocolate",
    "chicken",
    "corn",
    "sandwich",
    "soup",
    "potatoes",
    "beef",
    "lox",
    "lemonade",
]
fifth = []

for x in food:
    try:
        fifth.append(x[4])
    except IndexError:
        pass

print(fifth)

# Lösningsförslag:

# **********************************************************************************************************************

# Uppgift 5:

# Implementera felhantering i funktionen get_value().
# Om ett indexeringfel uppstår beroende på att det specifika indexet inte finns, så skall funktionen returnera None.
# I Python är None detsamma som NULL, som finns i de flesta andra programspråk. En variabel kan exempelvis tilldelas värdet None/NULL, vilket innebär den inte har något värde alls.
# Inga andra fel behöver hanteras.


def get_value(data_list, index):
    try:
        return data_list[index]
    except IndexError:
        return None


# Testkörning av funktionen
my_list = ["a", "b", "c"]

value1 = get_value(my_list, 2)
print(value1)

value2 = get_value(my_list, 4)
print(value2)

# Lösningsförslag:

# **********************************************************************************************************************


# Uppgift 6 (Kursbokens uppgift 3.39):

# Denna uppgift är hämtad från kursboken, sida 92, och lyder
# Lägg till felhanteringsrutinder i uppgift 3.36 och 3.38.
# För mer information hänvisas till kursboken, "Ingenjörens guide till Python".


# Lösningsförslag:

# **********************************************************************************************************************
