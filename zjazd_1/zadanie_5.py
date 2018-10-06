MiastoA = input("Podaj miasto A")
MiastoB = input("Podaj miasto B")
dystans = input("Podaj dystans")
cena = input("Podaj cenę paliwa")
spalanie = input("Podaj ile spalasz na 100km")
cena_final = int(int(dystans) * float(cena) * float(spalanie) / 100)

print(f"""Miasto A: {MiastoA}
Miasto B: {MiastoB}
dystans {MiastoA}-{MiastoB}: {dystans}
Cena paliwa: {cena}
Spalanie na 100km: {spalanie}

Koszt przejazdu {MiastoA}-{MiastoB} to {cena_final} PLN
""")
