from datetime import datetime, timedelta
from selenium import webdriver

from .INewslistScraper import INewslistScraper


from .. import article
from .. import driver

class Scraper(INewslistScraper):
    def __init__(self, limit: int = 100):
        INewslistScraper.__init__(self, limit)
        self._tag_to_url = {
            #"ukraine" : "https://tsn.ua/ukrayina",
            "politics" : "https://tsn.ua/politika",
            #"video" : "https://tsn.ua/video/video-novini",
            #"tsn" : "https://tsn.ua/vypusky",
            #"sport" : "https://tsn.ua/prosport",
            #"celebrities" : "https://tsn.ua/glamur",
            #"lady" : "https://tsn.ua/lady",
            #"intresting" : "https://tsn.ua/tsikavinki"
        }
        self.driver = driver.driver
        self.xpath = {
            "absolute_article_path" :
            '//*[@id="main-content"]/section/div/article/div/div/h4/a'
        }


    def _load_more(self):
        self.driver.find_element_by_xpath('//*[@id="main-content"]/section/div[12]/div/a').click()

    def _convert_datetime(self):
        return datetime.now()

    def _parse_by_tag(self, tag, url) -> list:
        dr = self.driver
        dr.get(url)
        elems = dr.find_elements_by_xpath(self.xpath["absolute_article_path"])
        while len(elems) < self.limit:
            self._load_more()
            elems = dr.find_elements_by_xpath(self.xpath["absolute_article_path"])

        res = []
        for e, _ in zip(elems, range(self.limit)):
            e_url = e.get_attribute("href")
            e_headline = e.text
            dt = self._convert_datetime()
            res.append(article.Article(e_url, e_headline, dt, tags=[tag]))
        return res


    def get_articles_list(self) -> list:
        res = []
        for tag in self._tag_to_url:
            res += self._parse_by_tag(tag, self._tag_to_url[tag])
        return res
