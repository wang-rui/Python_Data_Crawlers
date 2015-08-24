import requests
from bs4 import BeautifulSoup


def trade_spider(stock):
    url = 'http://seekingalpha.com/symbol/' + str(stock)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a', {'sasource': 'qp_latest'}):
        url_news = link.get('href')
        if ( url_news[1:8] == 'article'):
            url_news = 'http://seekingalpha.com' + link.get('href')
            source_code_news = requests.get(url_news)
            plain_text_news = source_code_news.text
            soup_news = BeautifulSoup(plain_text_news)
            for news_link in soup_news.findAll('div', {'id': 'article_body'}):
                news_text = news_link.text
                print(news_text)


trade_spider('IBM')