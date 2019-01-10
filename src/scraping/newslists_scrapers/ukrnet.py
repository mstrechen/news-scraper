from datetime import datetime, timedelta


from .INewslistScraper import INewslistScraper


from .. import article
from .. import driver

class Scraper(INewslistScraper):
    def __init__(self, limit: int = 100):
        INewslistScraper.__init__(self, limit)
        self._tag_to_url = {
            #"politics" : "https://www.ukr.net/news/politika.html",
            "economics" : "https://www.ukr.net/news/jekonomika.html",
            #"accidents" : "https://www.ukr.net/news/proisshestvija.html",
            #"society" : "https://www.ukr.net/news/society.html",
            #"technologies" : "https://www.ukr.net/news/tehnologii.html",
            #"science" : "https://www.ukr.net/news/science.html",
            #"auto" : "https://www.ukr.net/news/avto.html",
            #"sport" : "https://www.ukr.net/news/sport.html",
            #"health" : "https://www.ukr.net/news/zdorove.html",
            #"celebrities" : "https://www.ukr.net/news/show_biznes.html",
            #"global" : "https://www.ukr.net/news/za_rubezhom.html",
            #"fun" : "https://www.ukr.net/news/kurezy.html",
            #"photoreport" : "https://www.ukr.net/news/fotoreportazh.html",
            #"video" : "https://www.ukr.net/news/video.html"
        }
        self.driver = driver.driver
        self.xpath = {
            "absolute_article_path" : '//*[@id="main"]/div/article/section'
        }

        self.monthshorts = [u"січ", u"лют", u"бер", u"кві", u"тра", \
            u"чер", u"лип", u"сер", u"вер", u"жов", u"лис", u"гру"]

    def _load_more(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def _date_from_ukr_to_datetime(self, s: str, index: int):
        mon = s[s.find(' ') + 1 :]
        day = int(s[: s.find(' ')])
        return datetime(datetime.today().year, self.monthshorts.index(mon) + 1, \
        day, index // 60, index % 60)

    def _convert_datetime(self, s: str, index: int):
        s = s.strip()
        if s.find(':') != -1:
            h = int(s[:2])
            m = int(s[3:])
            return datetime.today() + timedelta(hours=h, minutes=m)
        return self._date_from_ukr_to_datetime(s, index)

    def _parse_by_tag(self, tag, url) -> list:
        dr = self.driver
        dr.get(url)
        elems = dr.find_elements_by_xpath(self.xpath["absolute_article_path"])
        while len(elems) < self.limit:
            self._load_more()
            elems = dr.find_elements_by_xpath(self.xpath["absolute_article_path"])

        res = []
        for e, index in zip(elems, range(self.limit)):
            dt = e.find_element_by_tag_name("time")
            dt = self._convert_datetime(dt.text, index)
            e = e.find_element_by_tag_name("div")
            e = e.find_element_by_tag_name("div")
            link = e.find_element_by_tag_name("a")
            e_url = link.get_attribute("href")
            e_headline = link.text
            res.append(article.Article(e_url, e_headline, dt, tags=[tag]))
        return res


    def get_articles_list(self) -> list:
        res = []
        for tag in self._tag_to_url:
            res += self._parse_by_tag(tag, self._tag_to_url[tag])
        return res
