from abc import ABC, abstractmethod

from lxml import etree
from bs4 import BeautifulSoup
from urllib import parse

from elasticsearch import Elasticsearch

from ..imgsave import download_and_name_img

def is_absolute(url):
    return bool(parse.urlparse(url).netloc)

class IArticleScraper(ABC):
    def __init__(self):
        self.url = ""

    def get_url(self) -> str:
        return self.url

    @abstractmethod
    def update_article(self, article):
        pass

    def elem_to_str(self, elem):
        res = etree.tostring(elem, encoding='utf-8').decode('utf-8')
        for e in elem:
            res += etree.tostring(e, encoding='utf-8').decode('utf-8')
        return res.strip()

    def get_pure_text(self, text):
        return BeautifulSoup(text, "lxml").text


    def process_image(self, site_link, url):
        if not is_absolute(url):
            url = site_link + url
        return download_and_name_img(url)
        
    def get_site_link(self, url):
        r = parse.urlparse(url)
        return r.scheme + "://" + r.netloc