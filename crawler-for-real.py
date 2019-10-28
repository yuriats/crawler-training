# import the library
import requests
from bs4 import BeautifulSoup
import urllib
import lxml
import html5lib

# open url
html = requests.get('http://www.healthdata.org/').text
soup = BeautifulSoup(html, 'lxml')

for article in soup.find_all('article'):
    titulo = article.find('div', class_="views-field views-field-title").a.text
    print(titulo)

    resumo = article.find('div', class_="views-field views-field-body").p.text
    print(resumo)

    data = article.find('div', class_="views-field views-field-field-publication-date").span.text
    print(data)

