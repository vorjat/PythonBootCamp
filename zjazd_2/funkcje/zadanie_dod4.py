def rysuj_romb(x=0):
    x = int(input("Podaj wartosc x (pol wysokosci): "))
    n = 0
    count1 = 0
    count2 = x

    while n < 2 * x:
        if n == 0:
            spacje = " " * (x - 1)
            print(f"{spacje}/\{spacje}")

        elif n <= x - 1:
            count1 += 1
            spacje = " " * count1 * 2
            bok = " " * (x - count1 - 1)
            print(f"{bok}/{spacje}\{bok}")

        elif n > x-1 and n <2*x-1:
             count2 -=1
             spacje = " " * count2 * 2
             bok = " " * (x - count2 - 1)
             print(f"{bok}\{spacje}/{bok}")

        elif n == 2 * x - 1:
            spacje = " " * (x - 1)
            print(f"{spacje}\/{spacje}")

        n += 1

rysuj_romb()
