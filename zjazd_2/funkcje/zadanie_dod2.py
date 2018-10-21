def podwajacz(tekst=""):
    tekst = input ("Podaj co mam podwajac")
    tekst_wynikowy =""
    for index, litera in enumerate(tekst):
        if index % 2 == 0 or index == 0:
            tekst_wynikowy += litera
        else:
            tekst_wynikowy += litera*2

    print(tekst_wynikowy)

podwajacz()
