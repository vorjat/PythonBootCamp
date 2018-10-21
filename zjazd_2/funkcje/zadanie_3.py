def policz_znaki(tekst, znak_otwarcia="<", znak_zamkniecia=">"):
    punkt = 0
    suma_punktow = 0

    for litera in tekst:
        if litera == znak_otwarcia:
            punkt += 1
        elif litera == znak_zamkniecia:
            punkt -= 1
        else:
            suma_punktow += punkt

    return suma_punktow


def test1():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4


def test2():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18


def test3():
    assert policz_znaki('a <a<a<a>>>') == 6
