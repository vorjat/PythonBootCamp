def zabawy_tekstem(podany_tekst, min_wystapien):
    slownik = {}
    finalny = set()
    for litera in podany_tekst:
        litera = litera.lower()
        slownik[litera] = slownik.get(litera, 0) + 1

    for n in slownik:
        if slownik[n] > int(min_wystapien):
            finalny.add(n)

    return finalny


#zm1 = input("Podaj dowolny tekst")
#zm2 = input("Podaj min wystapien")

#print(zabawy_tekstem(zm1, zm2))

def test_pusty():
    assert zabawy_tekstem("",0) == set()

def test_niepusty():
    assert zabawy_tekstem("aaaaabbbccd",2) == {'a','b'}

def test_duzemale():
    assert zabawy_tekstem("AAabBbccd",2) == {'a','b'}