import sys

nazwa_pliku = sys.argv[1]
try:
    with open(nazwa_pliku) as f:
        for i, line in enumerate(f, start=1):
            print(str(i) + ": " + line, end="")

except FileNotFoundError:
    print("Wrong filename")
