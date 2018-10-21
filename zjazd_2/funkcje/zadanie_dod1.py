def rozbij_tekst(tekst):
    tekst1 = ""
    tekst2 = ""
    for index, litera in enumerate(tekst):
        if index % 2 == 0 or index == 0:
            tekst1 = tekst1 + litera
            tekst2 = tekst2 + " "
        else:
            tekst2 = tekst2 + litera
            tekst1 = tekst1 + " "

    print(tekst1)
    print(tekst2)


rozbij_tekst("HELLO WORLD!")
