myText = input("Podaj tekst")
counter = 0

for letter in myText:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
        counter += 1

print(f"Tych samoglosek jest {counter}")
