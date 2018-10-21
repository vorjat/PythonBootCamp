def login_check(login="", haslo=""):
    baza = {"Zbych":"qwerty", "Adam":"qwe123", "Alojz":"qsz321"}
    login = input("Podaj login")
    haslo = input("Podaj haslo")

    if login in baza:
        if haslo == baza[login]:
            print("Autoryzacja pomyślna")
        else:
            print("Błąd logowania")
    else:
        print("Błąd logowania")

login_check()