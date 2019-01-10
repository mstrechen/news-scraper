import queue
import time
import threading
from elasticsearch import Elasticsearch


from . import newslists_scrapers
from . import article_scrapers

newslists = []
articles = queue.Queue()
article_parsers = {}

def init_newslists_scrapers():
    global newslists
    newslists = newslists_scrapers.scrapers


def init_article_scrapers():
    global article_parsers
    article_parsers = article_scrapers.scrapers

def scrap_newslists():
    while True:
        for newslist in newslists:
            newslist.push_articles_list(articles)
        time.sleep(60 * 5) # update every 5 minutes

def scrap_articles():
    es = Elasticsearch()
    while True:
        article = articles.get(block=True)
        src = article.get_source()
        if article.already_exists(es):
            if article.can_be_updated(es) and src in article_parsers:
                article_parsers[src].update_article(article)
                article.update_in_es(es)
        else:
            if src in article_parsers:
                article_parsers[src].update_article(article)
            article.insert_into_es(es)


def process_scraping():
    ARTICLES_THREAD = threading.Thread(target=scrap_articles)
    ARTICLES_THREAD.daemon = True
    ARTICLES_THREAD.start()

    NEWSLIST_THREAD = threading.Thread(target=scrap_newslists)
    NEWSLIST_THREAD.daemon = True
    NEWSLIST_THREAD.start()
