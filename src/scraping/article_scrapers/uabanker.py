import requests
from lxml import html
import resizeimage

from ..article import Article

from .IArticleScraper import IArticleScraper

class Scraper(IArticleScraper):
    def __init__(self):
        self.url = "ua-banker.com.ua"

    def update_article(self, article: Article):
        src = requests.get(article.url).content
        tree = html.fromstring(src)
        text = tree.xpath("/html/body/div[5]/div[3]/div/div[3]/div/div[2]/div[2]")[0]
        text = self.elem_to_str(text)
        article.text = self.get_pure_text(text)
        article.richtext = text
        img = tree.xpath("/html/body/div[5]/div[3]/div/div[3]/div/div[1]/img/@src")[0]
        img = str(img)

        try:
            article.img = "/storage/" +\
            self.process_image("http://" + article.get_source(), img, height=100)
        except resizeimage.imageexceptions.ImageSizeError:
            article.img = ""
