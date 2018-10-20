myList = [2, 2, 1, 4, 5, 12, 7, 8, 9, 10]

listMax = max(myList)
listMin = min(myList)

for index, i in enumerate(myList):
    if i == listMax:
        maxIndex = index
    if i == listMin:
        minIndex = index

myList[minIndex] = listMax
myList[maxIndex] = listMin

print(myList)