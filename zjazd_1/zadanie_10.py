a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
q = input("Podaj rodzaj operacji: ")

if q == "+":
    wynik = f"Wynik: {a+b}"
elif q == "-":
    wynik = f"Wynik: {a-b}"
elif q == "*":
    wynik = f"Wynik: {a*b}"
elif q == "/":
    if b == 0:
        raise ValueError("Nie mozna dzielic przez 0!")
    wynik = f"Wynik: {a/b}"
else:
    wynik = "Podaj prawidłowy znak."

print(wynik)
