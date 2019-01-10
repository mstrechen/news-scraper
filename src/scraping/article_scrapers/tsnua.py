import requests
from lxml import html
import resizeimage

from ..article import Article


from .IArticleScraper import IArticleScraper


class Scraper(IArticleScraper):
    def __init__(self):
        self.url = "tsn.ua"

    def update_article(self, article: Article):
        src = requests.get(article.url).content
        tree = html.fromstring(src)
        print(article.url)
        text = tree.xpath('//*[@id="main-content"]//' +
                          'article[contains(@class, "u-content-read") or ' +
                          'contains(@class, "c-main")]')[0]
        text = self.elem_to_str(text)
        
        article.text = self.get_pure_text(text)
        article.richtext = text
        img = tree.xpath("/html/body/div[5]/div[3]/div/div[3]/div/div[1]/img/@src")
        if not img:
            img = tree.xpath('//*[@id="main-content"]/' +
                             'div/div[1]/div/div[2]/header/div[1]/div/div[1]/div[1]/img/@src')

        if img:
            img = img[0]
            img = str(img)
            try:
                article.img = "/storage/" +\
                self.process_image("http://" + article.get_source(), img, height=100)
            except resizeimage.imageexceptions.ImageSizeError:
                article.img = ""