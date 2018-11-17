import json

try:
    with open("zadanie_1_baza.json") as f:
        pracownicy = json.load(f)
except FileNotFoundError:
    pracownicy = []

odp = input("Co chcesz zrobic? [d - dodaj, w - wypisz]")
if odp == "d":
    imie = input("Imie: ")
    nazwisko = input("Nazwisko: ")
    rok_ur = int(input("Rok urodzenia: "))
    pensja = float(input("Pensja: "))

    pracownik = {"imie": imie, "nazwisko": nazwisko, "rok urodzenia": rok_ur, "pensja": pensja}
    pracownicy.append(pracownik)
    with open("zadanie_1_baza.json", "w") as f:
        json.dump(pracownicy, f)
elif odp == "w":
    print("Pracownicy:")
    for i, pracownik in enumerate(pracownicy):
        print(
            f"[{i +1}] {pracownik['imie']} {pracownik['nazwisko']} - rok: {pracownik['rok urodzenia']}, pensja: {pracownik['pensja']}")
else:
    print("coś nie gra.")


# # pracownik = namedtuple("imie", "nazwisko","rok_urodzenia","pensja")
# pracownik = {"Imie": imie, "Nazwisko": nazwisko, "Rok urodzenia": rok_ur, "Pensja": pensja}
# pracownicy.append(pracownik)
# # print(pracownicy)
# with open("zadanie_1_baza.json", "r+") as f:
#     # json.dump(pracownik, f)
#     # pracownicy = json.load(f)
#     # pracownicy.append(pracownik)
#     json.dump(pracownicy, f)
# main_def()
