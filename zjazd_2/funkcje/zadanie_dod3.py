def rysuj_kwadrat(bok=1):
    bok = int(input("Podaj długość boku: "))
    n = 0
    while n < bok:
        if n == 0 or n == bok - 1:
            print("*" * bok)
        else:
            #print("*", end="")
            #print(" " * (bok - 2), end="")
            #print("*")
            spacje = " "*(bok-2)
            print(f"*{spacje}*")

        n += 1

rysuj_kwadrat()
