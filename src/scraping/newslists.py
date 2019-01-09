import queue
import time
import threading


from . import newslists_scrapers


newslists = []
articles = queue.Queue()
article_scrapers = {}

def init_newslists_scrapers():
    global newslists
    newslists = newslists_scrapers.scrapers


def init_article_scrapers():
    global article_scrapers
    #article_scrapers = article_scrapers.scrapers

def scrap_newslists():
    while True:
        for newslist in newslists:
            for article in newslist.get_articles_list():
                articles.put_nowait(article)
        time.sleep(20)

def scrap_articles():
    while True:
        article = articles.get(block=True)
        print(article.get_source())

def process_scraping():
    ARTICLES_THREAD = threading.Thread(target=scrap_articles)
    ARTICLES_THREAD.daemon = True
    ARTICLES_THREAD.start()

    NEWSLIST_THREAD = threading.Thread(target=scrap_newslists)
    NEWSLIST_THREAD.daemon = True
    NEWSLIST_THREAD.start()
