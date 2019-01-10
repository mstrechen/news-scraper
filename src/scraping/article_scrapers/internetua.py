import requests
from lxml import html, etree
from bs4 import BeautifulSoup

from ..article import Article

from .IArticleScraper import IArticleScraper
from elasticsearch import Elasticsearch


class Scraper(IArticleScraper):
    def __init__(self):
        self.url = "internetua.com"

    def update_article(self, article: Article):
        src = requests.get(article.url).content
        tree = html.fromstring(src)
        text = tree.xpath("/html/body/main/div/div/div[1]/div/div/article/div")[0]
        text = self.elem_to_str(text)
        article.text = self.get_pure_text(text)
        article.richtext = text
        img = tree.xpath("//img/@src")[0]
        img = str(img)

        article.img = "/storage/" + self.process_image("http://" + article.get_source(), img)
