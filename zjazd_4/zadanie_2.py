import json
import urllib.request

with urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/tables/A/?format=json") as f:
    kursy = json.loads(f.read())


#print (kursy[0]['rates'])

#for i in kursy[0]['rates']:
#    print(f"{i['code']} - {i['mid']}")

print("Równowartość 100zł w jakiej walucie podać? Dostępne waluty:", end=" ")
for i in kursy[0]['rates']:
    print(f"{i['code']}", end=" ")
print()
waluta = input("Trzyliterowy skrót: ")

for i in kursy[0]['rates']:
    if i['code'] == waluta:
        wynik = 100/i['mid']

print(f"100 PLN == {wynik}")