N = 1
myList = []

while N < 11:
    dana = (input("Podaj liczbę (max 10). Wpisz q żeby zakończyć"))

    if dana == 'q':
        break

    dana = int(dana)
    myList.append(dana)
    N += 1

print(sum(myList) / len(myList))
