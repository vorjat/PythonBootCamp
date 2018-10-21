import random


def lotto():
    n = 1
    zbior = set()
    while n <= 6:
        liczba = random.randint(1, 49)
        if not liczba in zbior:
            zbior.add(liczba)
            n += 1

    print(zbior)


lotto()
