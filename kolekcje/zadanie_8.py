nawias1 = 0
nawias2 = 0
myText = input("Podaj tekst")

for index, i in enumerate(myText):
    if i == "<":
        nawias1 = index
    if i == ">":
        nawias2 = index

print(nawias2 - nawias1-1)
