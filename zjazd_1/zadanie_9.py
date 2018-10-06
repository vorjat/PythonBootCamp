import datetime
now = datetime.datetime.now()


rok_ur = int(input("Podaj rok urodzenia: "))

if now.year - rok_ur >= 18:
    print("Jesteś pełnoletni!")
else:
    print("Jesteś dzieciorem.")