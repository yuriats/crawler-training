# import the library
import requests
from bs4 import BeautifulSoup
import urllib
import lxml
import html5lib

# open url
html = requests.get('http://www.healthdata.org/').text
soup = BeautifulSoup(html, 'lxml')

for i in range(3):
    titulo = soup.find_all("div", {"class": "views-field views-field-title"})
    resumo = soup.find_all("div", {"class": "views-field views-field-body"})
    data = soup.find_all("div", {"class": "views-field views-field-field-publication-date"})
    print("Data: %s" % data[i].text)
    print("Título: %s" % titulo[i].text)
    print("Resumo: %s" % resumo[i].text)
    print()


#not working
#g_data = soup.find_all("div", {"class": "view view-recent-research-articles-and-policy-reports view-id-recent_research_articles_and_policy_reports view-display-id-block view-dom-id-34bec593b75df59bb7b7bef3e707e730"})
#len(g_data)
#for item in g_data:
#    print(item.text)
