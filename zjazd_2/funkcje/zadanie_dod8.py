def cyfry_na_tekst(tekst=""):
    tekst = input("Podaj tekst: ")
    slownik = {"0": "zero", "1": "jeden", "2": "dwa", "3": "trzy", "4": "cztery", "5": "pięć", "6": "sześć", "7": "siedem", "8": "osiem",
               "9": "dziewięć"}
    for litera in tekst:
        wydruk = slownik.get(litera, "")
        if wydruk != "":
            print(wydruk, end=" ")

cyfry_na_tekst()