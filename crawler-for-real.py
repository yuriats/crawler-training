# import the library
import requests
from bs4 import BeautifulSoup
import urllib
import lxml
import html5lib

# open url
html = requests.get('http://www.healthdata.org/').text
soup = BeautifulSoup(html, 'lxml')

g_data = soup.find_all("div", {"class": "view view-recent-research-articles-and-policy-reports view-id-recent_research_articles_and_policy_reports view-display-id-block view-dom-id-34bec593b75df59bb7b7bef3e707e730"})

for item in g_data:
    print(item.text)


for article in soup.find_all('span'):
    titulo = article.find('div', class_='views-field views-field-title').a.text
    print(titulo)

    resumo = article.find('div', class_='views-field views-field-body').p.text
    print(resumo)

    data = article.find('div', class_='views-field views-field-field-publication-date').span.text
    print(data)

