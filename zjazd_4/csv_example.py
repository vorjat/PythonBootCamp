import csv

with open("dane/titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=',')
    M_ifSurvived = 0
    W_ifSurvived = 0
    M_agesum = 0
    W_agesum = 0
    M_count = 0
    M_countAge = 0
    W_count = 0
    W_countAge = 0
    for row in data:
        # przezywalnosc[row['Survived']] = przezywalnosc.get(row['Survived'], 0) + 1
        if row['Sex'] == 'male':
            M_count += 1
            if (row['Age']) != "":
                M_agesum += float(row['Age'])
                M_countAge += 1
            if row['Survived'] == '1':
                M_ifSurvived += 1

        if row['Sex'] == 'female':
            W_count += 1
            if (row['Age']) != "":
                W_agesum += float(row['Age'])
                W_countAge += 1
            if row['Survived'] == '1':
                W_ifSurvived += 1
    # print(przezywalnosc)

    # print(f"Ogółem przeżyło {M_ifSurvived + W_ifSurvived} z {M_count + W_count}, czyli {(M_ifSurvived + W_ifSurvived)/(M_count + W_count)*100}%")
    # print(f"Wśród kobiet przeżyło {W_ifSurvived} z {W_count}, czyli {(W_ifSurvived/W_count)*100}%")
    # print(f"Wśród facetów przeżyło {M_ifSurvived} z {M_count}, czyli {(M_ifSurvived/M_count)*100}%")
    #
    # print(f"Średni wiek (z tych podanych) to {(M_agesum + W_agesum)/(M_countAge+W_countAge)}")
    # print(f"Średni wiek kobiet (z tych podanych) to {(W_agesum/W_countAge)}")
    # print(f"Średni wiek facetów (z tych podanych) to {(M_agesum/M_countAge)}")

#     wyniki = []
#     wyniki.append(["Przeżyło z ogółu", (M_ifSurvived + W_ifSurvived) / (M_count + W_count) * 100])
#     wyniki.append(["Wśród kobiet przeżyło", (W_ifSurvived / W_count) * 100])
#     wyniki.append(["Wśród facetów przeżyło", (M_ifSurvived / M_count) * 100])
#     wyniki.append(["Średni wiek", (M_agesum + W_agesum) / (M_countAge + W_countAge)])
#     wyniki.append(["Średni wiek kobiet", W_agesum / W_countAge])
#     wyniki.append(["Średni wiek facetów", M_agesum / M_countAge])
#
#     print(wyniki)
#
# with open("report.csv", 'w', encoding='utf-8', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(wyniki)

import matplotlib.pyplot as plt

dane = [(M_agesum + W_agesum)/(M_countAge+W_countAge), W_agesum/W_countAge, M_agesum/M_countAge]
index= ['ogółem', 'kobiety', 'faceci']
colors = ['b', 'r', 'g']
plt.bar(index, dane,color = colors)
plt.show()