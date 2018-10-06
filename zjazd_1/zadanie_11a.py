MapX = int(input("Podaj X mapy "))
MapY = int(input("Podaj Y mapy "))

X = int(input("Podaj pozycję gracza X: "))
Y = int(input("Podaj pozycję gracza Y: "))

# poza planszą
if X < 0 or X > MapX or Y < 0 or Y > MapY:
    print("Poza planszą")
elif Y >= int(0.9*MapY) and X >= int(0.1*MapX) and X <= int(0.9*MapX):
    print("Górna krawędź")
elif Y >= int(0.9*MapY) and X >= int(0.9*MapX):
    print("Prawy górny róg")
elif X >= int(0.9*MapX) and Y >= int(0.1*MapY) and Y <= int(0.9*MapY):
    print("Prawa krawędź")
elif X>=int(0.9*MapX) and Y<=int(0.1*MapY):
    print("Prawy dolny róg")
elif Y<=int(0.1*MapY) and X>=int(0.1*MapX) and X<=int(0.9*MapX):
    print ("Dolna krawędź")
elif Y<=int(0.1*MapY) and X <=int(0.1*MapX):
    print ("Lewy dolny róg")
elif X<=int(0.1*MapX) and Y>=int(0.1*MapY) and Y<=int(0.9*MapY):
    print ("Lewa krawędź")
elif X<=int(0.1*MapX) and Y>=int(0.9*MapY):
    print("Lewy górny róg")
elif X>int(0.1*MapX) and X<int(0.9*MapX) and Y>10 and Y>int(0.9*MapY):
    print("Centrum")

