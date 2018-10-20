liczba = int(input("Podaj liczbę do sprawdzenia czy jest pierwszą: "))
# liczba = 0

def czypierwsza(liczba):
    for x in range(2, liczba):
        if liczba % x == 0:
            return False
    return True


print(czypierwsza(liczba))


def test_dla8():
    assert not czypierwsza(8)
