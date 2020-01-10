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

g_data = soup.find_all("div", {"class": "view view-recent-research-articles-and-policy-reports view-id-recent_research_articles_and_policy_reports view-display-id-block view-dom-id-34bec593b75df59bb7b7bef3e707e730"})
 for key in g_data:
        tweet_id = tweet['data-item-id']
        tweet_text = tweet.select('p.tweet-text')[0].get_text()
        all_tweets.append({"id": tweet_id, "text": tweet_text})
        print(all_tweets)


#not working
#g_data = soup.find_all("div", {"class": "view view-recent-research-articles-and-policy-reports view-id-recent_research_articles_and_policy_reports view-display-id-block view-dom-id-34bec593b75df59bb7b7bef3e707e730"})
#len(g_data)
#for item in g_data:
#    print(item.text)
titulo = soup.find_all("div", {"class": "views-field views-field-title"})
resumo = soup.find_all("div", {"class": "views-field views-field-body"})
data = soup.find_all("div", {"class": "views-field views-field-field-publication-date"})
    
soup_dict =  {'Data': data, 'Título': titulo, 'Resumo': resumo}

for key in soup_dict:
    print(key, ':', soup_dict[key].text)
