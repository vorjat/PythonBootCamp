lista_produktow = {"sól": 2, "mąka": 3, "kasza": 2.50, "jabłka": 1.50}
magazyn = {"sól": 5, "mąka": 7, "kasza": 12, "jabłka": 33}
koszyk = {}
suma = 0

komenda = "k"
while komenda != "w":
    komenda = input("Chcesz [k]upic, [d]odac czy [w]yjsc?")
    if komenda == "w":
        break
    elif komenda == "d":
        nowy_produkt = input("Co chcesz dodac?")
        ile_nowego = float(input("Ile kg tego produktu?"))
        if nowy_produkt in magazyn:
            magazyn[nowy_produkt] += ile_nowego
        else:
            cena_nowego = float(input("Ile on kosztuje?"))
            lista_produktow[nowy_produkt] = ile_nowego
            magazyn[nowy_produkt] = ile_nowego
    elif komenda == "k":
        produkt = input("Podaj nazwę produktu, lista to: sól, mąka, kasza, jabłka")
        if produkt in lista_produktow:
            ile_kg = int(input("Podaj ile kg chcesz kupić"))
            if ile_kg > int(magazyn[produkt]):
                print("Sorki memorki, nie mamy tyle towaru")
            else:
                cena = lista_produktow[produkt]
                if produkt in koszyk:
                    koszyk[produkt] += ile_kg*cena
                else:
                    koszyk[produkt] = ile_kg * cena
             #   print(f"{ile_kg}kg produktu {produkt} kosztuje {ile_kg*cena}zł")
                suma += ile_kg * cena
                magazyn[produkt] = magazyn[produkt] - ile_kg
        else:
            print("Nie ma takiego towaru")

for produkt in koszyk:
    print (f"{produkt} -  {koszyk[produkt]}")

print(f"Łącznie wychodzi {suma}")
