podany_tekst = input("Podaj dowolny tekst")
slownik = {}

for litera in podany_tekst:
    slownik[litera] = slownik.get(litera, 0) + 1

for litera in slownik:
    print(f"{litera} - {slownik[litera]}")
