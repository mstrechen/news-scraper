from queue import Queue
from datetime import datetime

from .INewslistScraper import INewslistScraper

import selenium

from .. import article
from .. import driver

class Scraper(INewslistScraper):
    def __init__(self, limit: int = 100):
        INewslistScraper.__init__(self, limit)
        self._tag_to_url = {
            "ukraine" : "https://tsn.ua/ukrayina",
            "politics" : "https://tsn.ua/politika",
            "sport" : "https://tsn.ua/prosport",
            "celebrities" : "https://tsn.ua/glamur",
            "lady" : "https://tsn.ua/lady",
            "intresting" : "https://tsn.ua/tsikavinki"
        }
        self.driver = driver.driver
        self.xpath = {
            "absolute_article_path" :
            '//*[@id="main-content"]/section/div/article/div/div/h4/a'
        }


    def _load_more(self):
        try:
            button = self.driver.find_element_by_xpath('//*[@id="main-content"]/section/div[12]/div/a')
            self.driver.execute_script("arguments[0].scrollIntoView()", button)
            button.click()
        except (selenium.common.exceptions.ElementClickInterceptedException,\
            selenium.common.exceptions.NoSuchElementException):
            print("Error while clicking...")

    def _convert_datetime(self):
        return datetime.now()

    def _parse_by_tag(self, tag, url, queue: Queue):
        dr = self.driver
        dr.get(url)
        elems = dr.find_elements_by_xpath(self.xpath["absolute_article_path"])
        prev_cnt = 0
        while len(elems) < self.limit and len(elems) != prev_cnt:
            self._load_more()
            prev_cnt = len(elems)
            elems = dr.find_elements_by_xpath(self.xpath["absolute_article_path"])

        for e, _ in zip(elems, range(self.limit)):
            e_url = e.get_attribute("href")
            e_headline = e.text
            dt = self._convert_datetime()
            queue.put_nowait(article.Article(e_url, e_headline, dt, tags=[tag]))



    def push_articles_list(self, queue: Queue):
        for tag in self._tag_to_url:
            self._parse_by_tag(tag, self._tag_to_url[tag], queue)
        
