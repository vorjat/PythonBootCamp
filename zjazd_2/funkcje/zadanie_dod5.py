def rysuj_trojkat(x=0):
    x = int(input("Podaj dlugosc przyprostokatnej: "))

    n = 0
    while n < x:
        if n == 0:
            print("*")
        elif n > 0 and n < x - 1:
            spacje = " " * n
            print(f"*{spacje}*")
        elif n == x - 1:
            print("*" * (x + 1))
        n = n + 1


rysuj_trojkat()
