from random import randint

Tx = randint(0, 9)
Ty = randint(0, 9)

Px = None
Py = None

while (Px is None and Py is None) or (Px == Tx and Py == Ty):
    Px = randint(0, 9)
    Py = randint(0, 9)

# print(Tx, Ty, Px, Py)

baseDistance = abs(Tx - Px) + abs(Ty - Py)
print(f"Minimalna liczba kroków do skarbu to {baseDistance}")

N = 0
N_all = 0

while True:
    oldDistance = abs(Tx - Px) + abs(Ty - Py)
    command = input("Podaj w/s/a/d by ruszyc.")
    if command == "w":
        Py += 1
    elif command == "a":
        Px -= 1
    elif command == "s":
        Py -= 1
    elif command == "d":
        Px += 1
    else:
        print("Nieprawidlowy ruch")
    newDistance = abs(Tx - Px) + abs(Ty - Py)
    if Px < 0 or Px > 9 or Py < 0 or Py > 9:
        print("Wyszedłeś poza mapę, nie żyjesz.")
        break
    if Px == Tx and Ty == Py:
        N += 1
        N_all +=1
        print(f"Brawo, znalazłeś skarb w {N_all} ruchach!")
        break
    if not (Px == Tx and Ty == Py):
        #        print(f"W tej chwili jesteś o {abs(Tx - Px) + abs(Ty - Py)} pól od skarbu")
        if newDistance > oldDistance:
            print("Zimniej!")
        elif oldDistance > newDistance:
            print("Cieplej!")
        N += 1
        N_all += 1
        if baseDistance * 2 == N:
            print("Za długo! Skarb zmienia miejsce!")
            Tx = randint(0, 9)
            Ty = randint(0, 9)
            baseDistance = abs(Tx - Px) + abs(Ty - Py)
            print(f"Minimalna liczba kroków do skarbu to {baseDistance}")
            N = 0
