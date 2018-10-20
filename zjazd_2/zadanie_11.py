zbior = set()
while True:
    komenda = input("Podaj liczbę, ewentualnie [w]yjdz")
    if komenda == "w":
        break
    zbior.add(int(komenda))

zbior2 = set()

for liczba in zbior:
    if liczba % 2 == 0 and liczba < 101:
        zbior2.add(liczba)

zbior3 = zbior & zbior2
print(zbior3)
print(len(zbior3))
