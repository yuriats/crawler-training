# import the library
import requests
from bs4 import BeautifulSoup
import urllib
import lxml
import html5lib

# open url
html = requests.get('http://www.healthdata.org/').text
soup = BeautifulSoup(html, 'lxml')

titulo = soup.find_all("div", {"class": "views-field views-field-title"})
resumo = soup.find_all("div", {"class": "views-field views-field-body"})
data = soup.find_all("div", {"class": "views-field views-field-field-publication-date"})

for key in range(3):
    soup_dict =  {'Data': data[key].text, 'Título': titulo[key].text, 'Resumo': resumo[key].text}
    print(key, ':', soup_dict)
    print()
    
