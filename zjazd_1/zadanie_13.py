liczba_dni = int(input("Ile jest dni?"))
suma = 0

Tmin = 100000
Tmax = 0

N = 1
while N <= liczba_dni:
    dana = int(input(f"Podaj temperaturę dla dnia tygodnia nr {N}"))
    suma = suma + dana

    if dana < Tmin :
        Tmin = dana
    if dana > Tmax:
        Tmax = dana

    N += 1

print(f"""Średnia temperatur z {liczba_dni} dni wynosi {suma/liczba_dni}
Minimalna temperatura wyniosła {Tmin}
Maxymalna temperatura wynioska {Tmax}
""")
