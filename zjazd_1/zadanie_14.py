print("Wpisz dowolną liczbę liczb. Zakończ komendą q")
Qmin = None
Qmax = None
suma = 0
N = 1

while True:
    dana = input()
    if dana.lower() == 'q':
        break
    else:
        dana = int(dana)
        if Qmin is None or dana < Qmin:
            Qmin = dana
        if Qmax is None or dana > Qmax:
            Qmax = dana
        suma += dana
        N += 1

if Qmin is None and suma == 0:
    print("Nie wprowadzono żadnych danych.")
else:
    print(f"""Średnia to {suma/N}
Max to {Qmax}
Min to {Qmin}
""")
