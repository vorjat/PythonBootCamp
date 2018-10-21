# delta = b^2 - 4ac
# x1 = (-b - pierw delta)/2a
# x2 = (-b + pierw delta)/2a
import math
def rozwiaz_rownanie_kwadratowe(a=0, b=0, c=0):
    a = float(input("Podaj a rownania: "))
    b = float(input("Podaj b rownania: "))
    c = float(input("Podaj c rownania: "))

    if a == 0:
        print("To nie jest równanie kwadratowe")
    else:
        # policz deltę
        delta = b ** 2 - 4 * a * c
        if delta == 0:
            x1 = -b / 2 * a
            print(f"Jedyny pierwiastek równania to {x1}")
        elif delta < 0:
            print("Delta mniejsza od 0, nie bawimy się w liczby zespolone.")
        else:
            x1 = (-b - math.sqrt(delta)) / 2 * a
            x2 = (-b + math.sqrt(delta)) / 2 * a
            print(f"Pierwiastki równania to {x1} i {x2}.")

rozwiaz_rownanie_kwadratowe()