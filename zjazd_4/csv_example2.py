import csv

with open("dane/titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=',')
    dlugosci = {}
    for row in data:
        dlugosci[row['Survived']] = dlugosci.get(row['Survived'], 0) + 1

    przezylo = dlugosci['1']
    zginelo = dlugosci['0']

    #print(f"Przeżyło z ogółu {round(100*przezylo/(przezylo+zginelo),2)}")

with open("dane/titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=',')

    how_many_woman = 0
    sum_woman_age = 0

    for row in data:
        if row['Sex']=='female' and row['Age'] != "":
            how_many_woman +=1
            sum_woman_age += float(row['Age'])
    print (f"Średnia wieku kobiet {sum_woman_age / how_many_woman}" )