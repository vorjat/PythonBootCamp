lista = []
while True:
    komenda = input("Podaj liczbę, ewentualnie [w]yjdz")
    if komenda == "w":
        break
    lista.append(int(komenda))

print("Nieposortowane:")
print(lista)

n = 0
while n < len(lista):

    for i, liczba in enumerate(lista):
        if i > n:
            min = None

            if min == None:
                min = liczba
                tempindex = i
            else:
                if liczba < min:
                    min = liczba

            if min != lista[n]:
                lista[n], lista[tempindex] = lista[tempindex], lista[n]

    n += 1

print("Posortowane:")
print(lista)