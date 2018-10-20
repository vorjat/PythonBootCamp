a = int(input("Podaj dlugosc w cm: "))
b = int(input("Podaj szerokosc w cm: "))
c = int(input("Podaj glebokosc w cm: "))
v = a * b * c

output = f"""Objetosc wynosi {v}
czy objetosc wieksza niz 1000 cm3? Odpowiedz to {v>1000}
"""

print(output)

if v > 1000:
    print("Hurra, wiekszy niz 1000")
else:
    print("Buuu, nie jest większe niż 1000")
