from datetime import datetime
from urllib import parse

from elasticsearch import Elasticsearch

class Article:
    def __init__(self, url: str, headline: str, dt: datetime = datetime.now()):
        self.url = url
        self.datetime = dt
        self.headline = headline
        self.img = ""
        self.text = ""
        self.richtext = ""
        self.src_name = ""
        self.tags = []


    def get_source(self):
        return parse.urlparse(self.url).netloc

    def _normilize_time_for_es(self):
        return self.datetime.strftime("%Y-%m-%dT%H:%M:%S")

    def insert_into_es(self, es: Elasticsearch):
        es.index(index="news", doc_type="article", body={
            "url": self.url,
            "headline": self.headline,
            "datetime": self._normilize_time_for_es(),
            "img": self.img,
            "src_url": self.get_source(),
            "src_name": self.src_name,
            "text": self.text,
            "richtext" : self.richtext,
            "tags": self.tags
        })
