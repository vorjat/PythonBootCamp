X = int(input("Podaj pozycję gracza X: "))
Y = int(input("Podaj pozycję gracza Y: "))

# poza planszą
if X < 0 or X > 100 or Y < 0 or Y > 100:
    print("Poza planszą")
elif Y >= 90 and X >= 10 and X <= 90:
    print("Górna krawędź")
elif Y >= 90 and X >= 90:
    print("Prawy górny róg")
elif X >= 90 and Y >= 10 and Y <= 90:
    print("Prawa krawędź")
elif X>=90 and Y<=10:
    print("Prawy dolny róg")
elif Y<=10 and X>=10 and X<=90:
    print ("Dolna krawędź")
elif Y<=10 and X <=10:
    print ("Lewy dolny róg")
elif X<=10 and Y>=10 and Y<=90:
    print ("Lewa krawędź")
elif X<=10 and Y>=90:
    print("Lewy górny róg")
elif X>10 and X<90 and Y>10 and Y>90:
    print("Centrum")

