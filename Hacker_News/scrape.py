import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser') 
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_news(news):
    return sorted(news, key = lambda k:k['votes'], reverse = True)

def custom_news(links, subtext):
    news = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                news.append({'title': title, 'link': href, 'votes' : points})
    return sort_news(news)

pprint.pprint(custom_news(links, subtext))
