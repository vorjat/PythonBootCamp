from requests import get
from bs4 import BeautifulSoup


url = "https://helion.pl/search?qa=&serwisyall=&szukaj=python&wprzyg=&wsprzed=&wyczerp="

response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

books = html_soup.find_all('div', class_="book-info")

for b in books:
    print(b.a.text)