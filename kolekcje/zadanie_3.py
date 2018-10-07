myList = (-1, 1, -2, 2, -3, 3, -1500, 333, 17, 22, -5)

countPlus = 0
countMinus = 0

for N in myList:
    if N > 0:
        countPlus += 1
    elif N < 0:
        countMinus += 1
    else:
        print("???")

print(f"Dodatnich jest {countPlus}, ujemnych jest {countMinus}.")
